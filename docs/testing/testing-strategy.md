# Testing Strategy — LEGO Center Website (K-A-website)

**Status:** Proposed strategy (tools and numeric gates marked for approval)  
**Audience:** Future implementation and QA sessions  
**Sources:** `docs/project/project-overview.md`; `docs/project/pages.md`; `docs/project/development-plan.md`; project conversation (Farsi-first RTL site; Figma → code; launch in Iran; Phases 1–4)

---

## Table of contents

1. [Project context and assumptions](#1-project-context-and-assumptions)
2. [Testing objectives and scope](#2-testing-objectives-and-scope)
3. [Testing methodology](#3-testing-methodology)
4. [Testing pyramid](#4-testing-pyramid)
5. [White-box and black-box strategies](#5-white-box-and-black-box-strategies)
6. [Testing types](#6-testing-types)
7. [Recommended tools and rationale](#7-recommended-tools-and-rationale)
8. [Test environment and test data](#8-test-environment-and-test-data)
9. [Automation, workflows, and CI/CD](#9-automation-workflows-and-cicd)
10. [Quality goals, coverage, and quality gates](#10-quality-goals-coverage-and-quality-gates)
11. [Risks and mitigations](#11-risks-and-mitigations)
12. [Open questions and decisions requiring approval](#12-open-questions-and-decisions-requiring-approval)
13. [Phased implementation roadmap](#13-phased-implementation-roadmap)

---

## 1. Project context and assumptions

### 1.1 Confirmed facts

| Fact | Source |
|---|---|
| The repository is documentation-only. There is no application code, test suite, CI pipeline, or hosting config. | Repo inspection; `development-plan.md` §2 |
| Product is a Farsi-first, RTL, responsive public website for a LEGO construction center. | Conversation; `development-plan.md` §1 |
| Workflow is Figma → implementation in this repo → launch in Iran. | Conversation |
| Phase 1 (MVP) is informational pages. Visitors do not book or pay online. | Conversation; `development-plan.md` §3.1 |
| Documented MVP quality bar: unit/integration for critical functionality; E2E for core user journeys; basic responsive and accessibility checks; all tests run in CI before deploy. | `project-overview.md` §2.2.2 |
| CI/CD must validate before merge and deploy approved changes consistently. | `project-overview.md` §2.2.1 |
| MVP also requires FAQ, location and map, basic SEO, simple navigation, social links, performance, analytics, mobile and tablet. | `project-overview.md` §2.2 |
| PAGE-011 includes a cooperation / meeting-request form. | `pages.md` |
| PAGE-005 (Super Mario) and PAGE-015 (pieces) are TBD / future. | `pages.md` |
| PAGE-016 (آلبوم) is Phase 2: integrate an **existing separate PWA** (sets, specs, availability). Integration method is unresolved. | Conversation; `pages.md` |
| Phase 3 is booking (events, workshops with capacity, رزرو برای ساخت). | Conversation; `project-overview.md` §1.3 |
| Phase 4 is Iranian-capable payment for bookings and sales. | Conversation |
| Technology stack is **not chosen**. | Conversation; `development-plan.md` §4.2 |
| Bilingual is listed in MVP docs; conversation decided Farsi-first RTL. Conflict unresolved. | `project-overview.md` vs conversation |
| PAGE-014 is assigned twice in `pages.md`. | `pages.md` |

### 1.2 What does not exist (do not test as if it shipped)

- No UI, routes, forms, APIs, auth, database, payment, or album integration in this repo
- No Figma files in the repo
- No test framework, coverage reports, or environments
- No documented album PWA contract
- No chosen map, analytics, font, or host vendor

### 1.3 Assumptions (labeled)

These are used only where the repo is silent. They are not product requirements.

| ID | Assumption |
|---|---|
| A1 | Phase 1 is mostly static content plus a cooperation form; domain logic is thin until Phases 2–4. |
| A2 | PAGE-010 cost/capacity in MVP is editorial copy, not a live inventory API (`development-plan.md` §10.3). |
| A3 | Reasonable current browsers used in Iran (Chromium-based, Firefox, Safari) are the compatibility set until a list is approved. |
| A4 | GitHub remains the collaboration remote; CI will attach to that remote unless changed. |
| A5 | “Basic” accessibility means the bar in `development-plan.md` §7.3 (headings, labels, focus, alt text, keyboard, contrast, RTL order), not a named WCAG level, until one is approved. |
| A6 | Production must be verified from an Iran-reachable path, not only from CI runners outside Iran. |

### 1.4 Gaps (do not invent)

- Stack, test runner, E2E tool, a11y engine, performance budget numbers
- WCAG target level
- Form submission backend
- Map and analytics vendors (Iran reachability)
- Hosting and how CI deploys to an Iran-facing origin
- Album PWA API/auth/availability semantics
- Booking and payment designs (Phases 3–4)
- Whether bilingual tests are in scope for MVP

---

## 2. Testing objectives and scope

### 2.1 Objectives

1. Prevent regressions on Phase 1 journeys: discover the center, read programs, trust/FAQ, contact, request partnership.
2. Enforce Farsi-first **RTL** layout, responsive behavior, and basic accessibility in CI.
3. Catch Iran-specific failures (blocked fonts, maps, analytics, CDNs, slow media) before launch.
4. Keep tests aligned with Figma and `pages.md` so implementation sessions have a verifiable done state.
5. Leave a pyramid that can grow for آلبوم, booking, and payment without throwing away Phase 1 suites.

### 2.2 In scope by phase

| Phase | In scope for testing |
|---|---|
| **Now (pre-implementation)** | This strategy; traceability from pages → future tests; no executable tests until code exists |
| **Phase 1 MVP** | Phase 1 pages in `development-plan.md` §3.2; nav/footer; cooperation form; map/contact; FAQ; SEO basics; responsive; basic a11y; performance sanity; Iran smoke |
| **Phase 2** | PAGE-016 album: set list, specs, availability, predicted free time; integration with the existing PWA |
| **Phase 3** | Booking events, workshops (capacity), ساخت appointments |
| **Phase 4** | Payment for bookings and in-scope sales; Iranian PSP flows |

### 2.3 Out of scope until explicitly added

- Full features for PAGE-005 and PAGE-015
- Live booking or payment in Phase 1 suites
- Invented CMS, auth, or admin UIs
- Load testing of systems that do not exist yet
- Legal/compliance certification (not specified)

---

## 3. Testing methodology

### 3.1 Principles

- **Facts over guesses:** If a page section, API, or vendor is unspecified, record a content/integration gap; do not assert expected JSON or copy.
- **Shift left:** Figma review and RTL/responsive checks before large implementation; automated checks from the first mergeable code.
- **Risk-based:** Highest Phase 1 risk is not algorithms — it is broken RTL, unusable mobile nav, failed form, blocked map/fonts in Iran, and visual drift from Figma.
- **Traceability:** Map tests to PAGE-IDs and development-plan tasks.
- **CI as the gate:** `project-overview.md` requires tests before merge and before deploy. Local-only testing is not sufficient.
- **Coverage is a signal, not quality:** See §10.

### 3.2 Test design techniques (when code exists)

| Technique | Use on this project |
|---|---|
| Equivalence / boundaries | Form fields (empty, too long, Farsi vs Latin, email shape) once fields are specified |
| State transitions | Phase 2 set availability (آزاد / در حال ساخت); Phase 3 capacity; Phase 4 payment states |
| Decision tables | Phase 3 booking rules (undesigned — wait) |
| Exploratory + session charters | RTL overflow, Farsi wrapping, gallery media, Iran network |
| Visual comparison vs Figma | Phase 1 page implementation (manual first; optional automated screenshots later) |
| Contract tests | Phase 2 PWA/API once a contract exists |

### 3.3 Roles (until a QA hire is specified)

**Assumption A7:** Implementers write automated tests in the same change as the feature. Exploratory Iran/RTL passes may be done by the project owner. This is not documented in the repo.

---

## 4. Testing pyramid

Phase 1 has little business logic. A **classic 70/20/10 unit-heavy pyramid does not fit** a mostly static RTL marketing site. Use a **Phase 1 pyramid** and plan a **Phase 2+ pyramid**.

```
Phase 1 (MVP)
        / E2E \          few: home → FAQ → contact; cooperation form
       / integ  \        form submit path; optional map/analytics load
      /  unit     \      only real units (validation helpers, date/RTL utils)
     / visual+a11y \     static routes: axe/pa11y, breakpoint screenshots or Playwright viewports
    /  lint/build    \   always-on CI

Phase 2–4 (when domain logic exists)
        / E2E \          critical journeys only (book, pay, album availability)
       / API integ \     PWA/booking/payment adapters
      /  unit        \   booking rules, pricing, availability, payment state machines
```

**Balance:**

| Layer | Phase 1 share | Later share | Why |
|---|---|---|---|
| Lint/build/typecheck | Required | Required | Fastest feedback |
| Unit | Low | High | Almost no domain code in MVP |
| Integration | Medium if a form backend exists; else low | High | Album/booking/payment adapters |
| E2E | Small, stable set | Small, critical money/booking paths | Slow, brittle; still required by overview §2.2.2 |
| Visual / responsive / a11y | **High relative importance in Phase 1** | Continues | Matches documented MVP checks and RTL/Figma workflow |
| Manual Iran smoke | Required at launch | Required on infra/vendor change | CI runners may not represent Iranian networks |

Do not pad unit tests to hit a percentage. Prefer one E2E journey that fails when nav or the form breaks over dozens of snapshot tests of static strings.

---

## 5. White-box and black-box strategies

### 5.1 White-box (structure-aware)

**Purpose:** Exercise known branches in code the team controls.  
**Scope:** Future helpers (form validation, SEO meta builders, availability mappers, booking rules). Not applicable until those modules exist.  
**Methodology:** Read implementation; cover branches, error paths, RTL/locale helpers.  
**Tools:** Unit runner chosen with the stack (**proposed, needs approval** — §7).  
**Examples (future):** Reject empty PAGE-011 submit; map PWA `in_use` → «در حال ساخت»; do not call a blocked analytics URL when disabled.  
**Priority:** Phase 1 — only if non-trivial helpers appear. Phases 2–4 — high.  
**Phase:** Task 4+ of `development-plan.md`.

White-box **does not** replace Figma comparison or Iran reachability.

### 5.2 Black-box (behavior-aware)

**Purpose:** Validate what parents, schools, and staff would see without knowing internals.  
**Scope:** Phase 1 pages, navigation, form success/error, contact/map, later album/booking/payment.  
**Methodology:** Given/when/then from `pages.md` and Figma; exploratory RTL and mobile.  
**Tools:** E2E browser tests; manual checklists; optional visual diffs (**proposed**).  
**Examples:** Open صفحه اصلی; follow nav to تماس با ما; see address; submit همکاری form and see success or error.  
**Priority:** Highest for Phase 1 user-visible quality.  
**Phase:** From first implemented pages through launch.

---

## 6. Testing types

For each type: purpose, scope, methodology, suitable tools, examples, priority, implementation phase.

### 6.1 Unit testing

| | |
|---|---|
| **Purpose** | Fast checks of isolated functions. Matches overview “unit tests for critical functionality.” |
| **Scope Phase 1** | Only extracted logic (validation, URL builders). Static JSX/HTML with no logic: skip or keep to trivial smoke. |
| **Scope later** | Availability, capacity, booking windows, payment amount/status mapping. |
| **Methodology** | Arrange-act-assert; no network; Farsi strings as fixtures when comparing copy helpers. |
| **Tools** | **Proposed (approval required):** whatever is native to the chosen stack (e.g. Vitest/Jest for JS; pytest if Python). Do not install until stack is chosen. |
| **Examples** | `isNonEmptyFarsiName("") === false`; later `availabilityLabel("busy") === "در حال ساخت"`. |
| **Priority** | Phase 1: P2 unless helpers exist. Phase 2–4: P1 for domain rules. |
| **Phase** | Development-plan Task 4/9; expand in Tasks 11–13. |

### 6.2 Integration testing

| | |
|---|---|
| **Purpose** | Verify modules work together (form handler + mail/API; page + CMS; site + PWA). Matches overview “integration tests for critical functionality.” |
| **Scope Phase 1** | Cooperation form submission path once a backend is decided. Do not invent a mock PSP or album API. |
| **Scope later** | HTTP client vs album PWA; booking store; payment callback verification. |
| **Methodology** | Test doubles at the true boundary (HTTP, mail). Contract tests when the PWA schema is known. |
| **Tools** | Same unit runner plus HTTP mocking (**proposed**). |
| **Examples** | Valid form POST returns success page; invalid payload 400; Phase 2: GET sets includes `status`. |
| **Priority** | P1 as soon as any I/O exists; otherwise skip empty layers. |
| **Phase** | Task 7 (forms); Task 11–13. |

### 6.3 End-to-end testing

| | |
|---|---|
| **Purpose** | Core user journeys through a real browser. Required by `project-overview.md` §2.2.2. |
| **Scope Phase 1** | Journeys in `development-plan.md` Task 9: open home, navigate to contact, open FAQ, submit cooperation form if present. |
| **Out of scope Phase 1** | Booking checkout, payment, full album. |
| **Methodology** | Stable selectors (`data-testid` or roles); Farsi visible names; `dir=rtl` assertions; avoid coupling to CSS animation. |
| **Tools** | **Proposed (approval required):** Playwright (good RTL/viewport/CI story) or Cypress. Choice follows stack. |
| **Examples** | `dir` on `html` is `rtl`; nav to PAGE-012; form happy path. |
| **Priority** | P1 — small suite, always green in CI. |
| **Phase** | Task 9; keep green through Task 10. |

### 6.4 Regression testing

| | |
|---|---|
| **Purpose** | New pages (gallery, about) must not break nav, RTL, or the form. |
| **Scope** | Entire Phase 1 suite on every PR; expand with each page. |
| **Methodology** | CI on every change; no skipping the core E2E set to land visuals. |
| **Tools** | Same CI + E2E + unit. Optional visual snapshots later (**approval required** — flaky on fonts). |
| **Examples** | Footer social links still present after PAGE-006 lands. |
| **Priority** | P1 once any automated test exists. |
| **Phase** | Continuous from first test file. |

### 6.5 Security testing

| | |
|---|---|
| **Purpose** | Phase 1: HTTPS, safe forms, no secrets in git, dependency hygiene (`development-plan.md` §9.2). Later: booking abuse, payment callbacks. |
| **Scope Phase 1** | Form injection/XSS in rendered fields; CSRF if a cookie session appears (not specified); dependency audit; secret scanning. |
| **Out of scope until designed** | Auth matrix, IDOR on bookings, PCI assessments. |
| **Methodology** | Checklist on form PR; `npm audit` / equivalent after a lockfile exists; never log PII from the form. |
| **Tools** | **Proposed:** GitHub secret scanning; OS/package audit; later OWASP ZAP only if there is an authenticated or payment surface (**approval required**). |
| **Examples** | Script in name field is not executed; `.env` not committed. |
| **Priority** | P1 for form and secrets; P2 for DAST until there is a backend. |
| **Phase** | Task 7 and 9; heavy in Tasks 12–13. |

**Do not** run aggressive penetration tests against third-party Iranian PSPs or production without a written rule of engagement.

### 6.6 Performance testing

| | |
|---|---|
| **Purpose** | MVP “good performance and fast loading” plus typical Iranian connectivity (`development-plan.md` §4.3, §9.1). **No numeric budget exists.** |
| **Scope Phase 1** | Image weight, font loading, no blocked third-party CDNs, LCP sanity on home and gallery. |
| **Methodology** | Lab: Lighthouse/Playwright metrics on throttled profile. Field: Iran smoke (A6). Do not treat lab scores as Iran reality. |
| **Tools** | **Proposed (approval required):** Lighthouse CI or Playwright `page.goto` + resource sizes; later optional WebPageTest-like check from a reachable region. |
| **Examples** | Home does not request fonts.gstatic.com if that path is rejected in Task 1; gallery images have width constraints. |
| **Priority** | P1 for “blocked CDN / huge hero image”; P2 for synthetic load until traffic exists. |
| **Phase** | Tasks 8 and 10; revisit when media is real. |

**Proposed decision (approval required):** numeric budgets (e.g. max hero image KB, max fonts) after stack and Figma assets exist. Until then, fail CI only on extreme regressions (e.g. uncompressed multi‑MB images) if such a check is implemented.

### 6.7 Accessibility testing

| | |
|---|---|
| **Purpose** | Overview requires **basic** a11y checks in CI. No WCAG level specified. |
| **Scope** | Headings, form labels, focus, alt text, keyboard nav, contrast as in Figma, RTL reading/focus order (`development-plan.md` §7.3). |
| **Methodology** | Automated axe/pa11y on key routes + manual keyboard pass on nav and form. Automated tools miss RTL and Farsi pronunciation issues. |
| **Tools** | **Proposed (approval required):** axe-core via Playwright or `@axe-core/cli`. |
| **Examples** | PAGE-011 inputs have labels; skip-to-content if added in design; decorative gallery images empty alt or similar per Figma. |
| **Priority** | P1 for CI automated scan on home, contact, FAQ, cooperation; P2 for full page list. |
| **Phase** | Task 9. |

**Proposed decision (approval required):** target WCAG 2.2 Level AA vs keep “basic” only.

### 6.8 Responsive design and browser compatibility

| | |
|---|---|
| **Purpose** | MVP mobile and tablet; desktop implied by Figma. Compatibility list not in repo (A3). |
| **Scope** | Breakpoints from Figma; RTL overflow (long Farsi titles, sticky headers); tap targets on mobile nav. |
| **Methodology** | Playwright viewports matching Figma; manual device pass; if Figma omits a breakpoint, log a design gap — do not invent widths. |
| **Tools** | Playwright viewport matrix; optional Chromium/Firefox/WebKit in CI (**approval required** — WebKit on GitHub Linux may be enough). |
| **Examples** | Mobile menu usable in RTL; PAGE-001 hero does not clip CTA. |
| **Priority** | P1 Chromium + one extra engine if CI cost allows; real iOS/Android at launch. |
| **Phase** | Tasks 6, 9, 10. |

### 6.9 Iran reachability and operational testing (project-specific)

Not a classic ISTQB bucket, but required by conversation and `development-plan.md` Task 10.

| | |
|---|---|
| **Purpose** | Fonts, map, media, analytics, host work **inside Iran**. |
| **Scope** | PAGE-008 map; webfonts; gallery; analytics; HTTPS origin. |
| **Methodology** | Checklist from an in-country or representative network; document blocked URLs; CI cannot fully replace this. |
| **Tools** | Browser + network panel; optional simple uptime ping to production. |
| **Examples** | Map tiles load; no infinite spinner on Google Maps if unused; FAQ readable with system/self-hosted fonts. |
| **Priority** | P1 before calling MVP launched. |
| **Phase** | Tasks 1, 8, 10. |

### 6.10 Visual / Figma conformance (project-specific)

| | |
|---|---|
| **Purpose** | Implementation matches approved Figma (`development-plan.md` Task 6). |
| **Scope** | Phase 1 pages at designed breakpoints. |
| **Methodology** | Side-by-side review per page. Automated screenshot diffs only after fonts are stable. |
| **Tools** | Figma + browser; optional Playwright screenshots (**approval required**). |
| **Priority** | P1 manual per page; P2 automation. |
| **Phase** | Task 6–7. |

### 6.11 SEO basics (lightweight)

MVP lists basic SEO. Tests can assert `lang` appropriate for Farsi, a title, and a meta description per route **once copy exists**. Do not invent descriptions in tests.

---

## 7. Recommended tools and rationale

**No tools are installed in this repository.** The following are **proposals requiring approval**. Final choice waits for development-plan Task 3 (stack).

| Need | Proposed option | Rationale | Approval |
|---|---|---|---|
| Unit / integration | Stack-native (Vitest or Jest if JS; other if not) | Avoid a second ecosystem | Required |
| E2E + viewports + RTL | Playwright | Multi-browser, CI-friendly, `dir` and viewport APIs | Required |
| A11y in CI | axe-core on Playwright pages | Fits “basic a11y checks in CI” | Required |
| Visual regression | Defer | Font/Figma instability early | Required if introduced |
| Performance lab | Lighthouse CI or Playwright resource checks | Lightweight; no k6 until booking/payment | Required |
| Security (deps) | Default audit of the chosen package manager | Matches §9.2 of the development plan | Required once lockfile exists |
| Iran smoke | Manual checklist (see §8.3) | Cannot be fully automated from typical GitHub runners | Process approval |

If the stack is not JavaScript, replace the JS-named tools with the equivalent; do not add a JS toolchain solely for tests.

---

## 8. Test environment and test data

### 8.1 Environments (target; none exist yet)

| Environment | Role | Notes |
|---|---|---|
| Local | Dev + unit + subset E2E | RTL/Farsi must render locally |
| CI | Lint, unit, integration, E2E, a11y, responsive viewports | Required by overview §2.2 |
| Staging (if any) | Pre-prod Iran-like config | **Unresolved** whether staging exists |
| Production (Iran-facing) | Task 10 smoke | Real fonts, map, analytics |

Do not point automated destructive tests at production. Phase 1 has little to destroy; Phases 3–4 must use staging bookings and test PSP credentials.

### 8.2 Test data

| Phase | Data | Rules |
|---|---|---|
| Phase 1 | Farsi fixture copy; placeholder images labeled as such; form payloads | No real parent phone numbers in git; no production mailbox dump |
| Phase 2 | Fixture set catalog and availability states | Prefer snapshots of PWA contract; no need to hit production inventory if a sandbox exists (**unresolved**) |
| Phase 3–4 | Synthetic users, sandbox payment | **Unspecified** — design before automating |

### 8.3 Iran smoke checklist (manual until a better probe exists)

For each production (or staging that mirrors vendors):

- [ ] Home loads over HTTPS from inside Iran
- [ ] Farsi webfonts apply (or documented fallback)
- [ ] Nav works on a phone-sized viewport
- [ ] PAGE-008 map usable
- [ ] Gallery media appears
- [ ] Analytics either fires or fails silently as designed
- [ ] Cooperation form delivers to the intended inbox/backend

---

## 9. Automation, workflows, and CI/CD

### 9.1 Development workflow

1. Implement page or helper with the test that proves it (E2E or unit as appropriate).
2. Run unit tests locally; run E2E for touched journeys when feasible.
3. Open PR to the collaboration branch (`main` today).
4. CI must pass before merge (`project-overview.md` §2.2.1–2.2.2).
5. Reviewer checks tests against PAGE-ID / Figma, RTL, and that Phase 2–4 behavior was not silently added.
6. Deploy only after CI green, to the Iran-facing host (mechanism **unresolved**).

### 9.2 Suggested CI jobs (when pipelines exist)

| Job | Blocks merge? | Notes |
|---|---|---|
| Build / typecheck / lint | Yes | |
| Unit + integration | Yes | Empty-skip until code exists |
| E2E core journeys | Yes | Home, contact, FAQ, form |
| A11y scan on key routes | Yes | “Basic” bar |
| Responsive viewport screenshots or layout asserts | Yes if cheap; else nightly | **Approval required** |
| Dependency audit | Warn then fail on high severity | **Approval required** for fail vs warn |
| Deploy | After merge on approved pipeline | Iran origin |

### 9.3 Releases

- Phase 1: tag/release only with green CI + completed Iran smoke checklist.
- Do not skip E2E because “it is only copy.”
- After Phase 3–4: add a release checklist for sandbox booking/payment.

---

## 10. Quality goals, coverage, and quality gates

### 10.1 Coverage vs quality

Line or statement **coverage is not a quality score**. 100% coverage of static presentational code can still ship a broken RTL nav or a blocked map. Prefer:

- Critical journeys encoded as E2E
- Domain rules as unit tests when they exist
- Explicit Iran and a11y checks

**Proposed coverage targets (approval required):**

| Phase | Suggested target | Meaning |
|---|---|---|
| Phase 1 | No hard % gate | Require: CI green; listed E2E; a11y on key routes; no untested form I/O |
| Phase 2+ | Coverage **for domain modules** (availability, booking, payment mappers) at a later agreed % | Do not apply that % to page components |

If a coverage number is desired later, measure it on `src/domain` (or equivalent), not on generated or presentational files.

### 10.2 Measurable Phase 1 quality goals (verifiable without invented vendors)

| Goal | How we know |
|---|---|
| Core journeys automated | CI runs home → contact, FAQ, cooperation form |
| RTL default | E2E or static assert `dir="rtl"` and Farsi `lang` (e.g. `fa` or `fa-IR` once chosen) |
| Responsive | At least one mobile and one tablet viewport in CI, matching Figma if frames exist |
| Basic a11y | Automated scan on home, contact, FAQ, cooperation with zero new serious violations vs baseline |
| Form safety | Integration or E2E success and validation error paths |
| Iran launch | Smoke checklist §8.3 signed off |
| No Phase 3/4 in MVP | Test inventory does not require live booking/payment |

### 10.3 Exit criteria — Phase 1 MVP

MVP testing is **done** when:

1. CI runs the checks in `project-overview.md` §2.2.2 on every merge candidate.
2. E2E covers the Task 9 journeys.
3. Basic a11y and responsive checks run in CI.
4. PAGE-005, PAGE-015, album, booking, and payment are not required to pass MVP.
5. Iran smoke checklist is completed for production.
6. Known placeholders (copy, images, social URLs) are listed, not hidden by tests that assert fake content.

### 10.4 Exit criteria — later phases

- **Phase 2:** Automated coverage of set list, spec fields documented in `pages.md`, availability states, predicted free time; contract tests if an API exists.
- **Phase 3:** E2E reservation for events, workshops (capacity visible), ساخت; integration tests for capacity race **once designed**.
- **Phase 4:** Sandbox payment success, failure, and callback verification; no real charges in CI.

---

## 11. Risks and mitigations

| Risk | Mitigation |
|---|---|
| CI outside Iran is green while production fonts/maps fail | Mandatory Iran smoke; Task 1 vendor list; fail build if Google Fonts/Maps used without an approved fallback |
| Over-investing in unit tests on static pages | Follow Phase 1 pyramid (§4) |
| Flaky visual tests (Farsi fonts) | Delay pixel diffs; assert structure and `dir` first |
| Form backend undecided → no integration tests | Treat form as blocked for “done”; E2E can still fill fields |
| Duplicate PAGE-014 / bilingual conflict | Do not write conflicting tests; wait for Task 0 docs alignment |
| Album PWA unknown | No Phase 2 tests until contract exists |
| Payment testing on production | Forbid; use PSP sandbox only |
| Accessibility “basic” interpreted differently | Approve WCAG level or freeze the §7.3 checklist |

---

## 12. Open questions and decisions requiring approval

### 12.1 Open questions (from product docs; affect tests)

1. Farsi-only vs bilingual MVP — locale tests yes/no?
2. PAGE-014 unique ID?
3. PAGE-011 exact fields and submit mechanism?
4. Map and analytics products?
5. Album PWA contract?
6. Staging environment yes/no?
7. `lang` value (`fa` vs `fa-IR`)?

### 12.2 Proposed decisions — **require explicit approval**

| ID | Proposal | Default if you do not decide yet |
|---|---|---|
| D1 | Use Playwright for E2E, viewports, and axe, after a JS-capable stack is chosen | Do not add Playwright before Task 3 |
| D2 | No percentage coverage gate in Phase 1 | No coverage number in CI |
| D3 | Keep accessibility at “basic” checklist until WCAG AA is chosen | `development-plan.md` §7.3 only |
| D4 | Defer automated visual regression | Manual Figma compare |
| D5 | Defer load/stress tools until Phase 3 | Lab Lighthouse/size checks only |
| D6 | Browser matrix: Chromium in CI; Firefox or WebKit second; real devices at launch | Chromium-only CI is a gap to document |
| D7 | Dependency audit: warn on PR, fail on critical | Warn-only |
| D8 | Iran smoke is a release gate, not a GitHub-only job | Document in release notes |

---

## 13. Phased implementation roadmap

Do not install dependencies or add test code until implementation of the app begins and Task 3 has a stack.

| When | Testing work | Maps to development-plan |
|---|---|---|
| **Now** | This document only | Pre-Task 0 |
| **Task 0** | Update PAGE-ID traceability if IDs change | Docs alignment |
| **Task 1** | Turn Iran vendor decisions into denylist/allowlist checks later | Iran brief |
| **Task 3–4** | Add test runner; `dir`/`lang` smoke; CI skeleton | Bootstrap |
| **Task 5** | E2E: nav + footer + social placeholders | Chrome |
| **Task 6** | Per-page: sections exist; RTL; viewports; Figma review | Pages |
| **Task 7** | Form unit/integration/E2E; XSS check | Forms |
| **Task 8** | Map load (if testable); meta tags; image weight | Map/SEO/perf |
| **Task 9** | Full CI gate as in overview §2.2 | CI/CD |
| **Task 10** | Iran smoke sign-off | Launch |
| **Task 11** | Contract + E2E album | آلبوم |
| **Task 12** | Booking unit/integration/E2E; capacity | Booking |
| **Task 13** | Payment sandbox tests; callback security | Payment |

### 13.1 First executable tests (when code exists)

Suggested order so CI is useful immediately:

1. Build job
2. Assert document language and `dir="rtl"`
3. Visit `/` (or equivalent) and see the home landmark/title
4. Nav to contact and FAQ
5. Axe on those routes
6. Form tests only after the form is implemented

---

## 14. Traceability: Phase 1 journeys → tests

| Journey | PAGE-IDs | Automated (target) | Manual |
|---|---|---|---|
| Discover center | 001, 002, 003, 004 | E2E nav | Figma |
| Trust / FAQ | 012, 007 | E2E open FAQ | Copy review |
| Contact / map / hours / social | 008 | E2E + Iran map smoke | Iran |
| Workshops info (not booking) | 010 | Optional content presence | — |
| Gallery / community | 006 | Responsive + media load | Iran media |
| Partnership request | 011 | Form E2E | Inbox delivery |
| Karo & Kiana | 009 | Route exists | Content TBD |
| Sales guidance | 013, 014 | After ID fix | No checkout |
| Album / book / pay | 016 + later | Out of Phase 1 | — |

---

## 15. Related documents

- `docs/project/project-overview.md` — MVP quality bar
- `docs/project/pages.md` — page inventory
- `docs/project/development-plan.md` — tasks, Iran constraints, DoD

This strategy does **not** start implementation, install packages, or add CI config. Those happen only when separately requested after stack and tool approvals.
