# Documentation

> **Last updated:** 2026-10-27

Index of the project documentation. The project is a Persian-first (RTL), bilingual, responsive website for a LEGO center, launched in Iran. For a short introduction, see the [root README](../README.md).

## Purpose of `docs/`

`docs/` is the single home of project requirements, decisions, plans, and testing documentation. The project is in planning: no application code exists yet, so there is no architecture, setup, or deployment documentation yet (see [Not yet available](#not-yet-available)).

Start with the [development plan](development-plan.md). It is the roadmap and the entry point to everything else.

## Structure

```text
docs/
├── README.md                   This index
├── development-plan.md         Roadmap, terminology, current state, shared conventions
├── phases/                     One specification per phase, with stages, features, tasks, and progress
├── project/                    Requirements, page inventory, decision register, Iran constraints
└── testing/                    Testing strategy and master test plan
```

**Sources of truth** (each fact lives in one document; others link to it):

| Subject | Document |
|---|---|
| Requirements and pages | [project-overview.md](project/project-overview.md), [pages.md](project/pages.md) |
| Decisions | [decisions.md](project/decisions.md) |
| Work breakdown and progress | [phases/](phases/) documents |
| How testing is done / what is tested and when | [testing-strategy.md](testing/testing-strategy.md) / [test-plan.md](testing/test-plan.md) |

## Index

### Planning

| Document | Contents |
|---|---|
| [development-plan.md](development-plan.md) | Roadmap, phases, terminology and ID conventions (PAGE, S, F, T, DEC, A), current state, guiding principles, assumptions, key risks, Definition of Done, and the repository structure |
| [phases/phase-1-mvp.md](phases/phase-1-mvp.md) | Phase 1 (MVP): scope, confirmed requirements, proposed quality targets, stages S1.1–S1.8 with features, tasks, and checkable subtasks, and completion criteria |
| [phases/phase-2-album.md](phases/phase-2-album.md) | Phase 2 (آلبوم): provisional plan for a separate PWA album of the center's LEGO sets, integrated into PAGE-016 |
| [phases/phase-3-booking.md](phases/phase-3-booking.md) | Phase 3 (Booking): provisional plan for bookings of events, workshops, and set construction (رزرو برای ساخت) |
| [phases/phase-4-payment.md](phases/phase-4-payment.md) | Phase 4 (Payment): provisional plan for online payments for bookings and sales |

Phases 2–4 are post-MVP and not scheduled.

### Requirements

| Document | Contents |
|---|---|
| [project/project-overview.md](project/project-overview.md) | Project purpose, MVP requirements (including CI/CD and testing), and target visitors |
| [project/pages.md](project/pages.md) | Page inventory with PAGE-IDs and the phase of each page |
| [project/decisions.md](project/decisions.md) | Decision register (DEC-001 onward): pending and decided items, with a template for decision records |
| [project/iran-constraints.md](project/iran-constraints.md) | Connectivity, sanctions, hosting, domain, legal, localization, third-party services, development, testing, and payments in Iran |

### Testing

| Document | Contents |
|---|---|
| [testing/testing-strategy.md](testing/testing-strategy.md) | Draft. Test types, pyramid, proposed tools, environments and data, CI/CD approach, coverage and quality gates, risks, and open questions |
| [testing/test-plan.md](testing/test-plan.md) | Draft. Scope, risk-based test matrix, feature-to-test traceability, test cycles with entry and exit criteria, responsibilities, defect management, regression policy, and release readiness |

### Development, repository, and agent workflow

These files live outside `docs/`.

| File | Contents |
|---|---|
| [../AGENTS.md](../AGENTS.md) | Project-wide instructions for AI agents |
| [../.cursor/rules/documentation.mdc](../.cursor/rules/documentation.mdc) | Cursor rule: how documentation is kept in sync with changes |
| [../.cursor/agents/documentation.md](../.cursor/agents/documentation.md) | Cursor subagent that updates and audits documentation |
| [../.github/workflows/ci.yml](../.github/workflows/ci.yml) | GitHub Actions workflow "CI": currently only the documentation link check |
| [../scripts/check-doc-links.py](../scripts/check-doc-links.py) | Checks that relative links and heading anchors in Markdown files resolve |

### Not yet available

| Category | Status |
|---|---|
| Architecture | Not decided: the technology stack (DEC-016) is pending. The repository structure will be documented in the development plan §10 once decided (T1.3.2.1) |
| Development setup and CI/CD guide | Not written. CI setup and a local workflow are part of T1.3.2.1 and T1.3.4.1 |
| Deployment and operations | Not decided: hosting, domain, and deployment path (DEC-018, DEC-019, DEC-020). Runbooks are part of T1.8.3.2 |
| Maintenance and content update guide | Planned for handover (T1.8.3.2, depends on DEC-017) |
| Post-MVP page requirements | Phases 2–4 pages are added to [pages.md](project/pages.md) when each phase is detailed |

## Keeping documentation accurate

The full workflow is in [../.cursor/rules/documentation.mdc](../.cursor/rules/documentation.mdc). In short:

- Update the affected documents in the same change as the work. A change is not done until its documents are.
- Edit the source of truth and link to it; do not copy content between documents.
- Record decisions in [decisions.md](project/decisions.md) first, then update every document that references the DEC-ID. Do not mark a decision as decided without confirmation.
- Check a subtask only when its work is verifiably done. Never renumber or reuse IDs.
- Update the `Last updated` line of every document you change.
- Keep each document in its own language; do not translate Persian page names or terms.
- Run `python scripts/check-doc-links.py` before committing. CI runs the same check.
- When you add a document, add it to this index. Add it to the development plan's §1 documentation map as well.
