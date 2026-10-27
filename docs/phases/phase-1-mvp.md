# Phase 1 — MVP

> **Status:** Planning · **Current stage:** S1.1 · **Last updated:** 2026-10-27
> Roadmap: [development-plan.md](../development-plan.md) · Requirements: [project-overview.md](../project/project-overview.md), [pages.md](../project/pages.md) · Decisions: [decisions.md](../project/decisions.md) · Constraints: [iran-constraints.md](../project/iran-constraints.md) · Testing: [testing-strategy.md](../testing/testing-strategy.md), [test-plan.md](../testing/test-plan.md)

## 1. Purpose

Deliver the MVP: a Persian-first (RTL), bilingual, responsive content and marketing website that helps visitors discover the center (overview §2.1), launched in Iran.

## 2. Objectives

From overview §1: present the center (§1.1); display activities and programs (§1.2); build trust with parents (§1.4); promote the community (§1.5); give schools, businesses, and organizations a way to request group activities (§1.6). Booking (§1.3) belongs to Phase 3.

## 3. Scope

### 3.1 In Scope — Pages

| PAGE-ID | Page | Notes |
|---|---|---|
| PAGE-001 | صفحه ی اصلی | |
| PAGE-002 | معرفی خدمات | |
| PAGE-003 | ساخت لگو | Set data relates to Phase 2–3 (DEC-028) |
| PAGE-004 | کارگاه لگو بوست | Links to PAGE-014 (DEC-001) |
| PAGE-006 | گالری | Consent policy: DEC-013 |
| PAGE-007 | درباره ی ما | |
| PAGE-008 | تماس با ما | Map: DEC-022 |
| PAGE-009 | کارن و کیانا | Content undefined (DEC-007) |
| PAGE-010 | معرفی دوره های کارگاهی | Capacity: DEC-004 |
| PAGE-011 | همکاری | Request mechanism: DEC-009 |
| PAGE-012 | پرسش های متداول | |
| PAGE-013 | فروش | Purchase method without online payment: DEC-003 |
| PAGE-014 | ست لگو بوست | Listed under both PAGE-004 and PAGE-013 (DEC-001) |

### 3.2 In Scope — Cross-Cutting

All MVP requirements in overview §2.2 (see §4).

### 3.3 Out of Scope

- Booking and registration (Phase 3); live workshop capacity (Phase 3).
- Online payment and checkout (Phase 4).
- Album, PAGE-016 (Phase 2).
- PAGE-005 and PAGE-015 (unscheduled).
- User accounts (not required by any MVP requirement).

## 4. Confirmed Requirements

| Requirement | Source |
|---|---|
| Pages listed in §3.1 | pages.md (Phase 1-MVP) |
| Responsive; desktop, tablet, and mobile versions | overview §2.2 |
| FAQ | overview §2.2 |
| Bilingual: Persian (RTL, default) and English (LTR) | overview §2.2; conversation (Persian-first) |
| Location and map | overview §2.2 |
| Basic SEO & GEO | overview §2.2 (GEO meaning: DEC-008) |
| Simple navigation | overview §2.2 |
| Social media links | overview §2.2 |
| Good performance and fast loading | overview §2.2 |
| Analytics | overview §2.2 |
| Browser compatibility | overview §2.2 |
| CI/CD: every change tested before merging; approved changes deployed consistently | overview §2.2.1 |
| Unit/integration tests for critical functionality; E2E tests for core user journeys; basic responsive and accessibility checks; all tests run in CI before deployment | overview §2.2.2 |
| Pages designed in Figma first, then implemented with Cursor | conversation |
| Launched in Iran | conversation |

## 5. Constraints and Dependencies

- **Iran constraints** apply throughout, especially connectivity, third-party services, hosting, localization, and testing ([iran-constraints.md](../project/iran-constraints.md)).
- **No online payment** in this phase.
- **External inputs:** content and media from the center (DEC-014); brand assets (DEC-012); stakeholder decisions (§12).
- **Design gate:** a page is implemented (S1.5) only after its Figma design is signed off (T1.2.2.3).

## 6. Expected Outcomes

- All in-scope pages live in production in Persian, and in English per DEC-002.
- Site reachable and fast from Iranian mobile and fixed networks without a VPN.
- A CI pipeline validating every change; deployments to staging and approval-based deployments to production.
- Handover documentation: content updates, deployment, rollback.

## 7. Quality Targets (Proposed — Pending DEC-024)

