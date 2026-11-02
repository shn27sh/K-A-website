# Decision Register

> **Status:** Living document · **Last updated:** 2026-10-29

Every pending or decided project decision has a DEC-ID. Documents reference decisions by ID instead of repeating them.

**How to use:** add new items to the table as *Pending*. When decided, set the status to *Decided*, add a record under "Decision Records", and update every affected document.

## Register

| ID | Decision needed | Context / source | Needed by | Status |
|---|---|---|---|---|
| DEC-001 | Placement of PAGE-014: one page reached from PAGE-004 and PAGE-013, or separate pages? | pages.md listed PAGE-014 under both | T1.1.3.1 | Decided |
| DEC-002 | Scope and audience of the English (LTR) version: full parity or a subset; URL structure | overview §2.2 (bilingual); Persian-first | T1.1.3.2 | Pending |
| DEC-003 | How visitors buy from PAGE-013/014 without online payment | Sales in MVP; payment in Phase 4 | T1.2.2.1 | Decided |
| DEC-004 | Workshop capacity on PAGE-010 in the MVP: static values or omitted | PAGE-010 lists capacity; live capacity is Phase 3 | T1.2.2.1 | Decided |
| DEC-005 | Events, competitions, achievements, children's projects: sections in existing pages or new PAGE-IDs; how events are updated | overview §1.2, §1.5; PAGE-001 "رویداد ها" | T1.1.3.1 | Decided |
| DEC-006 | Placement of trust content: safety, instructors, educational benefits, policies; what "policies" contain | overview §1.4. User deferred on 2026-10-29 ("TBD") | T1.1.3.1 | Pending |
| DEC-007 | Purpose and content of PAGE-009 کارن و کیانا | pages.md: "صفحه ی اختصاصی" only | T1.1.3.1 | Decided |
| DEC-008 | Meaning and scope of "GEO" | overview §2.2 "Basic SEO & GEO" | T1.6.4.2 | Pending |
| DEC-009 | Request and contact mechanism: online form or contact channels; where submissions go | PAGE-011 "نحوه ی درخواست جلسه"; overview §1.6 | T1.2.2.1 | Decided |
| DEC-010 | Which social and messaging channels to display | Filtering policy confirmed 2026-10-29: links to filtered platforms are allowed; do not embed them; visitors use their own VPN. The channel list is still open. iran-constraints §7 | T1.2.2.2 | Pending |
| DEC-011 | Video hosting for PAGE-007 and PAGE-010 | Direction on 2026-10-29, not decided: Aparat, and possibly a storage server. YouTube is filtered | T1.1.4.3 | Pending |
| DEC-012 | Official brand name (fa/en), logo, brand assets; review of LEGO trademark use in name, logo, domain (including "خانه لگو") | pages.md PAGE-011 mentions "خانه لگو" | T1.2.1.1 | Pending |
| DEC-013 | Consent policy for publishing photos, videos, and projects of children | PAGE-006, PAGE-007 | T1.1.4.3 | Decided |
| DEC-014 | Content ownership and update workflow: who provides fa/en content; who updates prices, events, courses after launch, and how often | A-2, A-3. Price display format is DEC-015 | T1.1.4.1 | Pending |
| DEC-015 | Price display: Toman or Rial, formatting, update approach | PAGE-002, PAGE-010; inflation; redenomination. Who updates prices, and how often, stays in DEC-014 | T1.2.2.2 | Decided |
| DEC-016 | Technology stack (framework, styling, i18n, build) | Deferred until needed | T1.3.1.1 | Pending |
| DEC-017 | Content management approach (files in the repository, headless CMS, or admin panel) | Depends on DEC-014 | T1.3.1.1 | Pending |
| DEC-018 | Hosting provider and location for staging and production | iran-constraints §1, §3 | T1.3.5.1 | Pending |
| DEC-019 | Domain name, TLD, and registrant (eNamad implications) | iran-constraints §4; Phase 4 | T1.3.5.3 | Pending |
| DEC-020 | Git hosting, CI/CD platform, and deployment path to the host | overview §2.2.1; iran-constraints §8; GitHub and GitHub Actions in use since 2026-10-26 (A-7) | T1.3.5.1 | Pending |
| DEC-021 | Analytics tool, tracked events, privacy approach | overview §2.2; iran-constraints §7 | T1.6.3.1 | Pending |
| DEC-022 | Map provider and navigation app links | overview §2.2; iran-constraints §7. Approves Google Maps alongside Neshan and Balad | T1.2.2.2 | Decided |
| DEC-023 | Typefaces and web licenses (Persian and Latin) | iran-constraints §6. Change the fonts by updating this record | T1.2.1.2 | Decided |
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

Confirmed by the user on 2026-10-29. DEC-006, DEC-010, and DEC-011 were not confirmed and stay Pending (see the register).

### DEC-001 — One PAGE-014, linked from other pages
- **Status:** Decided (2026-10-29)
- **Decision:** PAGE-014 is a single page for selling LEGO Boost sets. Other pages, including PAGE-004, link to it so visitors can see that the sets are also for sale. It is not a second page.
- **Rationale:** User, 2026-10-29: "PAGE-014 is one page for selling LEGO Boosts, but we will also use that page links in the other pages like PAGE-004 to showcase workshops visitors LEGO Boosts is also available to sell."
- **Alternatives considered:** Separate pages under PAGE-004 and PAGE-013 (rejected).
- **Documents updated:** pages.md, phase-1-mvp.md, and the documents that cited the open question.

