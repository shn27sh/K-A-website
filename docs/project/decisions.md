# Decision Register

> **Status:** Living document · **Last updated:** 2026-10-26

Every pending or decided project decision has a DEC-ID. Documents reference decisions by ID instead of repeating them.

**How to use:** add new items to the table as *Pending*. When decided, set the status to *Decided*, add a record under "Decision Records", and update every affected document.

## Register

| ID | Decision needed | Context / source | Needed by | Status |
|---|---|---|---|---|
| DEC-001 | Placement of PAGE-014: one page reached from PAGE-004 and PAGE-013, or separate pages? | pages.md lists PAGE-014 under both | T1.1.3.1 | Pending |
| DEC-002 | Scope and audience of the English (LTR) version: full parity or a subset; URL structure | overview §2.2 (bilingual); Persian-first | T1.1.3.2 | Pending |
| DEC-003 | How visitors buy from PAGE-013/014 without online payment | Sales in MVP; payment in Phase 4 | T1.2.2.1 | Pending |
| DEC-004 | Workshop capacity on PAGE-010 in the MVP: static values or omitted | PAGE-010 lists capacity; live capacity is Phase 3 | T1.2.2.1 | Pending |
| DEC-005 | Events, competitions, achievements, children's projects: sections in existing pages or new PAGE-IDs; how events are updated | overview §1.2, §1.5; PAGE-001 "رویداد ها" | T1.1.3.1 | Pending |
| DEC-006 | Placement of trust content: safety, instructors, educational benefits, policies; what "policies" contain | overview §1.4 | T1.1.3.1 | Pending |
| DEC-007 | Purpose and content of PAGE-009 کارن و کیانا | pages.md: "صفحه ی اختصاصی" only | T1.1.3.1 | Pending |
| DEC-008 | Meaning and scope of "GEO" | overview §2.2 "Basic SEO & GEO" | T1.6.4.2 | Pending |
| DEC-009 | Request and contact mechanism: online form or contact channels; where submissions go | PAGE-011 "نحوه ی درخواست جلسه"; overview §1.6 | T1.2.2.1 | Pending |
| DEC-010 | Social media and messaging channels to display | overview §2.2; filtering (iran-constraints §7) | T1.2.2.2 | Pending |
| DEC-011 | Video hosting for PAGE-007 and PAGE-010 | YouTube filtered in Iran | T1.1.4.3 | Pending |
| DEC-012 | Official brand name (fa/en), logo, brand assets; review of LEGO trademark use in name, logo, domain (including "خانه لگو") | pages.md PAGE-011 mentions "خانه لگو" | T1.2.1.1 | Pending |
| DEC-013 | Consent policy for publishing photos, videos, and projects of children | PAGE-006, PAGE-007 | T1.1.4.3 | Pending |
| DEC-014 | Content ownership and update workflow: who provides fa/en content; who updates prices, events, courses after launch, and how often | A-2, A-3 | T1.1.4.1 | Pending |
| DEC-015 | Price display: Toman or Rial, formatting, update approach | PAGE-002, PAGE-010; inflation; redenomination | T1.2.2.2 | Pending |
| DEC-016 | Technology stack (framework, styling, i18n, build) | Deferred until needed | T1.3.1.1 | Pending |
| DEC-017 | Content management approach (files in the repository, headless CMS, or admin panel) | Depends on DEC-014 | T1.3.1.1 | Pending |
| DEC-018 | Hosting provider and location for staging and production | iran-constraints §1, §3 | T1.3.5.1 | Pending |
| DEC-019 | Domain name, TLD, and registrant (eNamad implications) | iran-constraints §4; Phase 4 | T1.3.5.3 | Pending |
| DEC-020 | Git hosting, CI/CD platform, and deployment path to the host | overview §2.2.1; iran-constraints §8 | T1.3.5.1 | Pending |
| DEC-021 | Analytics tool, tracked events, privacy approach | overview §2.2; iran-constraints §7 | T1.6.3.1 | Pending |
| DEC-022 | Map provider and navigation app links | overview §2.2; iran-constraints §7 | T1.2.2.2 | Pending |
| DEC-023 | Typefaces and web licenses (Persian and Latin) | iran-constraints §6 | T1.2.1.2 | Pending |
| DEC-024 | Quality targets: browser/device support, performance budgets, accessibility level | Proposed values in phase-1-mvp §7; proposed additions and page weight budgets in testing-strategy §4.6, §10.1 | T1.2.1.2 | Pending |
| DEC-025 | Testing tools (unit/integration, E2E, accessibility) | overview §2.2.2; tied to DEC-016; proposed tool set in testing-strategy §6 | T1.3.1.1 | Pending |
| DEC-026 | Figma-to-Cursor workflow and tools (plan, access from Iran) | Design-first workflow | T1.2.3.1 | Pending |
| DEC-027 | Phase 2 timeline and integration method into PAGE-016 | Album is an independent project | T2.1.1.2 | Pending |
| DEC-028 | Single source of LEGO set data across PAGE-003, the album, and set-construction booking | Phases 1–3 | T2.1.1.3 | Pending |
| DEC-029 | Payment handling for bookings before Phase 4 | Phase 3 precedes Phase 4 | T3.1.1.1 | Pending |
| DEC-030 | Payment gateway type and provider | Phase 4; iran-constraints §10 | T4.1.1.2 | Pending |
| DEC-031 | Online sales scope and relation to PAGE-013/014/015 | Phase 4 | T4.2.1.1 | Pending |
| DEC-032 | Scheduling of PAGE-005 and PAGE-015 | pages.md: Phase TBD | T1.8.3.3 | Pending |
| DEC-033 | Coverage and test suite health targets | testing-strategy §10.2–10.3 | T1.3.4.1 | Pending |
| DEC-034 | Testing access inside Iran: who tests on Iranian mobile and fixed networks without a VPN, which physical devices are available, and whether a test runner or server inside Iran is provided | testing-strategy §4.10, §7.1; T1.7.2.2; iran-constraints §9 | T1.3.5.2 | Pending |

## Decision Records

None yet. Template:

### DEC-### — Title
- **Status:** Decided (YYYY-MM-DD)
- **Decision:**
- **Rationale:**
- **Alternatives considered:**
- **Documents updated:**