| Area | Proposed target | Verified in |
|---|---|---|
| Performance | Core Web Vitals "good" on mobile: LCP ≤ 2.5 s, CLS ≤ 0.1, INP ≤ 200 ms; Lighthouse mobile performance ≥ 90 on key pages; measured from an Iranian network | T1.7.3.1 |
| Accessibility | WCAG 2.2 Level AA as the target; zero critical/serious automated violations; full keyboard operability | T1.7.1.3, T1.7.2.3 |
| Browsers | Latest two versions of Chrome, Edge, Firefox, Safari (macOS and iOS), Samsung Internet, Chrome for Android; older-version support decided from market and analytics data | T1.7.2.1 |
| Breakpoints | Mobile, tablet, desktop, as defined in Figma | T1.2.1.2 |
| SEO | Unique title and description per page and locale; valid hreflang, sitemap, robots, structured data | T1.6.4.1 |

## 8. Stages

| Stage | Objective | Depends on |
|---|---|---|
| S1.1 Foundation & Requirements Finalization | Version control, documentation, blocking decisions, information architecture, content production | — |
| S1.2 UX & Visual Design (Figma) | Design system and signed-off designs for all pages | S1.1 |
| S1.3 Technical Foundation | Stack, scaffolding, i18n/RTL, CI, staging, domain | S1.1 (decisions); parallel with S1.2 |
| S1.4 Design System & Site Shell | Tokens, components, header, footer, templates in code | S1.2 (foundations, components), S1.3 |
| S1.5 Page Implementation | All in-scope pages | S1.4; per-page design sign-off; content |
| S1.6 Integrations, SEO & Analytics | Map, request handling, analytics, SEO/GEO | S1.4; parallel with S1.5 |
| S1.7 Quality Assurance & Hardening | Complete test coverage; final verification | S1.5, S1.6 (testing is continuous) |
| S1.8 Launch in Iran | Production, go-live, monitoring, handover | S1.7 |

**Critical path:** S1.1 → S1.2 → S1.4 → S1.5 → S1.7 → S1.8.
**Start early (long lead):** content and media (F1.1.4), brand assets (DEC-012), domain (T1.3.5.3).

## 9. Features, Development Tasks, and Subtasks

### S1.1 — Foundation & Requirements Finalization

#### F1.1.1 — Version Control & Documentation Baseline

##### T1.1.1.1 — Initialize the Git repository
- **Purpose:** Track every change to documentation and later code from day one.
- **Outcome:** Repository under version control with the existing documentation committed.
- **Files:** `.gitignore`, `.gitattributes` (new); `docs/`.
- **Depends on:** — (remote hosting: DEC-020)
- **Acceptance criteria:** Initial commit contains `docs/`; line endings normalized to LF in the repository (Windows development environment); working tree clean.
- **Subtasks:**
  - [x] Initialize the repository and default branch
  - [ ] Add `.gitattributes` and `.gitignore`
  - [x] Commit `docs/`
  - [ ] Add the remote once DEC-020 is decided
- **Note:** A GitHub remote was added and the initial commit pushed on 2026-10-26 while DEC-020 is Pending (development-plan §11, A-7).

##### T1.1.1.2 — Establish the documentation structure
- **Purpose:** Separate the roadmap from phase specifications; track decisions and Iran constraints centrally.
- **Outcome:** This documentation set, cross-linked, plus agent instructions and a documentation workflow that keeps it synchronized.
- **Files:** `docs/development-plan.md`, `docs/phases/*.md`, `docs/project/decisions.md`, `docs/project/iran-constraints.md`, `AGENTS.md`, `.cursor/rules/documentation.mdc`, `.cursor/agents/documentation.md`.
- **Depends on:** —
- **Acceptance criteria:** All links resolve; terminology follows development-plan §3; every pending item has a DEC-ID.
- **Subtasks:**
  - [x] Create the documents
  - [x] Verify links and IDs
  - [x] Set up the documentation maintenance workflow (`AGENTS.md`, documentation rule, documentation subagent)

#### F1.1.2 — Requirements Clarification

##### T1.1.2.1 — Resolve requirement decisions that block architecture and design
- **Purpose:** Remove ambiguities before information architecture and design work.
- **Outcome:** Decisions recorded in `decisions.md`.
- **Depends on:** Stakeholder input.
- **Acceptance criteria:** DEC-001–DEC-007, DEC-009, DEC-010, and DEC-012–DEC-015 are each *Decided* (with date and rationale) or *Deferred* to a named later task.
- **Subtasks:**
  - [ ] Page structure: DEC-001, DEC-005, DEC-006, DEC-007
  - [ ] Language scope: DEC-002
  - [ ] MVP behavior: DEC-003, DEC-004, DEC-009
  - [ ] Channels and brand: DEC-010, DEC-012
  - [ ] Content policy: DEC-013, DEC-014, DEC-015