### DEC-003 — Offline purchase instructions
- **Status:** Decided (2026-10-29)
- **Decision:** In the MVP, buying from PAGE-013 and PAGE-014 is entirely offline. Those pages explain how: by phone, or by visiting the center in person. There is no online payment or checkout.
- **Rationale:** User, 2026-10-29: payment for those two pages in the MVP "is completely offline", with instructions in the page content such as calling or an in-person visit.
- **Alternatives considered:** Online checkout (Phase 4, DEC-031).
- **Documents updated:** phase-1-mvp.md, development-plan.md, pages.md.

### DEC-004 — Static workshop capacity
- **Status:** Decided (2026-10-29)
- **Decision:** PAGE-010 shows a fixed capacity for each workshop. The number is written into the page content by hand and does not update automatically. Live capacity is Phase 3.
- **Rationale:** User, 2026-10-29: "They are static values... The value is entered manually and does not update automatically."
- **Alternatives considered:** Omitting capacity in the MVP; live capacity (Phase 3).
- **Documents updated:** phase-1-mvp.md, phase-3-booking.md, development-plan.md, pages.md.

### DEC-005 — Sections on existing pages; events are not live
- **Status:** Decided (2026-10-29)
- **Decision:** Events, competitions, achievements, and children's projects are sections of existing pages. They do not get new pages or PAGE-IDs. Events are not live in the MVP. Which existing page holds each section, where pages.md does not already name it, is settled in the sitemap (T1.1.3.1).
- **Rationale:** User, 2026-10-29: those sections "will place in that existing page without any separate page and PAGE-IDs. The events are not live in MVP."
- **Alternatives considered:** New PAGE-IDs for each topic.
- **Documents updated:** pages.md, phase-1-mvp.md, phase-3-booking.md.

### DEC-007 — کارن و کیانا
- **Status:** Decided (2026-10-29)
- **Decision:** کارن and کیانا are two AI characters who introduce the center. PAGE-009 is their own page, and its content is commercial.
- **Rationale:** User, 2026-10-29: they "are two AI characters who introduce the center and basically are commercial contents which we have a separate page for them."
- **Alternatives considered:** Folding them into another page (rejected; the page already existed).
- **Documents updated:** pages.md, phase-1-mvp.md, test-plan.md.

### DEC-009 — Contact channels, no form
- **Status:** Decided (2026-10-29)
- **Decision:** PAGE-011 does not use an online form. Visitors request a meeting through contact channels. Which channels appear is decided in that page's content. Nothing is submitted to a server.
- **Rationale:** User, 2026-10-29: "In that page context we will determine but its basically through contact channels. Not any online form submission."
- **Alternatives considered:** An online form (rejected). T1.6.2.1 is therefore *Not needed*.
- **Documents updated:** phase-1-mvp.md, development-plan.md (A-4), pages.md, test-plan.md.

### DEC-013 — Permission before publishing children's media
- **Status:** Decided (2026-10-29)
- **Decision:** In the MVP, photos, videos, and children's project work may be published publicly only after the necessary permissions have been obtained.
- **Rationale:** User, 2026-10-29: they "may be published publicly only after the necessary permissions have been obtained."
- **Alternatives considered:** Publishing without a permission step (rejected).
- **Remaining detail:** Who grants permission, and how the permission is recorded, was not specified. That is settled while collecting media (T1.1.4.3), not by inventing a process here.
- **Documents updated:** iran-constraints.md, phase-1-mvp.md, development-plan.md, README.md.

### DEC-015 — Prices in Toman
- **Status:** Decided (2026-10-29)
- **Decision:** Prices are shown in Toman. Two accepted forms, as given: `5میلیون تومان` and `5,000,000 تومان`. Who updates prices, and how often, remains DEC-014.
- **Rationale:** User, 2026-10-29: "We will use Toman in this format for instance: 5میلیون تومان or 5,000,000 تومان."
- **Alternatives considered:** Rial as the displayed unit.
- **Documents updated:** phase-1-mvp.md, iran-constraints.md.

### DEC-022 — Google Maps, Neshan, and Balad
- **Status:** Decided (2026-10-29)
- **Decision:** The location block uses Google Maps, Neshan (نشان), and Balad (بلد), including links that open those apps. This approves Google Maps as a foreign-hosted map (an exception to the usual ban on foreign runtime resources). Neshan and Balad are included so the location can still be opened in Iran without a VPN. A static fallback (image and address) remains required when a map does not load. The map must not block the rest of the page.
- **Rationale:** User, 2026-10-29: "We will use Google Maps also Neshan and Balad." Google Maps often does not load in Iran without a VPN and needs international billing (iran-constraints §7); the other two providers cover that gap.
- **Alternatives considered:** Neshan and Balad only; Map.ir; OpenStreetMap.
- **Documents updated:** iran-constraints.md, phase-1-mvp.md.

### DEC-023 — Vazirmatn and Inter
- **Status:** Decided (2026-10-29)
- **Decision:** Persian text uses Vazirmatn. Latin text uses Inter. Both are self-hosted; they are not loaded from a font service. If the choice changes, update this record. Vazirmatn and Inter are published under the SIL Open Font License, which allows self-hosting; include those license files when the fonts are added (T1.2.1.2).
- **Rationale:** User, 2026-10-29: "Persian: Vazirmatn and Latin: Inter. If they changed later, we will update that."
- **Alternatives considered:** A licensed commercial Persian font.
- **Documents updated:** iran-constraints.md, phase-1-mvp.md.
