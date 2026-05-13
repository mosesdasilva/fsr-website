# Project Notes

## Current Status

The project has a static website baseline and a trust bar update merged into `main`.

Current live source files:

- `index.html`
- `styles.css`
- `script.js`

The old website archive remains in `source-site/` for source content, media, and business context only.

## Repository

- GitHub: https://github.com/mosesdasilva/fsr-website
- Visibility: private
- Default branch: `main`

## Current Branching Pattern

Use separate branches for each reviewable change.

Recent examples:

- `feature/trust-bar`
- `docs/project-agent-guidance`

## Business Context

Four Seasons Remodeling is a family-owned remodeling and construction company based in Woburn, MA.

Important business details currently used by the site:

- Phone: `(978) 876-7270`
- Location: `Woburn, MA 01801`
- Owner/founder context: Antonio DaSilva
- Experience claim: `30+ years of experience`
- Core services: kitchen remodeling, bathroom renovation, whole-home remodeling, general contracting, carpentry, tile, windows, doors, painting, and finish work

## Content Sources

Archived previous website:

- `source-site/download/index.html`
- `source-site/download/www.fourseasonsremodelingma.com/services.html`
- `source-site/download/www.fourseasonsremodelingma.com/recent-projects-gallery.html`
- `source-site/download/www.fourseasonsremodelingma.com/testimonials.html`
- `source-site/download/www.fourseasonsremodelingma.com/contact.html`

External profiles:

- BBB: https://www.bbb.org/us/ma/woburn/profile/remodeling/four-seasons-remodeling-painting-services-0021-512915
- Angi: https://www.angi.com/companylist/us/ma/woburn/four-seasons-remodeling-and-painting-reviews-1.htm

## Current Trust Claims

The trust bar currently uses:

- `5.0 on Angi`
- `77 reviews`
- `BBB Accredited A+`
- `Licensed #188474`
- `Free estimates`

The BBB and license items link to the BBB profile.

The Angi rating and review count link to the Angi profile.

## Design Decisions

- Use orange as the primary brand color.
- Use real project images from the source archive.
- Keep the site modern, clean, and trust-forward.
- Avoid copying the previous Weebly layout.
- Use the source archive only for business context, media, and historical content.
- Keep the site static with no build step.
- Deploy the static site with GitHub Pages through GitHub Actions. GitHub repository settings still need Pages `Source` set to `GitHub Actions`. The workflow publishes only `index.html`, `styles.css`, `script.js`, and archived assets needed by the page.

## AI Workflow Influence

The project workflow is influenced by Fabio Akita's writing on AI-assisted development:

- Article: https://akitaonrails.com/en/2026/02/20/zero-to-post-production-in-1-week-using-ai-on-real-projects-behind-the-m-akita-chronicles/
- GitHub: https://github.com/akitaonrails

Relevant principles for this project:

- The owner defines the business intent, priorities, and final taste.
- The agent proposes and executes implementation, but should surface tradeoffs.
- Work should happen in small production-ready increments.
- Documentation should evolve whenever new project context is discovered.
- The agent tends to overbuild if unchecked, so simple static-site solutions are preferred until there is a clear reason to add tooling.
- Refactoring should be continuous and small, not a late emergency cleanup.

## Next Proposed Work

Implement improvements one at a time:

1. Add a stronger Angi-focused reviews section.
2. Add a “Why Homeowners Choose Antonio” section.
3. Expand the service cards into more specific services.
4. Improve the estimate form with town, project timeline, budget range, and referral source fields.
5. Add a more complete footer with source links and license/accreditation details.

## Validation Notes

Last known lightweight checks:

- `node --check script.js`
- local asset reference check for `index.html`

Manual browser review is recommended for layout changes.
