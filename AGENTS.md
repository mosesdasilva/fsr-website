# Four Seasons Remodeling Codex Guide

This project is a lightweight static website for Four Seasons Remodeling, a Woburn, MA remodeling and construction business.

Work in small, reviewable increments. Prefer focused branches and separate commits for separate ideas.

## AI Pairing Workflow

Use AI as a pair programmer, not as an unsupervised product owner.

- The user owns the business intent, priority, taste, and final approval.
- The agent owns implementation options, tradeoff analysis, file edits, validation, and documentation updates.
- The agent may propose the "how", but must stay anchored to the user's "what" and "why".
- When a request is ambiguous, make the smallest reasonable assumption and state it.
- If a request risks overbuilding, broad refactoring, fragile claims, or unnecessary tooling, pause and explain the tradeoff before implementing.
- If a repeated workflow, source, decision, or limitation is discovered, add it to `docs/PROJECT_NOTES.md` or `AGENTS.md` so future sessions start with that context.

This follows the working philosophy from Fabio Akita's AI project writing: fast output only helps when paired with human judgment, small releases, validation, continuous refactoring, and living documentation.

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

## Production-Ready Static Site Commits

Every commit should leave the site in a usable state.

- Do not commit "broken now, fix later" intermediate states.
- Keep each commit focused enough that it can be reviewed or reverted by itself.
- For visual changes, preserve mobile and desktop usability.
- For JavaScript changes, keep existing interactions working unless the change intentionally replaces them.
- For documentation changes, avoid changing site behavior in the same commit.
- Push branches only after the working tree is clean and the relevant validation has been run.

## Design Direction

- Modern remodeling/construction business site.
- Orange is the primary brand color.
- Design should feel professional, grounded, and trust-building.
- Use strong photography, clear service sections, concise proof points, and direct calls to action.
- Keep the first screen focused on the business offer, not a generic landing page.
- Avoid decorative UI that does not support trust, service clarity, or conversion.
- Do not use text characters as UI imagery for controls, icons, arrows, or visual indicators. Prefer inline SVG, CSS-drawn shapes, or a proper icon library when imagery is needed.

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

## Source Claims And Public Trust Signals

Public trust claims need an explicit source.

- Angi rating and review count should come from the Angi profile.
- BBB accreditation, A+ rating, and license references should come from the BBB profile or official Massachusetts records.
- Phone, location, owner, services, and experience claims may come from the archived source site unless superseded by a newer source.
- Do not invent or soften claims to sound better. If the exact source wording is uncertain, keep the site copy conservative.
- When adding a new public claim, update `docs/PROJECT_NOTES.md` with the source and date if the detail is likely to change.

Do not add warranty, guarantee, financing, timeline, or pricing language unless the owner provides the exact policy.

## When To Refactor

Refactor continuously, but keep it small.

- Refactor when a change creates obvious duplication or makes a file harder to understand.
- Prefer small extraction and naming improvements during the feature branch that introduces the need.
- Do not mix a broad cleanup with a content/design feature unless the cleanup is required to complete it.
- Watch `styles.css` and `script.js` for junk-drawer growth. If a section becomes hard to scan, reorganize it while the change is still small.
- Keep the no-build-step constraint unless the project clearly outgrows plain HTML/CSS/JS and the owner approves a tooling change.

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
