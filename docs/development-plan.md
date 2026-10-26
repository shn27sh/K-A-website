# Development Plan

> **Status:** Active · **Current phase:** Phase 1 (MVP), Stage S1.1 · **Last updated:** 2026-10-26

The central roadmap and entry point for the project. It describes the whole project at a glance. Detailed features, development tasks, and subtasks live in the phase documents.

## 1. Documentation Map

| Document | Purpose |
|---|---|
| [development-plan.md](development-plan.md) | Roadmap, scope, phases, shared conventions, Definition of Done (this document) |
| [phases/phase-1-mvp.md](phases/phase-1-mvp.md) | Phase 1 (MVP) detailed specification |
| [phases/phase-2-album.md](phases/phase-2-album.md) | Phase 2 (آلبوم) detailed specification |
| [phases/phase-3-booking.md](phases/phase-3-booking.md) | Phase 3 (Booking) detailed specification |
| [phases/phase-4-payment.md](phases/phase-4-payment.md) | Phase 4 (Payment) detailed specification |
| [project/project-overview.md](project/project-overview.md) | Source requirements: purpose, MVP requirements, target visitors |
| [project/pages.md](project/pages.md) | Page inventory and PAGE-IDs |
| [project/decisions.md](project/decisions.md) | Decision register: pending and decided items (DEC-IDs) |
| [project/iran-constraints.md](project/iran-constraints.md) | Iran-specific constraints: connectivity, hosting, services, legal, localization, testing |
| [testing/testing-strategy.md](testing/testing-strategy.md) | Testing approach, tools, quality gates, and coverage targets across all phases (Draft) |

**Sources of truth:** requirements → `project-overview.md` and `pages.md`; decisions → `decisions.md`; work breakdown and progress → phase documents. This document summarizes and links; it does not repeat details.

## 2. Project Overview

A Persian-first (RTL), bilingual (Persian/English), responsive website for a LEGO center where children build LEGO sets. It is launched in Iran for an audience in Iran. The project starts as a content and marketing website (the MVP) and expands in post-MVP phases with a digital album, a booking system, and a payment system.

**Objectives** (from [project-overview.md](project/project-overview.md) §1):

1. Present the center: what it offers, who it is for, its atmosphere, activities, facilities, educational approach, and values.
2. Display activities and programs: ساخت لگو, لگو بوست robotics workshops, competitions.
3. Build trust with parents: safety, instructors, educational benefits, policies, photos, FAQs.
4. Promote the center's community: children's projects, events, competitions, achievements.
5. Give schools, business owners, and organizations a way to request group activities, educational programs, or special events.
6. Enable bookings (Phase 3) and payments (Phase 4).

**Target visitors** (§3): parents (primary); schools, teachers, business owners, and مهدکودک‌ها (secondary); children and teenagers.

The center's official name is pending (DEC-012); documents refer to it as "the center".

## 3. Terminology and Identifiers

### 3.1 Hierarchy

Project → MVP → Phase → Stage → Feature → Task → Subtask

| Term | Meaning |
|---|---|
| Project | The entire product, including the MVP and all post-MVP development |
| MVP | The minimum usable version that can be launched and deliver the core value |
| Phase | A major roadmap part grouping related stages; a significant milestone |
| Stage | A meaningful step within a phase toward a specific objective |
| Feature | A specific capability or functionality the system must provide |
| Task | A discrete unit of work to implement, integrate, test, document, or deliver a feature |
| Subtask | A smaller unit of work that belongs to a task |

Phase 1 delivers the MVP. Phases 2–4 are post-MVP and are not part of the MVP unless explicitly decided.

### 3.2 Identifier Conventions

| Item | Format | Example | Notes |
|---|---|---|---|
| Page | `PAGE-###` | PAGE-010 | Existing convention in `pages.md`; never renumber. Next free ID: PAGE-017 |
| Stage | `S{phase}.{n}` | S1.3 | Defined in phase documents |
| Feature | `F{phase}.{stage}.{n}` | F1.3.2 | |
| Task | `T{phase}.{stage}.{feature}.{n}` | T1.3.2.1 | |
| Subtask | Checklist item under its task | `- [ ] …` | Checked when done |
| Decision | `DEC-###` | DEC-016 | Registered in `decisions.md` |
| Assumption | `A-#` | A-2 | Listed in §11 |

