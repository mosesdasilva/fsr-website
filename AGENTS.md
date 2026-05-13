# Four Seasons Remodeling Codex Guide

This project is a lightweight static website for Four Seasons Remodeling, a Woburn, MA remodeling and construction business.

Work in small, reviewable increments. Prefer focused branches and separate commits for separate ideas.

## Product Goal

Build a modern, trustworthy business website that helps homeowners understand the company, see proof of work, and request a free estimate.

The site should communicate:

- local Woburn, MA remodeling expertise
- kitchen, bathroom, carpentry, tile, windows, doors, painting, and whole-home renovation services
- trust signals from Angi, BBB, licensing, photos, and reviews
- a hands-on, family-owned contractor experience led by Antonio DaSilva

## Current Technical Direction

Keep the project static and simple:

- `index.html`
- `styles.css`
- `script.js`
- no framework
- no build step
- no package install required

The site should work when opened directly as `index.html`. A local server can be used for testing, but should not be required for normal review.

## Source Material

Use these as content references, not as design templates:

- `source-site/download/`: archived copy of the previous website
- `source-site/manifest.json`: list of archived source pages and assets
- `source-site/archive_site.py`: one-off crawler used to create the archive
- BBB profile: https://www.bbb.org/us/ma/woburn/profile/remodeling/four-seasons-remodeling-painting-services-0021-512915
- Angi profile: https://www.angi.com/companylist/us/ma/woburn/four-seasons-remodeling-and-painting-reviews-1.htm

When adding trust claims, ratings, review counts, license numbers, or accreditation details, keep the source obvious in nearby documentation or comments if useful.

## Implementation Principles

- Keep HTML semantic and readable.
- Keep CSS organized by page section and responsive behavior.
- Keep JavaScript plain, small, and interaction-focused.
- Prefer real project photos from the archived source assets over generic stock imagery.
- Do not copy the old Weebly design; use it only for business context and media.
- Do not introduce a framework, bundler, CMS, or dependency unless explicitly requested.
- Avoid broad refactors while making content or design updates.
- Keep unrelated cleanup separate from behavior or content changes.

## Design Direction

- Modern remodeling/construction business site.
- Orange is the primary brand color.
- Design should feel professional, grounded, and trust-building.
- Use strong photography, clear service sections, concise proof points, and direct calls to action.
- Keep the first screen focused on the business offer, not a generic landing page.
- Avoid decorative UI that does not support trust, service clarity, or conversion.

## Content And Claims

Be careful with claims that may change or require verification.

Current sourced claims:

- `5.0 on Angi`
- `77 reviews`
- `BBB Accredited A+`
- `Licensed #188474`
- `Free estimates`
- `30+ years of experience`
- `Woburn, MA 01801`
- `(978) 876-7270`

If changing these, verify against the source profile or ask the owner.

Avoid making specific warranty, pricing, timeline, financing, or guarantee claims unless the owner provides exact wording.

## Git Workflow

Use branches for reviewable work:

1. Start from `main`.
2. Create a focused branch, for example `docs/project-agent-guidance` or `feature/reviews-section`.
3. Make one coherent change.
4. Run lightweight validation.
5. Commit with a clear message.
6. Push the branch or merge to `main` only after review.

For simple static-site changes, validation should include:

- `node --check script.js`
- verify local asset references in `index.html`
- manually inspect the page in a browser when layout changes are meaningful

## Documentation Expectations

Update documentation when decisions or source-of-truth details change.

Primary docs:

- `README.md`: project orientation and local use
- `docs/PROJECT_NOTES.md`: current decisions, source notes, next steps
- `AGENTS.md`: contributor and Codex guidance

Keep docs concise and practical. Prefer current status, clear file maps, and next likely actions over long process descriptions.

