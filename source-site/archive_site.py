from __future__ import annotations

import hashlib
import json
import mimetypes
import re
import time
from collections import deque
from pathlib import Path
from typing import Iterable
from urllib.parse import urldefrag, urljoin, urlparse
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup


START_URL = "https://www.fourseasonsremodelingma.com/"
OUTPUT_DIR = Path(__file__).resolve().parent / "download"
MANIFEST_PATH = Path(__file__).resolve().parent / "manifest.json"
MAX_PAGES = 100
MAX_ASSETS = 500
REQUEST_DELAY_SECONDS = 0.15
USER_AGENT = "Mozilla/5.0 (compatible; Codex site archive for owner rebuild)"

PAGE_ATTRS = {
    "a": ["href"],
}

ASSET_ATTRS = {
    "img": ["src", "srcset"],
    "source": ["src", "srcset"],
    "script": ["src"],
    "link": ["href"],
    "video": ["src", "poster"],
    "audio": ["src"],
}


def fetch(url: str) -> tuple[bytes, str]:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    with urlopen(request, timeout=25) as response:
        content_type = response.headers.get("content-type", "").split(";")[0].strip()
        return response.read(), content_type


def clean_url(url: str) -> str:
    return urldefrag(url)[0]


def is_http_url(url: str) -> bool:
    return urlparse(url).scheme in {"http", "https"}


def same_site(url: str) -> bool:
    return urlparse(url).netloc.lower().removeprefix("www.") == "fourseasonsremodelingma.com"


def page_path(url: str) -> Path:
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    if not path:
        return OUTPUT_DIR / "index.html"
    suffix = Path(path).suffix
    if suffix:
        return OUTPUT_DIR / parsed.netloc / path
    return OUTPUT_DIR / parsed.netloc / path / "index.html"


def asset_path(url: str, content_type: str = "") -> Path:
    parsed = urlparse(url)
    path = parsed.path.strip("/")
    if not path or path.endswith("/"):
        digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:12]
        ext = mimetypes.guess_extension(content_type) or ".bin"
        path = f"asset-{digest}{ext}"
    return OUTPUT_DIR / "assets" / parsed.netloc / path


def write_file(path: Path, body: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(body)


def iter_srcset(value: str) -> Iterable[str]:
    for item in value.split(","):
        candidate = item.strip().split(" ")[0]
        if candidate:
            yield candidate


def rewrite_srcset(value: str, page_file: Path, replacements: dict[str, Path]) -> str:
    parts = []
    for item in value.split(","):
        stripped = item.strip()
        bits = stripped.split(" ")
        url = bits[0]
        if url in replacements:
            bits[0] = relative_link(page_file, replacements[url])
        parts.append(" ".join(bits))
    return ", ".join(parts)


def relative_link(from_file: Path, to_file: Path) -> str:
    return Path(
        __import__("os").path.relpath(to_file, from_file.parent)
    ).as_posix()


def extract_links(soup: BeautifulSoup, base_url: str, attrs: dict[str, list[str]]) -> set[str]:
    links = set()
    for tag, attr_names in attrs.items():
        for node in soup.find_all(tag):
            for attr in attr_names:
                value = node.get(attr)
                if not value:
                    continue
                if attr == "srcset":
                    links.update(clean_url(urljoin(base_url, item)) for item in iter_srcset(value))
                else:
                    links.add(clean_url(urljoin(base_url, value)))
    return {link for link in links if is_http_url(link)}


def archive() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    page_queue = deque([START_URL])
    seen_pages: set[str] = set()
    seen_assets: set[str] = set()
    asset_paths: dict[str, Path] = {}
    manifest = {"start_url": START_URL, "pages": {}, "assets": {}, "errors": []}

    while page_queue and len(seen_pages) < MAX_PAGES:
        page_url = clean_url(page_queue.popleft())
        if page_url in seen_pages or not same_site(page_url):
            continue
        seen_pages.add(page_url)
        try:
            body, content_type = fetch(page_url)
            time.sleep(REQUEST_DELAY_SECONDS)
        except Exception as exc:
            manifest["errors"].append({"url": page_url, "error": repr(exc)})
            continue

        file_path = page_path(page_url)
        if "html" not in content_type:
            target = asset_path(page_url, content_type)
            write_file(target, body)
            manifest["assets"][page_url] = str(target.relative_to(OUTPUT_DIR))
            continue

        soup = BeautifulSoup(body, "html.parser")
        page_links = extract_links(soup, page_url, PAGE_ATTRS)
        asset_links = extract_links(soup, page_url, ASSET_ATTRS)

        for link in page_links:
            if same_site(link) and link not in seen_pages:
                page_queue.append(link)

        for asset_url in sorted(asset_links):
            if len(seen_assets) >= MAX_ASSETS:
                break
            target = asset_path(asset_url)
            if asset_url in asset_paths:
                continue
            if target.exists():
                asset_paths[asset_url] = target
                manifest["assets"][asset_url] = str(target.relative_to(OUTPUT_DIR))
                continue
            if asset_url in seen_assets:
                continue
            seen_assets.add(asset_url)
            try:
                asset_body, asset_type = fetch(asset_url)
                time.sleep(REQUEST_DELAY_SECONDS)
                target = asset_path(asset_url, asset_type)
                write_file(target, asset_body)
                asset_paths[asset_url] = target
                manifest["assets"][asset_url] = str(target.relative_to(OUTPUT_DIR))
            except Exception as exc:
                manifest["errors"].append({"url": asset_url, "error": repr(exc)})

        for tag, attr_names in ASSET_ATTRS.items():
            for node in soup.find_all(tag):
                for attr in attr_names:
                    value = node.get(attr)
                    if not value:
                        continue
                    if attr == "srcset":
                        resolved = {clean_url(urljoin(page_url, item)): item for item in iter_srcset(value)}
                        replacements = {
                            original: asset_paths[absolute]
                            for absolute, original in resolved.items()
                            if absolute in asset_paths
                        }
                        if replacements:
                            node[attr] = rewrite_srcset(value, file_path, replacements)
                    else:
                        absolute = clean_url(urljoin(page_url, value))
                        if absolute in asset_paths:
                            node[attr] = relative_link(file_path, asset_paths[absolute])

        for node in soup.find_all("a"):
            href = node.get("href")
            if not href:
                continue
            absolute = clean_url(urljoin(page_url, href))
            if same_site(absolute):
                node["href"] = relative_link(file_path, page_path(absolute))

        write_file(file_path, str(soup).encode("utf-8"))
        manifest["pages"][page_url] = str(file_path.relative_to(OUTPUT_DIR))

    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Archived {len(manifest['pages'])} pages and {len(manifest['assets'])} assets.")
    if manifest["errors"]:
        print(f"Completed with {len(manifest['errors'])} fetch errors. See {MANIFEST_PATH}.")


if __name__ == "__main__":
    archive()