IDs are never reused. Dropped items stay in place, marked *Dropped* with a reference to the decision.

## 4. Current State (2026-10-26)

| Area | State |
|---|---|
| Documentation | Documentation set established; agent instructions and documentation workflow in place (§10, §15) |
| Version control | Not initialized |
| Designs (Figma) | Not started |
| Technology stack | Not decided |
| Code | None |
| Hosting, domain, CI/CD | Not decided / not set up |
| Content and media | None in the repository |

No features are implemented. Every task in the phase documents is planned work.

## 5. Guiding Principles

1. **Persian-first.** Persian (RTL) is the default language; English (LTR) is secondary (scope: DEC-002).
2. **Built for Iran.** Host where users in Iran can reliably reach the site, avoid runtime dependencies on foreign-hosted resources, and test from Iranian networks without a VPN. See [iran-constraints.md](project/iran-constraints.md).
3. **Design first.** Pages are designed and approved in Figma before implementation; Cursor is used to implement from the Figma designs.
4. **Decide when necessary.** Undecided items stay open until they block work, then get recorded in `decisions.md`.
5. **MVP discipline.** Post-MVP work does not enter Phase 1 without an explicit decision.
6. **Quality gates.** Every change is validated in CI before merging; approved changes are deployed consistently (overview §2.2.1–2.2.2).
7. **Keep later phases possible.** Phase 1 choices should not block Phases 2–4, without building for them prematurely.

## 6. Roadmap

| Phase | Name | Status | Objective | Specification |
|---|---|---|---|---|
| 1 | MVP | Planning (S1.1) | Content and marketing website, launched in Iran | [phase-1-mvp.md](phases/phase-1-mvp.md) |
| 2 | آلبوم (Album) | Not scheduled | PWA album of the center's LEGO sets and their availability, integrated into the website | [phase-2-album.md](phases/phase-2-album.md) |
| 3 | Booking | Not scheduled | Reservations for events, workshops, and set construction | [phase-3-booking.md](phases/phase-3-booking.md) |
| 4 | Payment | Not scheduled | Secure payments for bookings and sales | [phase-4-payment.md](phases/phase-4-payment.md) |

Phases are numbered in their intended order. Phase 2's timeline is not determined.

### 6.1 Phase 1 — MVP

- **Objective:** Launch a Persian-first, bilingual, responsive content and marketing website that helps visitors discover the center (overview §2.1).
- **Scope:** 13 pages (PAGE-001–004, PAGE-006–014) plus the MVP requirements in overview §2.2: responsive design, FAQ, bilingual fa/en, location and map, basic SEO & GEO, simple navigation, social links, performance, analytics, browser compatibility, CI/CD, automated testing. No booking, payment, or user accounts.
- **Stages:** S1.1 Foundation & Requirements Finalization → S1.2 UX & Visual Design (Figma) → S1.3 Technical Foundation (parallel with S1.2) → S1.4 Design System & Site Shell → S1.5 Page Implementation → S1.6 Integrations, SEO & Analytics (parallel with S1.5) → S1.7 Quality Assurance & Hardening → S1.8 Launch in Iran.
- **Expected outcome:** A production website hosted for, and verified from inside, Iran; an automated validation and deployment pipeline; handover documentation.
- **Dependencies:** Content and media from the center; resolution of the Phase 1 decisions.

### 6.2 Phase 2 — آلبوم (Album)

- **Objective:** A PWA serving as a digital album of the center's LEGO sets, showing specifications (categories, age groups, number of elements) and availability (available to build or being built), with a prediction of when a set becomes free (PAGE-016).
- **Scope:** Developed as a separate, independent project. This repository covers its integration into a page of the website (PAGE-016). Stack, architecture, and timeline are undetermined.
- **Expected outcome:** Visitors can browse the center's sets and see their availability from the website.
- **Dependencies:** Phase 1 live; progress of the album project; DEC-027 (integration), DEC-028 (shared set data).

