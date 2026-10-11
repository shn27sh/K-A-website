# K-A-website

Persian/Farsi-first, RTL website for a LEGO center where children construct LEGO sets.

Remote: [https://github.com/shn27sh/K-A-website](https://github.com/shn27sh/K-A-website) (`main`).

## Overview

The site is meant to help visitors understand the center, its offerings, atmosphere, facilities, and educational approach. Primary audience is parents; schools, teachers, business owners, and مهدکودک‌ها are secondary; children and teenagers are tertiary.

Intended delivery: design pages in Figma, implement them in this repository, then launch in Iran (hosting, connectivity, testing, and later Iranian payment constraints).

Product purposes and MVP launch items are defined in [`docs/project/project-overview.md`](docs/project/project-overview.md). Page inventory is in [`docs/project/pages.md`](docs/project/pages.md). The implementation roadmap is in [`docs/project/development-plan.md`](docs/project/development-plan.md).

## Current status

**Documentation-only.** There is no application source, package manifest, CI pipeline, hosting configuration, or implemented UI.

| Exists | Does not exist |
| --- | --- |
| Product and page docs | Runnable website |
| Development plan | Chosen technology stack |
| Testing strategy and master test plan | Automated tests, lint, or build commands |
| GitHub remote on `main` | `.env` / example env file, license file, contribution guide |

No website features are implemented. Treat everything below as **planned** unless noted.

## Planned features

Phased as documented. Phase assignment for some pages is inferred in the development plan; `pages.md` does not label every page.

**Phase 1 — MVP (informational site)**  
Showcase pages (home, services, ساخت لگو, لگو بوست, gallery, about, contact, کارن و کیانا, workshops as display-only, cooperation form, FAQ, sales/purchase guidance). RTL Farsi layout, responsive mobile/tablet, basic SEO, map, social links, analytics, CI/CD and tests before deploy. Visitors do **not** book or pay online.

**Phase 2 — آلبوم**  
Integrate an existing separate PWA into PAGE-016 (set photos/specs, availability, predicted free time). Integration method is unresolved.

**Phase 3 — Booking**  
Events, workshops (visible capacity), رزرو برای ساخت.

**Phase 4 — Payment**  
Iranian-capable payment for bookings and in-scope sales.

Explicitly later/TBD in `pages.md`: PAGE-005 (بازی‌سازی با سوپرماریو), PAGE-015 (pieces by part code).

Unresolved product conflicts (do not assume either side in code): `project-overview.md` lists bilingual MVP; conversation/development plan treat the public site as Farsi-first RTL. PAGE-014 is assigned twice in `pages.md`.

## Project structure

```
K-A-website/
├── README.md
└── docs/
    ├── README.md
    ├── project/
    │   ├── development-plan.md
    │   ├── pages.md
    │   └── project-overview.md
    └── testing/
        ├── test-plan.md
        └── testing-strategy.md
```

There is no `src/`, `package.json`, CI config, or `.env.example` in this repository.

## Prerequisites

None for running an application: nothing is bootstrapped yet.

To work on documentation: Git, and a Markdown editor. A Node/Python/other runtime will be required only after a stack is chosen (`development-plan.md` Task 3). That decision is not recorded.

## Environment variables

No environment files or variable names are defined. Do not invent `.env` keys. When secrets are introduced, they must not be committed (see Security).

## Commands

There are **no** project-defined development, build, lint, or test commands (no package manager scripts, Makefiles, or task runners). Do not assume `npm test` or similar until a stack and scripts exist.

## Testing

Testing is planned, not implemented. Quality bar in `project-overview.md`: unit/integration for critical functionality, E2E for core journeys, basic responsive and accessibility checks, all in CI before deploy. Iran reachability is an additional launch concern.

- Strategy (pyramid, types, proposed tools): [`docs/testing/testing-strategy.md`](docs/testing/testing-strategy.md)
- Master test plan (scope, matrix, gates, release readiness): [`docs/testing/test-plan.md`](docs/testing/test-plan.md)

Tool choices (for example Playwright) are **proposals requiring approval**. They are not installed.

## Documentation

Index of all docs: [`docs/README.md`](docs/README.md)

| Document | Contents |
| --- | --- |
| [Project overview](docs/project/project-overview.md) | Purpose, MVP checklist, audiences |
| [Pages](docs/project/pages.md) | PAGE-001 … PAGE-016 content outlines |
| [Development plan](docs/project/development-plan.md) | Phases, tasks, Iran constraints, definition of done |
| [Testing strategy](docs/testing/testing-strategy.md) | How testing should be done |
| [Test plan](docs/testing/test-plan.md) | How testing is coordinated |

Architecture, deployment runbooks, and maintenance docs are **not** in the repository.

## Development workflow

No `CONTRIBUTING.md` exists. Documented intent:

1. Align product docs (development-plan Task 0) where IDs and language policy conflict.
2. Record Iran launch constraints (Task 1).
3. Design Phase 1 in Figma (Task 2).
4. Choose stack and bootstrap (Tasks 3–4).
5. Implement pages from Figma; add tests and CI before Iran launch (Tasks 5–10).

Collaboration branch is `main`. Overview requires automated validation before merge and consistent deploy of approved changes; **no CI workflow file exists yet**.

## Security

- Do not commit credentials, API tokens, PSP keys, or production `.env` files.
- Phase 1 planned controls (when code exists): HTTPS, safe form handling, no secrets in the client or git, dependency hygiene.
- Do not run payment or booking tests against production (see test plan).

## License

No license file is present in this repository. Licensing is unspecified.