##### T1.1.2.2 — Align `pages.md` with decisions
- **Purpose:** Keep the page inventory accurate and unambiguous.
- **Outcome:** Updated `pages.md`.
- **Files:** `docs/project/pages.md` (and `project-overview.md` if requirements change).
- **Depends on:** T1.1.2.1
- **Acceptance criteria:** Each PAGE-ID is defined exactly once (other mentions are explicit cross-references); every MVP page has a content list; PAGE-009 is described; new pages use the next free ID (PAGE-017 onward) without renumbering.
- **Subtasks:**
  - [ ] Resolve PAGE-014 placement (DEC-001)
  - [ ] Add pages or sections from DEC-005 and DEC-006
  - [ ] Describe PAGE-009 (DEC-007)

#### F1.1.3 — Information Architecture

##### T1.1.3.1 — Define the sitemap and navigation
- **Purpose:** Give every page a place and a path from the home page.
- **Outcome:** Documented sitemap, primary navigation, footer navigation, and calls to action.
- **Files:** `docs/project/pages.md` (structure section).
- **Depends on:** T1.1.2.2
- **Acceptance criteria:** Every in-scope PAGE-ID has a position in the hierarchy and at least one navigation path from PAGE-001; primary navigation, mobile navigation pattern, and footer contents are defined.
- **Subtasks:**
  - [ ] Hierarchy, including the services group (PAGE-002 → PAGE-003, PAGE-004, PAGE-013/014) and PAGE-010
  - [ ] Primary and footer navigation
  - [ ] Main call to action per page

##### T1.1.3.2 — Define URL and language structure
- **Purpose:** Fix the bilingual structure before design and implementation.
- **Outcome:** URL scheme for Persian and English.
- **Depends on:** DEC-002
- **Acceptance criteria:** URL pattern for fa (default) and en defined; slug language decided; each Persian page mapped to its English counterpart or marked Persian-only; hreflang approach documented.
- **Subtasks:**
  - [ ] Locale URL pattern
  - [ ] Slug convention
  - [ ] fa ↔ en page mapping

#### F1.1.4 — Content Inventory and Production

##### T1.1.4.1 — Build the content inventory
- **Purpose:** Content is the core of a marketing MVP and the most likely launch blocker.
- **Outcome:** Per-page list of required content with owner and status.
- **Files:** Location to be decided (repository document or shared spreadsheet).
- **Depends on:** T1.1.3.1, DEC-014
- **Acceptance criteria:** Each in-scope PAGE-ID lists its text blocks, images, videos, and data (prices, schedules, FAQs, instructor profiles), each with an owner and a status.
- **Subtasks:**
  - [ ] Inventory per PAGE-ID
  - [ ] Assign owners and due dates

##### T1.1.4.2 — Write Persian copy and English translation
- **Outcome:** Approved copy for all pages.
- **Depends on:** T1.1.4.1, DEC-002
- **Acceptance criteria:** Persian copy approved by the center for every in-scope page; English copy approved per DEC-002; fa/en glossary of recurring terms (for example ساخت لگو, لگو بوست).
- **Subtasks:**
  - [ ] Persian copy per page
  - [ ] English translation per DEC-002
  - [ ] Glossary

##### T1.1.4.3 — Collect photos and videos
- **Outcome:** Media for the gallery, about, courses, and home pages.
- **Depends on:** DEC-013, DEC-011
- **Acceptance criteria:** Original-resolution media collected for PAGE-001, PAGE-006, PAGE-007, PAGE-010; consent recorded for every identifiable child; videos prepared for the chosen hosting.
- **Subtasks:**
  - [ ] Environment and facilities photos
  - [ ] Children's projects (with consent)
  - [ ] Workshop photos and videos
  - [ ] Opening photos and videos (PAGE-007)

### S1.2 — UX & Visual Design (Figma)

#### F1.2.1 — Design Foundations

##### T1.2.1.1 — Define the visual direction
- **Outcome:** Approved style direction for the website.
- **Depends on:** DEC-012
- **Acceptance criteria:** Style direction approved by stakeholders, suitable for both parents (primary audience) and children; logo and brand assets available in vector form.

##### T1.2.1.2 — Define design tokens
- **Outcome:** Figma variables and styles for typography, color, spacing, radius, grid, and breakpoints.
- **Depends on:** T1.2.1.1, DEC-023, DEC-024
- **Acceptance criteria:** Variables defined and used consistently; Persian and Latin text styles defined; mobile, tablet, and desktop breakpoints defined; text/background color pairs meet the contrast level in DEC-024; font web licenses confirmed and files available for self-hosting.
- **Subtasks:**
  - [ ] Typography (fa and Latin)
  - [ ] Color palette with contrast checks
  - [ ] Spacing, radius, grid, breakpoints