### 6.3 Phase 3 — Booking

- **Objective:** A booking system for events, workshops, and set construction (رزرو برای ساخت): reserve spots at events and workshops, view available workshop capacity, book building appointments (overview §1.3).
- **Expected outcome:** Visitors can make reservations through the website; workshop capacity is shown from live data.
- **Dependencies:** Phase 1 live; server-side architecture decisions (backend, database, user identification — all undecided); set data (DEC-028); payment handling before Phase 4 (DEC-029). PAGE-IDs to be added to `pages.md`.

### 6.4 Phase 4 — Payment

- **Objective:** A secure payment system for bookings (including workshops and set construction) and for purchases and sales through the platform.
- **Expected outcome:** Users can pay online through an Iranian payment gateway; staff can reconcile payments.
- **Dependencies:** Phase 3 (booking payments); merchant prerequisites with long lead times (for example eNamad and a gateway contract); Iran-hosted backend; DEC-030 (gateway), DEC-031 (sales scope).

## 7. Cross-Phase Dependencies

| Item | Phases | Note |
|---|---|---|
| Technology stack and hosting (DEC-016, DEC-018) | 1 → 3, 4 | Phases 3–4 need server-side logic and data storage. Evaluate in Phase 1 whether the choice can be extended or cleanly paired with a separate backend; do not build it in Phase 1 |
| LEGO set data (DEC-028) | 1, 2, 3 | PAGE-003 introduces sets (Phase 1), the album lists them (Phase 2), set-construction booking reserves them (Phase 3) |
| Workshop capacity (DEC-004) | 1 → 3 | Static in Phase 1 (if shown); live in Phase 3 |
| Purchases (DEC-003, DEC-031) | 1 → 4 | PAGE-013/014 without online payment in Phase 1; online sales in Phase 4 |
| Domain registrant and published business details (DEC-019) | 1 → 4 | eNamad and payment gateways check these; verify requirements before registering the domain |
| Iran-hosted server | 1 → 4 | Iranian payment gateways commonly require requests from Iranian IPs (verify) |
| Post-MVP PAGE-IDs | 2–4 | To be added to `pages.md` when each phase is detailed |

## 8. Shared Requirements (All Phases)

These Phase 1 requirements apply to later phases unless revised: Persian RTL default with English LTR; responsive on desktop, tablet, and mobile; accessibility; browser compatibility; performance; SEO; analytics; automated tests running in CI before deployment. Targets are proposed in [phase-1-mvp.md §7](phases/phase-1-mvp.md) and confirmed through DEC-024. How testing is done across all phases is proposed in [testing-strategy.md](testing/testing-strategy.md).

## 9. Iran Constraints (Summary)

Full details: [iran-constraints.md](project/iran-constraints.md).

- Many foreign platforms are filtered, and international connectivity has been severely restricted at times; domestically hosted services generally stayed reachable.
- Sanctions limit access to many foreign services and to international payment methods.
- Fonts, scripts, maps, analytics, videos, and captchas must work without foreign-hosted resources.
- Local conventions: Persian digits, Solar Hijri (Jalali) calendar, Asia/Tehran time zone, Rial/Toman.
- Legal and merchant processes (for example Samandehi, eNamad, gateway contracts) have their own prerequisites and lead times.
- Testing must happen on Iranian networks without a VPN.

## 10. Technical Architecture and Repository Structure

**Architecture:** Not decided. Decisions are made in Phase 1: stack and content management in T1.3.1.1 (DEC-016, DEC-017, DEC-025); hosting and deployment in T1.3.5.1 (DEC-018, DEC-020). Constraints any option must satisfy are listed in T1.3.1.1.

**Current repository structure:**

| Path | Content |
|---|---|
| `docs/development-plan.md` | This roadmap |
| `docs/phases/` | Phase specifications |
| `docs/project/` | Requirements, decision register, Iran constraints |
| `docs/testing/` | Testing strategy |
| `AGENTS.md` | Project-wide instructions for AI agents |
| `.cursor/rules/documentation.mdc` | Cursor rule: keep documentation synchronized with changes; when to delegate |
| `.cursor/agents/documentation.md` | Cursor subagent that performs documentation updates and audits |

