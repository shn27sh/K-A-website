# Documentation

This directory is the source of product, planning, and testing documentation for K-A-website. The GitHub landing page for the repository is the [root README](../README.md); this file is the **index of documents**, not a second project overview.

There is no application implementation in the repo yet. These files describe intent. Keep them in sync when pages, phases, or quality gates change.

## Structure

```
docs/
├── README.md                 ← this index
├── project/                  ← product and delivery planning
│   ├── project-overview.md
│   ├── pages.md
│   └── development-plan.md
└── testing/                  ← QA strategy and master test plan
    ├── testing-strategy.md
    └── test-plan.md
```

## Project planning and requirements

| Document | Description |
| --- | --- |
| [project/project-overview.md](project/project-overview.md) | Why the site exists: present the center, programs, later booking, parent trust, community, B2B outreach. Defines MVP launch items (pages, responsive, FAQ, bilingual *as listed there*, map, SEO, nav, social, performance, analytics, CI/CD, tests) and audiences (parents, schools/organizations, children). |
| [project/pages.md](project/pages.md) | Sitemap-style inventory PAGE-001 through PAGE-016 with Farsi section bullets (home, services, gallery, about, contact, کارن و کیانا, workshops, cooperation, FAQ, sales subtree, آلبوم). PAGE-005 and PAGE-015 are marked TBD. PAGE-014 is assigned in two places. |
| [project/development-plan.md](project/development-plan.md) | Actionable roadmap: Farsi-first RTL vs bilingual conflict, current docs-only state, Phase 1–4 scope, Iran launch constraints, Tasks 0–13 with acceptance criteria, UI/a11y notes, risks, open questions, definition of done. Stack is explicitly **not** chosen. |

## Architecture

Not yet available. The development plan defers stack, hosting, CMS, and Iran vendors until those decisions are necessary. There is no architecture or ADR directory.

## Development

Use [project/development-plan.md](project/development-plan.md) as the development guide (task order, bootstrap, pages, forms, CI, Iran launch). There is no separate coding-standards or setup guide because there is no application tree.

## Testing

| Document | Description |
| --- | --- |
| [testing/testing-strategy.md](testing/testing-strategy.md) | Pre-implementation strategy: facts vs assumptions, white-box/black-box, unit through Iran smoke, Phase 1 vs later pyramid, proposed tools (approval IDs D1–D8), environments, CI jobs, coverage caveats, quality gates, testing roadmap mapped to development-plan tasks. |
| [testing/test-plan.md](testing/test-plan.md) | Master test plan: in/out of scope features, traceability, risk-based feature×test-type matrix, priorities, environments/browsers (placeholders), data/accounts, entry/exit criteria, schedule vs milestones (dates `TBD`), manual vs automated ownership, defect S/P definitions, regression policy, release readiness, risks D9–D13. |

No executable tests, CI workflows, or coverage reports exist.

## Deployment and maintenance

Not yet available. Iran hosting, DNS, TLS, analytics, map, and payment vendors are unresolved. Launch concerns are discussed inside the development plan (especially §4.4 and Task 10) and as Iran smoke in the testing docs—not as a runbook.

## Planned documentation (does not exist)

Do not link these as if they were files:

- Architecture / ADRs (after stack Task 3)
- Iran launch constraints brief (optional sibling to the development plan, Task 1)
- Environment example file (only after secrets exist)
- Contribution guide, license, changelog
- Deployment/runbook and operations/maintenance docs
- Album PWA contract (required before Phase 2 tests)

## Keeping docs accurate

- PAGE-IDs, phases, and bilingual vs Farsi-first policy must match across `pages.md`, `project-overview.md`, `development-plan.md`, and the testing docs after Task 0 alignment.
- Do not describe application commands, env vars, or CI jobs until they exist in the repo.
- Testing strategy and test plan share IDs (A1–A7, D1–D8); if one changes, update the other.
- When implementation starts, update the root README status and this index in the same change as new `docs/` files.
- Do not invent copy, vendors, or dates; use explicit TBD placeholders as the test plan does.