##### T1.2.1.3 — Build the component library
- **Outcome:** Reusable Figma components covering all MVP pages.
- **Depends on:** T1.2.1.2, T1.2.2.1
- **Acceptance criteria:** Every component used in page designs exists as a component with variants and states (default, hover, focus, disabled, error where applicable); RTL and LTR behavior defined; responsive behavior defined; component inventory documented.
- **Subtasks (expected; confirm against wireframes):**
  - [ ] Header and navigation (desktop and mobile), language switcher
  - [ ] Footer, social links
  - [ ] Buttons and links
  - [ ] Cards (activity, course, set)
  - [ ] FAQ accordion
  - [ ] Gallery grid and image viewer
  - [ ] Price display
  - [ ] Location and map block
  - [ ] Video embed
  - [ ] Form elements (if DEC-009 selects a form)

#### F1.2.2 — Page Designs

##### T1.2.2.1 — Create wireframes
- **Outcome:** Low-fidelity layouts for every in-scope page.
- **Depends on:** T1.1.3.1, T1.1.4.1, DEC-003, DEC-004, DEC-009
- **Acceptance criteria:** Mobile and desktop wireframes for each in-scope PAGE-ID include every section listed in `pages.md`; reviewed by stakeholders.

##### T1.2.2.2 — Create high-fidelity designs
- **Outcome:** Final designs for every in-scope page.
- **Depends on:** T1.2.1.3, T1.2.2.1, T1.1.4.2, DEC-010, DEC-015, DEC-022
- **Acceptance criteria:** Each PAGE-ID designed at mobile, tablet, and desktop in Persian (RTL); English (LTR) variants per DEC-002; built only from library components and variables; uses real Persian copy, not placeholder text.

##### T1.2.2.3 — Review and sign off designs
- **Outcome:** Approved designs ready for implementation.
- **Depends on:** T1.2.2.2
- **Acceptance criteria:** Each PAGE-ID has a recorded sign-off; implementation of a page starts only after its sign-off.

#### F1.2.3 — Design-to-Code Handoff

##### T1.2.3.1 — Prepare Figma files for implementation with Cursor
- **Outcome:** Figma files that Cursor can translate accurately.
- **Depends on:** T1.2.1.3, DEC-026
- **Acceptance criteria:** Consistent layer naming; auto layout; variables bound (no hard-coded values); components with properties; the chosen Figma-to-Cursor method tested end to end on one page under the team's network conditions.

##### T1.2.3.2 — Export assets and back up designs
- **Outcome:** Implementation-ready assets; protection against losing access to Figma.
- **Depends on:** T1.2.2.3
- **Acceptance criteria:** Icons exported as SVG; images available at source resolution; Figma files backed up locally (`.fig`) on a regular schedule.

### S1.3 — Technical Foundation

#### F1.3.1 — Technology Stack Decision

##### T1.3.1.1 — Evaluate and decide the stack
- **Purpose:** Choose a stack that satisfies MVP requirements and Iran constraints without blocking later phases.
- **Outcome:** DEC-016 (stack), DEC-017 (content management), DEC-025 (testing tools) decided.
- **Depends on:** DEC-002, DEC-014, [iran-constraints.md](../project/iran-constraints.md)
- **Acceptance criteria:** Decision recorded with rationale, alternatives considered, and how each criterion below is met.
- **Subtasks (evaluation criteria):**
  - [ ] Pre-rendered HTML (static generation or server rendering) for SEO and fast first load on mobile networks
  - [ ] First-class i18n with per-locale RTL/LTR
  - [ ] All assets self-hostable; no required runtime calls to foreign services
  - [ ] Builds and deploys on the chosen hosting (DEC-018) under Iranian network conditions, including package registry access
  - [ ] Supports unit/integration, E2E, and accessibility testing in CI
  - [ ] Content updates feasible for the people defined in DEC-014
  - [ ] Phase 3–4 server-side needs can be added or cleanly paired (evaluated, not built)
  - [ ] Fits the Figma-to-Cursor workflow and team skills

#### F1.3.2 — Project Scaffolding & Code Quality

##### T1.3.2.1 — Scaffold the application and define the repository structure
- **Outcome:** A running application skeleton with a documented structure.
- **Files:** Defined by the stack; structure documented in development-plan §10.
- **Depends on:** T1.3.1.1
- **Acceptance criteria:** The app runs locally and renders a placeholder page in Persian (RTL); repository structure documented; `README.md` has setup instructions.

##### T1.3.2.2 — Set up code quality tooling
- **Outcome:** Consistent, automatically checked code.
- **Depends on:** T1.3.2.1
- **Acceptance criteria:** Lint, format, and type-check commands (as applicable) run locally and pass; editor configuration committed; lockfile committed; package registry/mirror configuration documented if needed for Iranian networks.