The application structure is defined in T1.3.2.1 and documented here once decided.

## 11. Assumptions

| ID | Assumption | Status |
|---|---|---|
| A-1 | Most visitors access the site from inside Iran, largely on mobile devices | To verify with analytics after launch |
| A-2 | The center provides all text, photos, videos, prices, and schedules | To confirm in DEC-014 |
| A-3 | After launch, prices, events, and courses change more often than other content | To confirm in DEC-014 |
| A-4 | The MVP stores no personal data, except form submissions if DEC-009 selects a form | Follows from Phase 1 scope |
| A-5 | Phase 2, being an independent project, may follow its own timeline | To confirm in DEC-027 |
| A-6 | Phase 1 is mostly pre-rendered pages with little client-side logic, so test risk concentrates in content, layout, localization, integrations, and delivery ([testing-strategy.md](testing/testing-strategy.md) §1.3) | To verify with DEC-016 |

## 12. Key Risks

| Risk | Impact | Mitigation | Related |
|---|---|---|---|
| Filtering or international connectivity disruption | Site unreachable or broken for users in Iran | Host in Iran; self-host all assets; test without VPN | DEC-018 |
| No one available to test on Iranian networks and real devices without VPN | Iran-specific failures found only after launch | Decide testing access early; automated foreign-request checks in CI | DEC-034; [testing-strategy §12](testing/testing-strategy.md#12-risks-and-mitigations) |
| Sanctions affecting tools (Figma, GitHub, Cursor, package registries, Google services) | Workflow interruption | Local backups, registry mirrors, alternatives identified in advance | iran-constraints §2, §8 |
| Content and media not ready | Launch delay | Content inventory and owners in S1.1 | T1.1.4.1, DEC-014 |
| Open decisions block design | Design delay | Resolve in S1.1; track in register | T1.1.2.1 |
| Price volatility from inflation | Outdated prices on the site | Easy update path; agreed price format | DEC-014, DEC-015, DEC-017 |
| Use of the LEGO trademark in name, logo, or domain | Forced rebrand or domain loss | Review before brand and domain decisions | DEC-012, DEC-019 |
| Publishing children's images | Privacy and reputational harm | Consent policy before collecting media | DEC-013 |
| Bilingual effort underestimated | Doubles content, design, and QA work | Define English scope early | DEC-002 |
| Unknown album integration | Rework in Phase 2 | Define the integration contract when Phase 2 starts | DEC-027 |
| Post-MVP scope entering Phase 1 | MVP delay | MVP discipline; explicit decision required | §5 |

## 13. Definition of Done

| Level | Done when |
|---|---|
| Subtask | Its checklist item is satisfied |
| Task | Acceptance criteria met; code reviewed (if code); CI passing; affected documents updated; related decisions recorded |
| Feature | All tasks done; works in Persian (and English per DEC-002) at all breakpoints; automated tests and accessibility checks pass; deployed to staging and checked from an Iranian network |
| Stage | All features done, or explicitly deferred through a recorded decision; phase document updated |
| Phase | The phase's completion criteria are met and signed off by stakeholders; launches verified in production from inside Iran |

## 14. Unscheduled Items

| PAGE-ID | Page | Source |
|---|---|---|
| PAGE-005 | بازی سازی با سوپرماریو | `pages.md`: Phase TBD (post-MVP planned feature) |
| PAGE-015 | قطعه (bricks with part codes) | `pages.md`: Phase TBD (post-MVP planned feature) |

Scheduling is tracked in DEC-032.

## 15. Maintaining the Documentation

- Requirement changes → `project-overview.md` / `pages.md`. Decisions → `decisions.md`, then every affected document. Progress → checklists in phase documents.
- Keep IDs stable and link instead of copying content.
- Update the **Last updated** line of every document you change.
- AI agents follow this workflow through `.cursor/rules/documentation.mdc` and delegate multi-document updates to the `documentation` subagent.
