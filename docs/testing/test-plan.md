# Master Test Plan — LEGO Center Website (K-A-website)

**Document type:** Master test plan (coordination and control)  
**Status:** Proposed (numeric gates, tools, and dates use placeholders or require approval)  
**Companion:** `docs/testing/testing-strategy.md` (approach, pyramid, techniques)  
**Product sources:** `docs/project/project-overview.md`; `docs/project/pages.md`; `docs/project/development-plan.md`

This plan coordinates **what** is tested, **when**, **by whom**, and **when we may release**. It does not replace the strategy. Where this plan and the strategy overlap (gates, pyramid, tools), they must stay aligned. Tool IDs **D1–D8** and assumptions **A1–A7** refer to `testing-strategy.md`.

**Current application state:** documentation only. There is no application source, CI, or executable suite. This plan governs **future** testing from first code through Iran MVP launch and later phases. Do not treat any website feature as already tested.

---

## Table of contents

1. [Project scope and objectives](#1-project-scope-and-objectives)
2. [Features in scope and out of scope](#2-features-in-scope-and-out-of-scope)
3. [Testing levels and methodologies](#3-testing-levels-and-methodologies)
4. [Feature-to-test traceability](#4-feature-to-test-traceability)
5. [Risk-based test matrix](#5-risk-based-test-matrix)
6. [Test priorities](#6-test-priorities)
7. [Test environments and supported browsers](#7-test-environments-and-supported-browsers)
8. [Test data and account management](#8-test-data-and-account-management)
9. [Entry and exit criteria](#9-entry-and-exit-criteria)
10. [Test schedule aligned with development milestones](#10-test-schedule-aligned-with-development-milestones)
11. [Manual versus automated testing responsibilities](#11-manual-versus-automated-testing-responsibilities)
12. [Defect severity and priority](#12-defect-severity-and-priority)
13. [Regression testing policy](#13-regression-testing-policy)
14. [CI/CD quality gates](#14-cicd-quality-gates)
15. [Test reporting and metrics](#15-test-reporting-and-metrics)
16. [Release readiness criteria](#16-release-readiness-criteria)
17. [Risks, dependencies, and mitigations](#17-risks-dependencies-and-mitigations)
18. [Open questions and assumptions](#18-open-questions-and-assumptions)

---

## 1. Project scope and objectives

### 1.1 Product under test

A **Farsi-first, RTL, responsive** public website for a LEGO center. Delivery: Figma → code in this repository → launch **in Iran**. Phases: (1) informational MVP, (2) آلبوم via existing PWA, (3) booking, (4) Iranian payment.

### 1.2 Testing objectives

| ID | Objective | Source |
|---|---|---|
| TO-1 | Prove Phase 1 journeys: discover, trust/FAQ, contact, partnership request | `testing-strategy.md` §2.1 |
| TO-2 | Enforce RTL, Farsi, responsive (mobile/tablet), basic a11y in CI | Overview §2.2; development-plan §7 |
| TO-3 | Catch Iran-specific failures (fonts, map, analytics, CDNs, media, host) before calling launch done | Conversation; Task 10 |
| TO-4 | Keep tests traceable to PAGE-IDs and development-plan tasks | Strategy §3.1 |
| TO-5 | Grow suites for آلبوم, booking, and payment without discarding Phase 1 gates | Strategy §2.1 |
| TO-6 | Block merge and deploy when required checks fail | Overview §2.2.1–2.2.2 |

### 1.3 Items not covered by this plan

- Figma design quality as a design-system audit (Figma is an input; visual conformance is in scope once frames exist)
- Legal/PCI certification (not specified)
- Load testing of systems that do not exist (defer to Phase 3+ per strategy D5)
- Penetration testing of third-party PSPs without a written rule of engagement

---

## 2. Features in scope and out of scope

### 2.1 In scope — Phase 1 (MVP)

Pages from `development-plan.md` §3.2:

| Feature ID | PAGE-ID | Feature | Notes |
|---|---|---|---|
| F-HOME | PAGE-001 | صفحه اصلی | Hero, intro, activities, informational events |
| F-SVC | PAGE-002 | معرفی خدمات | Skills, cost/discounts, authentic sets |
| F-BUILD | PAGE-003 | ساخت لگو | Introduce sets |
| F-BOOST | PAGE-004 | کارگاه لگو بوست | Workshop intro |
| F-GAL | PAGE-006 | گالری | Venue, kids’ builds, workshops |
| F-ABOUT | PAGE-007 | درباره ما | Story, goals, opening media |
| F-CONTACT | PAGE-008 | تماس با ما | Address, map, hours, social |
| F-KK | PAGE-009 | کارن و کیانا | Dedicated page; content TBD |
| F-WS | PAGE-010 | دوره‌های کارگاهی | Editorial cost/capacity/duration — **not** live booking |
| F-PARTNER | PAGE-011 | همکاری | Values, models, meeting-request form |
| F-FAQ | PAGE-012 | پرسش‌های متداول | Age, prerequisites, safety |
| F-SALES | PAGE-013 | فروش | Purchase **guidance** only |
| F-SET | PAGE-014 | ست / خرید لگو بوست | ID conflict unresolved; guidance only |
| F-NAV | — | Shared nav, footer, social | MVP simple navigation |
| F-RTL | — | Farsi-first RTL | Site-wide |
| F-RESP | — | Responsive mobile/tablet | Desktop if Figma provides it |
| F-SEO | — | Basic SEO | `lang`, title, description once copy exists |
| F-A11Y | — | Basic accessibility | Development-plan §7.3 |
| F-PERF | — | Fast loading | No numeric budget yet |
| F-IRAN | — | Iran reachability | Fonts, map, media, analytics, host |
| F-CI | — | CI before merge/deploy | Overview §2.2 |

### 2.2 In scope — later (planned, not MVP exit)

| Feature ID | PAGE-ID / phase | Feature |
|---|---|---|
| F-ALBUM | PAGE-016 / Phase 2 | Set list, specs, آزاد vs در حال ساخت, predicted free time |
| F-BOOK | Phase 3 | Events, workshops with capacity, رزرو برای ساخت |
| F-PAY | Phase 4 | Payment for bookings and in-scope sales |

### 2.3 Out of scope until explicitly added

| Item | Reason |
|---|---|
| PAGE-005 بازی‌سازی با سوپرماریو | TBD in `pages.md` |
| PAGE-015 قطعه | TBD in `pages.md` |
| Live booking or checkout in Phase 1 | Phases 3–4 |
| Locale switcher / English content | Unresolved bilingual vs Farsi-first |
| Auth/admin UIs | Not designed |
| CMS-specific tests | CMS vs static **unresolved** |
| Invented form fields | PAGE-011 fields unspecified |

---

## 3. Testing levels and methodologies

Aligned with `testing-strategy.md` §§3–6. Phase 1 uses a **content/RTL-heavy pyramid**, not a unit-heavy one.

| Level | Method | Phase 1 use | Later use |
|---|---|---|---|
| Unit (white-box) | Isolated functions | Only real helpers (e.g. form validation) | Availability, booking, payment mappers |
| Integration | Boundaries (HTTP, mail) | Form submit once backend exists | PWA, booking store, PSP callbacks |
| E2E (black-box) | Browser journeys | Home, contact, FAQ, cooperation form | Album, book, pay |
| Accessibility | Automated + manual keyboard | Key routes in CI | Expand with new flows |
| Responsive / compatibility | Viewports + browsers | Mobile + tablet in CI; devices at launch | Same |
| Visual / Figma | Side-by-side; optional screenshots | Manual P1 per page (D4: defer auto) | Revisit if fonts stable |
| Security | Form XSS, secrets, dep audit | Form PRs; no DAST required yet | Auth, IDOR, PSP sandbox |
| Performance | Lab size/LCP + Iran field | Image/font/CDN; no k6 (D5) | Booking load when designed |
| Iran operational | Manual smoke | Release gate (D8) | On vendor/infra change |
| Regression | Full core suite every PR | From first test file | Expand, never skip core E2E |

Techniques: equivalence on form fields **once specified**; exploratory RTL/Iran charters; contract tests **only** when the album PWA schema exists.

---

## 4. Feature-to-test traceability

| Feature ID | PAGE-ID | Primary tests | Automated target | Manual target |
|---|---|---|---|---|
| F-HOME | 001 | E2E land; RTL; viewport; a11y; Figma | Yes | Figma compare |
| F-SVC | 002 | Sections present; RTL; Figma | Route/smoke | Figma |
| F-BUILD | 003 | Same | Route/smoke | Figma |
| F-BOOST | 004 | Same | Route/smoke | Figma |
| F-GAL | 006 | Responsive; media load | Viewport | Iran media |
| F-ABOUT | 007 | Route; media | Smoke | Copy/media |
| F-CONTACT | 008 | E2E; map; hours; social | E2E | Iran map |
| F-KK | 009 | Route exists | Smoke | Content TBD |
| F-WS | 010 | Editorial content; **no** book CTA required | Optional presence | No live capacity API |
| F-PARTNER | 011 | Form E2E success/error; XSS; labels | E2E + integration when backend exists | Inbox delivery |
| F-FAQ | 012 | E2E open FAQ | E2E | Copy |
| F-SALES | 013 | Guidance only; no checkout | After copy | — |
| F-SET | 014 | After PAGE-ID fix | Blocked until Task 0 | — |
| F-NAV | — | E2E nav/footer | E2E | Mobile menu RTL |
| F-RTL | — | `dir="rtl"`; `lang` TBD | E2E/static | Overflow charter |
| F-RESP | — | Mobile + tablet viewports | CI | Real phone/tablet at launch |
| F-SEO | — | Title/meta when copy exists | Light assert | — |
| F-A11Y | — | axe on home, contact, FAQ, cooperation | CI | Keyboard pass |
| F-PERF | — | Image weight; no blocked CDNs | Lab if implemented | Iran feel |
| F-IRAN | — | Smoke checklist | Not fully in GitHub CI | **Release gate** |
| F-ALBUM | 016 | Contract + E2E availability | Phase 2 | — |
| F-BOOK | Ph3 | Capacity + reservation E2E | Phase 3 | — |
| F-PAY | Ph4 | Sandbox pay/fail/callback | Phase 4 | Never production charges in CI |

---

## 5. Risk-based test matrix

**Priority legend:** P0 = release blocker if untested or failing; P1 = required for MVP (or that phase); P2 = important, can follow immediately after; P3 = later / nice-to-have.  
**Impact:** parents (primary), schools (secondary), ops/Iran.

| Feature | Biz impact | Main risks | Unit | Integ | E2E | A11y | Resp | Visual | Sec | Perf | Iran | Pri |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F-RTL | All users | Unreadable Farsi layout | — | — | P0 | P1 | P0 | P1 | — | — | P1 | **P0** |
| F-NAV | All users | Cannot reach contact/FAQ | — | — | P0 | P1 | P0 | P1 | — | — | P1 | **P0** |
| F-HOME | Discover | Wrong first impression | — | — | P0 | P1 | P1 | P1 | — | P1 | P1 | **P0** |
| F-CONTACT | Trust / visit | No address/map/hours | — | — | P0 | P1 | P1 | P1 | — | — | **P0** | **P0** |
| F-FAQ | Parent trust | Safety/age unanswered | — | — | P1 | P1 | P2 | P2 | — | — | P2 | **P1** |
| F-PARTNER | Schools | Lost B2B lead; XSS | P1* | **P0*** | **P0** | P1 | P1 | P2 | **P0** | — | P1 | **P0** |
| F-GAL | Trust | Broken images in Iran | — | — | P2 | P2 | P1 | P1 | — | **P1** | **P1** | **P1** |
| F-ABOUT | Trust | Media/copy gaps | — | — | P2 | P2 | P2 | P1 | — | P2 | P2 | **P2** |
| F-SVC / BUILD / BOOST | Programs | Missing sections | — | — | P2 | P2 | P2 | P1 | — | — | P2 | **P1** |
| F-WS | Programs | Mistaken for live booking | — | — | P2 | P2 | P2 | P2 | — | — | — | **P1** |
| F-KK | Brand | Empty page | — | — | P3 | P3 | P3 | P2 | — | — | — | **P2** |
| F-SALES / SET | Pre-commerce | Fake checkout; ID clash | — | — | P3 | P3 | P3 | P2 | P2 | — | — | **P2**† |
| F-SEO | Discover | Missing `lang`/title | — | — | P2 | — | — | — | — | — | — | **P2** |
| F-A11Y | Inclusive | Unlabeled form | — | — | — | P1 | — | — | — | — | — | **P1** |
| F-PERF | Iran UX | Huge images / Google Fonts | — | — | — | — | — | — | — | P1 | P1 | **P1** |
| F-IRAN | Launch | CI green, users blocked | — | — | — | — | — | — | — | P1 | P0 | **P0** |
| F-CI | Quality | Untested merge | — | — | — | — | — | — | P1 | — | — | **P0** |
| F-ALBUM | Phase 2 | Wrong availability | P1 | P0 | P0 | P2 | P1 | P2 | P2 | P2 | P1 | Phase 2 P0 |
| F-BOOK | Phase 3 | Double-book / capacity | P0 | P0 | P0 | P1 | P1 | P2 | P0 | P2 | P1 | Phase 3 P0 |
| F-PAY | Phase 4 | Failed/wrong charge | P0 | P0 | P0 | P1 | P1 | P2 | P0 | P2 | P1 | Phase 4 P0 |

\* Form unit/integration are P0 **only after** a submit backend is chosen. Until then, E2E can fill fields; “form done” stays blocked (`testing-strategy.md` §11).  
† PAGE-014 duplicate: do not automate conflicting routes until Task 0.

**Not in matrix as MVP features:** PAGE-005, PAGE-015.

---

## 6. Test priorities

Derived from parent-primary audience (`project-overview.md` §3) and Iran launch risk.

| Rank | Theme | Why |
|---|---|---|
| 1 | RTL + nav + home | Site unusable if these fail |
| 2 | Contact/map + Iran fonts/host | Cannot visit the center / cannot render |
| 3 | FAQ + cooperation form (incl. security) | Trust and B2B capture |
| 4 | Services / LEGO / Boost / workshops (display) | Core offering |
| 5 | Gallery + performance of media | Trust and connectivity |
| 6 | About, Karo & Kiana, sales guidance | Secondary; sales is not checkout |
| 7 | SEO polish, extra browsers, visual automation | After core journeys |
| 8 | Album / booking / payment | After MVP freeze |

---

## 7. Test environments and supported browsers

### 7.1 Environments

None exist yet. Target model from `testing-strategy.md` §8.1:

| Name | Purpose | Data | Deploy | Status |
|---|---|---|---|---|
| Local | Dev, unit, subset E2E | Fixtures | Developer machine | **TBD** after Task 4 |
| CI | Merge gates | Fixtures | GitHub-hosted (**A4**) | **TBD** after Task 9 |
| Staging | Pre-prod, Iran-like vendors | Non-prod | **TBD** | Unresolved whether it exists |
| Production (Iran-facing) | Task 10 smoke only | Real content | **TBD host** | Destructive automation **forbidden** |

Placeholder: `ENV-STAGING-URL = TBD` · `ENV-PROD-URL = TBD` · `ENV-HOST-VENDOR = TBD`.

### 7.2 Supported browsers and viewports

**No official matrix in the repo.** Strategy assumption **A3** until approved (D6).

| Class | Proposed (approval required) | When |
|---|---|---|
| CI primary | Latest Chromium | Every PR |
| CI secondary | Firefox **or** WebKit | Every PR if cost allows (D6) |
| Launch manual | Current Chrome/Edge Android, Safari iOS, desktop Chrome/Firefox/Safari as used in Iran | Task 10 |
| Viewports | Figma mobile + tablet; desktop if designed. **Do not invent pixel widths.** | CI + manual |

Placeholder: `BREAKPOINT-MOBILE = TBD (from Figma)` · `BREAKPOINT-TABLET = TBD (from Figma)` · `BREAKPOINT-DESKTOP = TBD (from Figma)`.

---

## 8. Test data and account management

### 8.1 Phase 1

| Data | Rule |
|---|---|
| Farsi fixture copy | May be placeholder; tests must not require unpublished final marketing copy |
| Images | Labeled placeholders allowed; production smoke uses real media when provided |
| Form payloads | Synthetic names/emails/phones; **no real parent or school PII in git** |
| Mailbox | Dedicated test inbox **TBD**; not a production staff dump |
| Social URLs | Placeholders listed as such (`development-plan.md` Task 5) |

**Accounts:** Phase 1 has **no user accounts** in requirements. Do not create auth fixtures.

### 8.2 Phase 2–4 (placeholders)

| Need | Placeholder |
|---|---|
| Album PWA sandbox / API key | `ALBUM-CONTRACT = TBD` · `ALBUM-SANDBOX = TBD` |
| Booking test users | `BOOKING-TEST-ACCOUNTS = TBD` (guest vs account unresolved) |
| Staff admin | `STAFF-TEST-ACCOUNTS = TBD` |
| PSP sandbox | `PSP-SANDBOX = TBD` · never production cards in CI |
| Secret storage | CI secrets / env — **not** committed files |

---

## 9. Entry and exit criteria

### 9.1 Pre-implementation (now)

| | Criteria |
|---|---|
| **Entry** | Strategy and this plan exist (this document). |
| **Exit** | Not applicable; no code tests until Task 3–4. Planning complete when PAGE-ID traceability is usable (update after Task 0 if IDs change). |

### 9.2 Per development-plan task (implementation)

| Phase | Entry | Exit |
|---|---|---|
| Task 3–4 bootstrap | Stack chosen and recorded | Local run; `dir`/`lang` smoke; test runner present |
| Task 5 chrome | Figma nav/footer | E2E nav/footer; mobile menu |
| Task 6 each page | Approved Figma frame for that PAGE-ID; content or labeled placeholders | Sections from `pages.md` or documented gap; RTL; viewport; Figma review; **no** live book/pay |
| Task 7 form | Submit mechanism decided | Success/error paths; Farsi fill; no reflected XSS |
| Task 8 map/SEO/perf | Task 1 vendor decisions | Map strategy testable; meta on pages with copy; no blocked-CDN fonts |
| Task 9 CI | Enough journeys to automate | Overview §2.2.2 jobs block merge |
| Task 10 launch | Tasks 6–9 exit; host URL | Iran smoke signed; HTTPS; rollback known |

### 9.3 Phase 1 MVP test cycle

**Entry**

- Figma for in-scope pages approved **or** gaps listed
- Stack chosen
- CI running on the collaboration branch
- PAGE-014 conflict resolved **or** F-SET explicitly deferred in writing

**Exit** — same as `testing-strategy.md` §10.3 and development-plan §11.1 testing aspects:

- CI runs unit/integration (as applicable), E2E core journeys, basic a11y, responsive checks before merge/deploy
- Journeys: home, contact, FAQ, cooperation form (form **done** only if backend exists)
- PAGE-005, PAGE-015, F-ALBUM, F-BOOK, F-PAY not required
- Iran smoke checklist complete
- Placeholders listed
- No P0 open defects; P1 defects waived only with written owner approval (**placeholder process**)

### 9.4 Phase 2 / 3 / 4 test cycles

| Phase | Entry | Exit |
|---|---|---|
| 2 آلبوم | PWA contract documented; integration method chosen | Set list, specs, availability, ETA covered; contract tests if API |
| 3 Booking | Booking rules designed | E2E for events, workshops+capacity, ساخت; no production data corruption |
| 4 Payment | Iranian PSP sandbox | Success, failure, callback; **no real charges in CI** |

---

## 10. Test schedule aligned with development milestones

**No calendar dates exist in the repository.** Use sequence, not fabricated weeks.

Placeholder: `DATE-MVP-LAUNCH = TBD` · `DATE-PHASE-2 = TBD` · `DATE-PHASE-3 = TBD` · `DATE-PHASE-4 = TBD`.

| Milestone | Dev tasks | Test activities | Approx order |
|---|---|---|---|
| M0 Docs | Task 0 | Refresh PAGE-ID matrix | Before Figma freeze |
| M1 Iran constraints | Task 1 | Vendor allow/deny list for later CI | Before stack |
| M2 Design | Task 2 | Figma testability review (RTL, breakpoints, form) | Before code |
| M3 Stack | Task 3–4 | Runner + CI skeleton + RTL smoke | First code |
| M4 Chrome | Task 5 | Nav E2E | After bootstrap |
| M5 Pages | Task 6 | Per-page tests + Figma | Incremental |
| M6 Form | Task 7 | Form automation + security | After/with PAGE-011 |
| M7 Non-functional | Task 8 | Map, SEO, perf lab | After contact/gallery |
| M8 Quality gate | Task 9 | Full merge/deploy CI | Before launch |
| M9 Iran launch | Task 10 | Iran smoke + release review | `DATE-MVP-LAUNCH` |
| M10 آلبوم | Task 11 | Contract + E2E | `DATE-PHASE-2` |
| M11 Booking | Task 12 | Domain + E2E | `DATE-PHASE-3` |
| M12 Payment | Task 13 | Sandbox payment | `DATE-PHASE-4` |

Core regression suite runs **on every PR** from M3 onward (grows from RTL smoke to full MVP set).

---

## 11. Manual versus automated testing responsibilities

**Assumption A7** (strategy): implementers write automated tests with the feature. No named QA hire in the repo.

| Activity | Automated | Manual | Owner (proposed) |
|---|---|---|---|
| Unit / integration | Yes | — | Implementer |
| E2E core journeys | Yes (CI) | Exploratory extras | Implementer |
| A11y engine on key routes | Yes | Keyboard + RTL reading order | Implementer + reviewer |
| Responsive viewports | Yes in CI | Real iOS/Android at M9 | Implementer; owner at launch |
| Figma visual compare | No (D4 defer) | Per page before “page done” | Implementer + design owner **TBD** |
| Iran smoke | No (typical GitHub runners) | Checklist § strategy 8.3 | **TBD** in-country tester / owner |
| Form inbox delivery | Partial | Confirm received | **TBD** |
| Copy accuracy | No | Review | Content owner **TBD** |
| Album/booking/payment | Yes when designed | Exploratory edge cases | Implementer |
| Release sign-off | CI green | Iran + defect review | **TBD** release authority |

**Proposed (approval required):** project owner is release authority until a QA lead is named.

---

## 12. Defect severity and priority

No defect tracker is specified. Use these definitions in whatever tracker is chosen (`TRACKER = TBD`).

### 12.1 Severity (impact)

| Severity | Meaning on this project |
|---|---|
| **S1 Blocker** | Site unusable in Farsi/RTL; cannot navigate; production down in Iran; form stores/executes XSS; later: payment charges wrong or booking corrupts capacity |
| **S2 High** | Contact/map unusable in Iran; main journeys broken on mobile; FAQ/home major content missing; fonts fail so text is unreadable |
| **S3 Medium** | Single inner page layout bugs; gallery image fail with others OK; a11y label missing on non-form page |
| **S4 Low** | Cosmetic vs Figma; placeholder copy; SEO description missing |

### 12.2 Priority (when to fix)

| Priority | Rule |
|---|---|
| **P0** | Fix before merge to `main` / before Iran launch |
| **P1** | Fix before MVP release |
| **P2** | Fix soon after release; do not block if waived |
| **P3** | Backlog |

Typical mapping: S1→P0, S2→P0/P1, S3→P2, S4→P3. A blocked map in Iran is **S2/P0** even if CI abroad is green.

### 12.3 Phase 1 “must not ship”

- RTL inverted or Latin-only default
- Nav broken on mobile
- Cooperation form silently drops submissions **once backend is in scope**
- Secrets in the repo
- Known blocked third-party font/map as the only path

---

## 13. Regression testing policy

Aligned with `testing-strategy.md` §6.4.

1. **Every PR:** lint/build, unit/integration (when present), core E2E, a11y on key routes. Do not skip E2E to land copy or visuals.
2. **Every new PAGE-ID:** add smoke (route + RTL). Do not remove older journeys.
3. **Vendor/infra change** (fonts, host, map, analytics): repeat Iran smoke, not only CI.
4. **Phase 2+:** core Phase 1 E2E remains mandatory; add album/book/pay suites; never replace them.
5. **Visual snapshots:** only if D4 is reversed after fonts stabilize.
6. **Known placeholders** must not be “fixed” by asserting fake production content.

Full regression = CI suite + Iran checklist on production-bound releases.

---

## 14. CI/CD quality gates

From overview §2.2 and strategy §9.2. Jobs **do not exist yet**.

| Gate | Blocks merge? | Blocks deploy? | Notes |
|---|---|---|---|
| Build / typecheck / lint | Yes | Yes | |
| Unit + integration | Yes | Yes | Skip-empty until code; form I/O must not be untested |
| E2E: home, contact, FAQ, form | Yes | Yes | Form journey when implemented |
| A11y key routes | Yes | Yes | Basic bar (D3) |
| Responsive asserts | Yes if cheap; else **TBD** nightly | Prefer yes for merge | Approval in D6 / strategy 9.2 |
| Dependency audit | Warn; fail on **critical** (D7) | Same | After lockfile exists |
| Coverage % | **No** Phase 1 (D2) | No | Domain % only later if approved |
| Iran smoke | No (not on GitHub) | **Yes** (D8) | Manual/process gate |
| Deploy | After merge on approved pipeline | — | Origin **TBD** |

PR review additionally checks: tests map to PAGE-ID; no Phase 3/4 behavior in Phase 1; RTL not broken.

---

## 15. Test reporting and metrics

**No dashboard exists.** Until one is chosen (`REPORTING = TBD`):

### 15.1 Per PR

- CI pass/fail per job
- New/skipped tests
- List of PAGE-IDs touched

### 15.2 Per release (MVP and later)

| Metric | Intent | Caution |
|---|---|---|
| Core E2E pass rate | Must be 100% on the release commit | Do not hide skips |
| Open S1/S2 count | Must be 0 S1; S2 waived in writing | — |
| A11y serious violations on key routes | 0 new vs baseline | Tools miss RTL |
| Iran smoke checklist | 100% items run | Qualitative |
| Placeholder inventory | Known gaps visible | Not a pass/fail % |
| Line coverage | Optional later | **Not** a quality score (`testing-strategy.md` §10) |

### 15.3 Cadence

| Event | Report |
|---|---|
| Each PR | CI status |
| Each Task 6 page done | Figma review note + PAGE-ID |
| M9 launch | Release readiness (§16) |
| Post-launch | Defects from Iran smoke / users — **TBD process** |

---

## 16. Release readiness criteria

### 16.1 Phase 1 (Iran MVP)

Ready **only if** all are true:

1. Development-plan §11.1 product criteria met (Figma-approved Phase 1 pages implemented RTL/responsive; FAQ; map; SEO basics; nav; social; analytics or written exception; performance acceptable on representative Iran connection).
2. Strategy §10.3 / this plan §9.3 test exit met.
3. CI green on the release revision; gates in §14 that are implemented are passing.
4. Iran smoke (`testing-strategy.md` §8.3) completed from in-country or representative network.
5. Zero S1 defects; S2 none or waived with owner name and date (`WAIVER-LOG = TBD`).
6. PAGE-005, PAGE-015, album, booking, payment **not** treated as missing MVP features.
7. Placeholder list published (photos, social URLs, copy).
8. HTTPS origin reachable; rollback/republish path known (Task 10).
9. No live checkout.

### 16.2 Later releases

- Phase 2: §9.4 album exit + Phase 1 regression green + Iran smoke if vendors changed  
- Phase 3: booking E2E + capacity + no production booking corruption  
- Phase 4: sandbox payment paths + **no production charges in CI**

---

## 17. Risks, dependencies, and mitigations

| ID | Risk / dependency | Mitigation |
|---|---|---|
| R1 | CI outside Iran ≠ user experience | D8 Iran smoke; Task 1 vendors |
| R2 | Stack/tools unchosen | No test code until Task 3; D1 default wait |
| R3 | Form backend unknown | Block “form done”; still E2E-fill |
| R4 | PAGE-014 duplicate | No conflicting tests until Task 0 |
| R5 | Bilingual vs Farsi-first | No locale-switch tests until decided |
| R6 | Figma / content late | Placeholders; do not invent copy in asserts |
| R7 | Visual flake (fonts) | D4 defer pixel diffs |
| R8 | Album PWA unknown | No Phase 2 tests until contract |
| R9 | Staging missing | Production-only smoke increases risk; prefer creating staging (**approval**) |
| R10 | No named QA / release owner | Approve A7 and §11 owner |
| R11 | Payment tests hitting production | Forbid; PSP sandbox only |
| R12 | Coverage vanity | D2 no % gate in Phase 1 |
| R13 | Blocked Google Fonts/Maps | Fail or warn if used without fallback after Task 1 |

Dependencies: Task 0 docs; Task 1 Iran brief; Task 2 Figma; Task 3 stack; in-country tester access; album contract before M10.

---

## 18. Open questions and assumptions

### 18.1 Assumptions (inherited + plan-local)

| ID | Assumption |
|---|---|
| A1–A7 | See `testing-strategy.md` §1.3 and §3.3 |
| A8 | This plan’s P0–P3 and S1–S4 are used until a tracker’s scheme is chosen |
| A9 | Sequence in §10 is the schedule; dates stay `TBD` |
| A10 | Implementer-owned automation remains until a QA role is named |

### 18.2 Open questions

Same product questions as strategy §12.1, plus:

1. Who is release authority and in-country smoke tester?
2. Defect tracker and waiver log location?
3. Staging URL yes/no?
4. Exact Figma file and breakpoint values?
5. Form fields, destination, and test inbox?
6. `lang` (`fa` vs `fa-IR`)?
7. Calendar for `DATE-MVP-LAUNCH`?

### 18.3 Decisions requiring approval

Includes strategy **D1–D8**, plus:

| ID | Proposal |
|---|---|
| D9 | Use this document as the master plan; keep PAGE-ID matrix in sync after Task 0 |
| D10 | Severity/priority scheme in §12 |
| D11 | Project owner is release authority until a QA lead is named |
| D12 | No fabricated launch dates; fill `DATE-*` placeholders when known |
| D13 | Create a staging environment before Phase 3 (recommended; not required for Phase 1 if Iran prod smoke is done) |

---

## 19. Related documents

| Document | Role |
|---|---|
| `docs/testing/testing-strategy.md` | How to test; pyramid; tools D1–D8 |
| `docs/project/development-plan.md` | Tasks, DoD, Iran constraints |
| `docs/project/pages.md` | PAGE-ID inventory |
| `docs/project/project-overview.md` | MVP bar, audiences |

This plan does not modify application source (none exists) and does not install CI. Executable tests start only when implementation is separately requested after stack and tool approvals.