#### F1.3.3 — Internationalization & RTL Foundation

##### T1.3.3.1 — Implement locale routing and text direction
- **Outcome:** Persian default (RTL) and English (LTR) working across the app.
- **Depends on:** T1.1.3.2, T1.3.2.1
- **Acceptance criteria:** Persian pages render with `lang="fa" dir="rtl"`, English with `lang="en" dir="ltr"`; the language switcher opens the equivalent page; layout uses logical (start/end) properties so it mirrors without per-direction overrides; an automated test covers both directions.

##### T1.3.3.2 — Implement locale utilities and self-hosted fonts
- **Outcome:** Correct Persian formatting and typography everywhere.
- **Depends on:** T1.3.3.1, DEC-015, DEC-023
- **Acceptance criteria:** Unit-tested utilities for Persian digits, Solar Hijri dates, price formatting per DEC-015, and Persian text normalization (ي→ی, ك→ک, ZWNJ preserved); fonts self-hosted as WOFF2 with a defined `font-display` strategy; no requests to external font services.

#### F1.3.4 — Continuous Integration

##### T1.3.4.1 — Set up the CI validation pipeline
- **Outcome:** Every change validated before merging (overview §2.2.1).
- **Depends on:** T1.3.2.2, DEC-020
- **Acceptance criteria:** On every pull request, CI runs lint, type-check, unit/integration tests, and a production build; merging is blocked when any check fails; extended with E2E and accessibility checks in F1.7.1.
- **Current state (2026-10-27):** Only the documentation link check runs (`.github/workflows/ci.yml`). Lint, type-check, tests, build, and branch protection are not set up.
- **Subtasks:**
  - [ ] Pipeline configuration
  - [ ] Branch protection on the main branch
  - [ ] Dependency caching

#### F1.3.5 — Environments, Domain & Deployment

##### T1.3.5.1 — Decide hosting and the deployment path
- **Outcome:** DEC-018 and DEC-020 decided.
- **Depends on:** T1.3.1.1, [iran-constraints.md §3, §8](../project/iran-constraints.md)
- **Acceptance criteria:** Decision covers provider and data center location; reachability from Iranian networks without VPN; reachability from abroad (relevant to DEC-002); how CI deploys to the host; cost and a payment method available to the center; backups; SSL.

##### T1.3.5.2 — Set up staging with automated deployment
- **Outcome:** A shared environment that stakeholders can review from inside Iran.
- **Depends on:** T1.3.5.1, T1.3.4.1
- **Acceptance criteria:** Each merge to the main branch deploys to staging automatically; staging is reachable without VPN from at least one Iranian mobile operator and one fixed-line ISP; staging is excluded from search engines.

##### T1.3.5.3 — Register the domain
- **Outcome:** The production domain is secured.
- **Depends on:** DEC-012, DEC-019
- **Acceptance criteria:** Domain registered with the registrant agreed in DEC-019; DNS management access documented; renewal date recorded.

### S1.4 — Design System & Site Shell Implementation

#### F1.4.1 — Design Tokens and Base Styles

##### T1.4.1.1 — Implement tokens from Figma variables
- **Outcome:** Code-level design tokens matching Figma.
- **Depends on:** T1.2.1.2, T1.3.3.1
- **Acceptance criteria:** Color, typography, spacing, radius, and breakpoint tokens map 1:1 to Figma variables by name; base typography correct in Persian and English; components use tokens rather than hard-coded values.

#### F1.4.2 — Shared UI Components

##### T1.4.2.1 — Implement the component library
- **Outcome:** Coded components matching the Figma inventory.
- **Depends on:** T1.2.1.3, T1.4.1.1
- **Acceptance criteria:** Each inventory component implemented with its variants and states; correct in RTL and LTR; keyboard accessible with visible focus; interactive components (menu, accordion, image viewer) covered by tests.

#### F1.4.3 — Site Shell

##### T1.4.3.1 — Implement the header and navigation
- **Depends on:** T1.1.3.1, T1.4.2.1
- **Acceptance criteria:** Navigation matches the sitemap; the mobile menu works by touch and keyboard; the current page is indicated; the language switcher is present; correct at all breakpoints.

##### T1.4.3.2 — Implement the footer
- **Depends on:** T1.4.2.1, DEC-010
- **Acceptance criteria:** Footer contents match T1.1.3.1; social links per DEC-010 have accessible labels; no embedded widgets from filtered platforms.

##### T1.4.3.3 — Implement the page template and error pages
- **Depends on:** T1.4.3.1, T1.4.3.2
- **Acceptance criteria:** A shared page template with per-page metadata slots; custom 404 page in Persian and English.

### S1.5 — Page Implementation

