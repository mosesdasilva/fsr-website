# Four Seasons Remodeling Website

This repository contains the new static website for Four Seasons Remodeling, a remodeling and construction company based in Woburn, MA.

The site is built with plain HTML, CSS, and JavaScript. There is no framework, build step, or package install required.

## Current Scope

- modern one-page business website
- orange primary brand direction
- project photography from the archived previous website
- service sections for remodeling and construction work
- trust bar with Angi, BBB, license, and estimate signals
- interactive project gallery, lightbox, mobile navigation, process tabs, and estimate form behavior
- archived copy of the old website for source content and media

## Local Use

Open `index.html` directly in a browser.

Optional local server:

```bash
python3 -m http.server 4173
```

Then open:

```text
http://localhost:4173
```

## Main Files

- `index.html`: page structure and business content
- `styles.css`: visual design, responsive layout, and section styling
- `script.js`: mobile navigation, gallery filters, lightbox, process tabs, form behavior, and scroll interactions
- `source-site/`: archived previous website used only as source material
- `source-site.zip`: zipped snapshot of the archived previous website
- `AGENTS.md`: instructions for future Codex/contributor work
- `docs/PROJECT_NOTES.md`: current project decisions, source notes, and next steps

## GitHub Repository

Remote repository:

https://github.com/mosesdasilva/fsr-website

Default branch:

```text
main
```

## Git Workflow

Recommended workflow:

1. Pull latest `main`.
2. Create a focused branch.
3. Make one reviewable change.
4. Run validation.
5. Commit with a clear message.
6. Push or merge after review.

Example:

```bash
git checkout main
git pull
git checkout -b feature/reviews-section
```

## Validation

For code changes:

```bash
node --check script.js
```

Also verify that local assets referenced from `index.html` exist and manually inspect meaningful layout changes in a browser.

## Next Likely Improvements

- Add a stronger Angi-focused reviews section.
- Add a personal “Why Homeowners Choose Antonio” section.
- Expand service cards into more specific remodeling services.
- Improve the estimate form to match real quote intake needs.
- Add footer links to BBB, Angi, licensing, service area, and contact details.