Each page feature must also satisfy the **Page Implementation Standard** (§10). Tasks below list only page-specific work. Every page task depends on S1.4, the page's design sign-off (T1.2.2.3), and its approved content (T1.1.4.2).

**Recommended order:** PAGE-001 → PAGE-002, PAGE-003, PAGE-004, PAGE-010, PAGE-013/014 → PAGE-007, PAGE-012, PAGE-008 → PAGE-006 → PAGE-011 → PAGE-009. Pages can be built in parallel once S1.4 is complete.

#### F1.5.1 — PAGE-001 صفحه ی اصلی

##### T1.5.1.1 — Implement the home page
- **Acceptance criteria:** All sections present; each main activity links to its page; the events section follows DEC-005.
- **Subtasks:**
  - [ ] Hero
  - [ ] Main activities
  - [ ] Events (DEC-005)

#### F1.5.2 — PAGE-002 معرفی خدمات

##### T1.5.2.1 — Implement the services page
- **Acceptance criteria:** All sections present; links to the service pages defined in the sitemap; prices follow DEC-015.
- **Subtasks:**
  - [ ] Skills each activity strengthens
  - [ ] Cost and discounts for larger sets
  - [ ] Authenticity of the LEGO sets (shared with PAGE-007 from a single content source)

#### F1.5.3 — PAGE-003 ساخت لگو

##### T1.5.3.1 — Implement the LEGO building page
- **Acceptance criteria:** The center's sets are introduced as designed; set information is stored as structured content, not embedded in markup (supports DEC-028 without building Phase 2 functionality).
- **Subtasks:**
  - [ ] Introduction of the LEGO sets

#### F1.5.4 — PAGE-004 کارگاه لگو بوست

##### T1.5.4.1 — Implement the LEGO Boost workshop page
- **Acceptance criteria:** Workshop content as designed; link to PAGE-014 per DEC-001.
- **Subtasks:**
  - [ ] Workshop introduction (content from T1.1.4.1)
  - [ ] Link to buying the Boost set (PAGE-014)

#### F1.5.5 — PAGE-010 معرفی دوره های کارگاهی

##### T1.5.5.1 — Implement the workshop courses page
- **Acceptance criteria:** Courses grouped by age category; each course shows cost, duration, instructor(s), and capacity per DEC-004; course data stored as structured content that is easy to update (DEC-017).
- **Subtasks:**
  - [ ] Age-based categorization
  - [ ] Cost, capacity (DEC-004), duration
  - [ ] Instructor profiles with background
  - [ ] Course videos (DEC-011)

#### F1.5.6 — PAGE-013 فروش and PAGE-014 ست لگو بوست

##### T1.5.6.1 — Implement the sales and Boost set pages
- **Acceptance criteria:** A visitor can understand how to buy using the method in DEC-003; no checkout or payment interface; PAGE-014 reachable as defined in DEC-001.
- **Subtasks:**
  - [ ] Buying guide (راهنمای خرید)
  - [ ] Boost set page (PAGE-014)
  - [ ] Purchase path per DEC-003

#### F1.5.7 — PAGE-006 گالری

##### T1.5.7.1 — Implement the gallery
- **Acceptance criteria:** Images served in responsive sizes and modern formats with lazy loading; every image has Persian and English alt text; only consented media of children (DEC-013); page meets the performance target on mobile.
- **Subtasks:**
  - [ ] Environment photos
  - [ ] Children's projects
  - [ ] Workshop photos
  - [ ] Accessible image viewer

#### F1.5.8 — PAGE-007 درباره ی ما

##### T1.5.8.1 — Implement the about page
- **Acceptance criteria:** All sections present; videos follow DEC-011.
- **Subtasks:**
  - [ ] Beginning (شروع)
  - [ ] History of activity
  - [ ] Goals
  - [ ] Educational approach
  - [ ] Authenticity of the LEGO sets (shared content)
  - [ ] Opening photos and videos

#### F1.5.9 — PAGE-008 تماس با ما

##### T1.5.9.1 — Implement the contact page
- **Acceptance criteria:** Phone numbers are tappable (`tel:`) on mobile; working hours shown with Persian digits in Persian; the map works without VPN (F1.6.1); social links per DEC-010.
- **Subtasks:**
  - [ ] Address and map
  - [ ] Contact channels
  - [ ] Working hours
  - [ ] Social pages

#### F1.5.10 — PAGE-009 کارن و کیانا

##### T1.5.10.1 — Implement the Karen and Kiana page
- **Blocked by:** DEC-007. Content, subtasks, and acceptance criteria are defined after the decision.

#### F1.5.11 — PAGE-011 همکاری

##### T1.5.11.1 — Implement the collaboration page
- **Acceptance criteria:** All sections present; the request method follows DEC-009 and works end to end (F1.6.2 if a form is chosen).
- **Subtasks:**
  - [ ] Center introduction, goals, and values (creativity, problem solving, teamwork, hands-on learning)
  - [ ] Collaboration models: workshops at the school or the center; group visits
  - [ ] How to request a meeting (DEC-009)

#### F1.5.12 — PAGE-012 پرسش های متداول

##### T1.5.12.1 — Implement the FAQ page
- **Acceptance criteria:** Questions operable by keyboard and screen reader; content in Persian and English per DEC-002; FAQ structured data validates.
- **Subtasks:**
  - [ ] Age
  - [ ] Prerequisites
  - [ ] Level
  - [ ] What to bring
  - [ ] Safety and child care

### S1.6 — Integrations, SEO & Analytics

#### F1.6.1 — Location and Map

##### T1.6.1.1 — Implement the location block and map
- **Depends on:** DEC-022, T1.4.2.1
- **Acceptance criteria:** Map shows the center's location and loads in Iran without VPN; navigation links open the apps chosen in DEC-022; a static fallback (image and address) appears if the map fails; the map loads lazily and does not block rendering.

#### F1.6.2 — Request and Contact Handling (Conditional on DEC-009)

##### T1.6.2.1 — Implement request submission
- **Depends on:** DEC-009, DEC-018
- **Acceptance criteria (if a form is chosen):** Server-side validation, including Iranian phone formats; spam protection that works in Iran without Google reCAPTCHA; submissions reliably delivered to the destination in DEC-009, with alerts on delivery failure; success and error messages in Persian and English. If DEC-009 selects contact channels only, this task is closed as *Not needed* with a reference to the decision.

#### F1.6.3 — Analytics

##### T1.6.3.1 — Integrate analytics
- **Depends on:** DEC-021
- **Acceptance criteria:** Page views (and events defined in DEC-021) recorded for visitors in Iran without VPN; staging traffic excluded; the analytics script does not break the performance targets.

#### F1.6.4 — SEO and GEO

##### T1.6.4.1 — Implement technical SEO
- **Depends on:** T1.4.3.3, T1.1.3.2
- **Acceptance criteria:** Unique title and description per page and locale; canonical URLs; fa/en hreflang; `sitemap.xml` and `robots.txt`; Open Graph metadata; semantic headings; local business structured data (address, hours, phone) validates.

##### T1.6.4.2 — Implement GEO
- **Blocked by:** DEC-008. Acceptance criteria are defined after the decision.

### S1.7 — Quality Assurance & Hardening

Tests are written alongside each feature. This stage completes coverage and runs final verification.

#### F1.7.1 — Automated Testing

##### T1.7.1.1 — Define core user journeys and implement E2E tests
- **Depends on:** S1.5, DEC-025
- **Proposed journeys** (derived from overview §3; to confirm):
  1. Parent: home → activity or course page → age suitability, price, duration → how to register or contact.
  2. Parent: finds location, working hours, and contact channels.
  3. Organization: home → collaboration page → requests a meeting (DEC-009).
  4. Visitor switches language and lands on the equivalent page.
  5. Buyer: sales page → Boost set → understands the purchase method (DEC-003).
- **Acceptance criteria:** Each confirmed journey has E2E tests running in CI on mobile and desktop viewports, in Persian (and English per DEC-002); failures block merging.

##### T1.7.1.2 — Complete unit and integration tests for critical functionality
- **Acceptance criteria:** Locale utilities, locale routing and direction, navigation behavior, and form validation/submission (if any) covered; all pass in CI.

##### T1.7.1.3 — Add automated responsive and accessibility checks to CI
- **Acceptance criteria:** Automated accessibility scan of every page in both locales with zero critical/serious violations; layout checks at the defined breakpoints for key pages.

#### F1.7.2 — Manual Verification

##### T1.7.2.1 — Test across browsers and devices
- **Depends on:** DEC-024
- **Acceptance criteria:** All pages checked on the support matrix, including real Android and iOS devices; issues fixed or explicitly accepted.

##### T1.7.2.2 — Test from Iranian networks
- **Acceptance criteria:** Staging checked **without VPN** on at least one mobile operator and one fixed-line ISP; no failed or blocked third-party requests; with all third-party domains blocked in browser developer tools, pages still render fully.

##### T1.7.2.3 — Review accessibility manually
- **Acceptance criteria:** Keyboard-only walkthrough of every page; screen reader spot checks in Persian (TalkBack, VoiceOver); layout usable at 200% zoom.

##### T1.7.2.4 — Proofread content and run stakeholder acceptance
- **Acceptance criteria:** Persian copy proofread (spelling, نیم‌فاصله, terminology, Persian digits); English copy reviewed; prices, hours, and contact details confirmed by the center; written sign-off.

#### F1.7.3 — Performance and Security Hardening

##### T1.7.3.1 — Verify performance
- **Acceptance criteria:** Targets in §7 met on key pages (home, gallery, courses), measured on staging from an Iranian network.

##### T1.7.3.2 — Harden security
- **Acceptance criteria:** HTTPS only with HSTS; security headers configured (Content-Security-Policy, X-Content-Type-Options, Referrer-Policy, frame-ancestors); no known high or critical dependency vulnerabilities; no secrets in the repository; form endpoints rate-limited (if any); staging access restricted.

### S1.8 — Launch in Iran

#### F1.8.1 — Production Environment

##### T1.8.1.1 — Set up production hosting, DNS, SSL, and backups
- **Depends on:** T1.3.5.1, T1.3.5.3
- **Acceptance criteria:** Production provisioned per DEC-018; domain resolves; valid SSL with automatic renewal; HTTP redirects to HTTPS; backups configured and one restore tested.

##### T1.8.1.2 — Enable approval-based production deployment and rollback
- **Depends on:** T1.3.5.2
- **Acceptance criteria:** Production deploys only approved builds from the main branch through the pipeline; rolling back to the previous version tested once.

#### F1.8.2 — Go-Live

##### T1.8.2.1 — Complete the pre-launch checklist and go live
- **Depends on:** S1.7, F1.8.1
- **Acceptance criteria:** All criteria in §11 met; deployed; smoke-tested from Iranian networks without VPN; analytics receiving data.

##### T1.8.2.2 — Complete registrations and listings
- **Acceptance criteria:** Search engine verification done and sitemap submitted; the center's listing created or updated on the map services chosen in DEC-022; Samandehi registration completed if required (see iran-constraints §5).

#### F1.8.3 — Post-Launch Operations and Handover

##### T1.8.3.1 — Set up monitoring
- **Acceptance criteria:** Uptime monitoring includes at least one check from inside Iran and one from outside; alerts reach a named person.

##### T1.8.3.2 — Write handover documentation
- **Acceptance criteria:** Content update guide (per DEC-017); deployment and rollback runbook; inventory of accounts (domain, hosting, analytics) with confirmed owner access, stored securely.

##### T1.8.3.3 — Hold the post-launch review
- **Acceptance criteria:** Review held after launch using analytics and feedback; outcomes recorded; development plan updated; scheduling of PAGE-005/PAGE-015 revisited (DEC-032).

## 10. Page Implementation Standard

Applies to every page feature in S1.5:

- [ ] Matches the signed-off Figma design at mobile, tablet, and desktop
- [ ] Persian (RTL) complete; English (LTR) per DEC-002
- [ ] Approved copy only; no placeholder text
- [ ] Semantic HTML, correct heading hierarchy, alt text, keyboard accessible
- [ ] Unique SEO metadata per locale (T1.6.4.1)
- [ ] Images optimized: responsive sizes, modern formats, lazy loading below the fold
- [ ] No runtime requests to foreign third-party domains unless approved in `decisions.md`
- [ ] Automated accessibility check passes; E2E coverage if part of a core journey
- [ ] Deployed to staging and reviewed on a real mobile device

## 11. Phase Completion Criteria (MVP Launch)

- [ ] All in-scope PAGE-IDs live in production (PAGE-009 per DEC-007), in Persian and in English per DEC-002
- [ ] All confirmed requirements in §4 met
- [ ] Quality targets in §7 (as confirmed in DEC-024) met
- [ ] CI runs all tests on every change; production deployments happen only through the pipeline after approval
- [ ] Verified in production from inside Iran without VPN on mobile and fixed networks
- [ ] Every decision needed for Phase 1 recorded in `decisions.md`
- [ ] Handover documentation complete; stakeholder sign-off

## 12. Decisions Affecting This Phase

| Stage | Decisions |
|---|---|
| S1.1 | DEC-001–DEC-007, DEC-009, DEC-010, DEC-011, DEC-012–DEC-015 |
| S1.2 | DEC-023, DEC-024, DEC-026 |
| S1.3 | DEC-016–DEC-020, DEC-025, DEC-033, DEC-034 |
| S1.6 | DEC-008, DEC-021, DEC-022 |

## 13. Phase-Specific Risks

Project-level risks: [development-plan.md §12](../development-plan.md). Additional risks for this phase:

- Several design review rounds per page can stretch S1.2; review sets of pages together.
- Developers routinely using a VPN can hide Iran-specific failures; T1.7.2.2 is mandatory before launch.
- Losing access to Figma during design; mitigated by T1.2.3.2.
