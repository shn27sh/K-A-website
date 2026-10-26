# Testing Strategy

> **Status:** Draft — proposals require approval · **Last updated:** 2026-10-26
> Roadmap: [development-plan.md](../development-plan.md) · Requirements: [project-overview.md](../project/project-overview.md) §2.2.1–2.2.2 · Phase 1 testing work: [phase-1-mvp.md](../phases/phase-1-mvp.md) §7, §10, S1.7 · Decisions: [decisions.md](../project/decisions.md) · Constraints: [iran-constraints.md](../project/iran-constraints.md)

This document defines how the project is tested across all phases: what is tested, how, with which tools, and which gates a change must pass. It is a strategy, not a task list. Tasks and their checkboxes stay in the phase documents, and decisions stay in `decisions.md`.

Items marked **Proposed** need approval. Each maps to a DEC-ID or is listed in [§15](#15-proposals-requiring-approval).

## Contents

1. [Project Context](#1-project-context)
2. [Testing Objectives and Scope](#2-testing-objectives-and-scope)
3. [Testing Methodology](#3-testing-methodology)
4. [Test Types](#4-test-types)
5. [Testing Pyramid](#5-testing-pyramid)
6. [Recommended Tools](#6-recommended-tools)
7. [Test Environments and Test Data](#7-test-environments-and-test-data)
8. [Automation and CI/CD](#8-automation-and-cicd)
9. [Testing in the Development Workflow](#9-testing-in-the-development-workflow)
10. [Quality Goals and Coverage](#10-quality-goals-and-coverage)
11. [Quality Gates and Exit Criteria](#11-quality-gates-and-exit-criteria)
12. [Risks and Mitigations](#12-risks-and-mitigations)
13. [Open Questions and Required Decisions](#13-open-questions-and-required-decisions)
14. [Phased Implementation Roadmap](#14-phased-implementation-roadmap)
15. [Proposals Requiring Approval](#15-proposals-requiring-approval)

## 1. Project Context

### 1.1 Confirmed Facts

| Fact | Source |
|---|---|
| No application code, technology stack, CI, hosting, or test tooling exists; version control is not initialized | development-plan §4 |
| Phase 1 is a content and marketing website of 13 pages with no booking, payment, or user accounts | phase-1-mvp §3 |
| Persian (RTL) is the default locale; English (LTR) is secondary with scope pending | overview §2.2; DEC-002 |
| Every change is tested before merging; approved changes are deployed consistently | overview §2.2.1 |
| Unit/integration tests for critical functionality, E2E tests for core user journeys, basic responsive and accessibility checks, all run in CI before deployment | overview §2.2.2 |
| Quality targets for performance, accessibility (WCAG 2.2 AA), browsers, and SEO are proposed | phase-1-mvp §7; DEC-024 (Pending) |
| Testing tools are undecided | DEC-025 (Pending) |
| Staging and production must be verified from Iranian networks without a VPN | T1.7.2.2; phase-1-mvp §11 |
| No runtime dependency on foreign-hosted resources unless approved | iran-constraints §1; `AGENTS.md` |
| Phase 3 must prevent overbooking under concurrent use | phase-3-booking §9 |
| Phase 4 must test success, cancellation, gateway failure, lost and duplicate callbacks, and timeouts in a sandbox | T4.6.1.1 |

### 1.2 Planned Features and Integrations

Nothing below is implemented. The risk column is this strategy's assessment and sets test priority (§3.1).

| Area | Feature or integration | Phase | Defined in | Test risk |
|---|---|---|---|---|
| Content | 13 pages and their sections | 1 | pages.md; S1.5 | Medium |
| Localization | Locale routing, `lang`/`dir`, language switcher to the equivalent page | 1 | T1.3.3.1; DEC-002 | High |
| Localization | Persian digits, Solar Hijri dates, price formatting, text normalization | 1 | T1.3.3.2; DEC-015 | High |
| Typography | Self-hosted Persian and Latin fonts | 1 | T1.3.3.2; DEC-023 | Medium |
| Shell | Header, mobile menu, footer, 404 page | 1 | F1.4.3 | Medium |
| Components | FAQ accordion, gallery and image viewer, video embed, cards, price display | 1 | T1.2.1.3, T1.4.2.1 | Medium |
| Integration | Map with static fallback | 1 | F1.6.1; DEC-022 | High |
| Integration | Request form (only if chosen) | 1 | F1.6.2; DEC-009 | High if chosen |
| Integration | Video hosting | 1 | DEC-011 | Medium |
| Integration | Social links | 1 | DEC-010 | Low |
| Integration | Analytics | 1 | F1.6.3; DEC-021 | Medium |
| SEO | Metadata, canonical, hreflang, sitemap, robots, structured data | 1 | T1.6.4.1 | Medium |
| SEO | GEO | 1 | DEC-008 | Unknown |
| Content management | Files in the repository, CMS, or admin panel | 1 | DEC-017 | High (content changes may bypass CI) |
| Delivery | CI/CD, staging, production, rollback, monitoring | 1 | F1.3.4, F1.3.5, S1.8; DEC-018, DEC-020 | High |
| Security | HTTPS, HSTS, security headers, dependency hygiene | 1 | T1.7.3.2 | Medium |
| Album | Integration of the separate PWA into PAGE-016; shared set data | 2 | DEC-027, DEC-028 | Unknown |
| Booking | Events, workshops with live capacity, set construction, identification, notifications | 3 | phase-3-booking | High |
| Payment | Gateway, callbacks, verification, reconciliation, sales | 4 | phase-4-payment | High |

### 1.3 Assumptions

| ID | Assumption | Effect on this strategy | Verify by |
|---|---|---|---|
| A-1 | Most visitors are in Iran, mostly on mobile | Mobile-first test priority; Android emphasis in the device matrix | Analytics after launch |
| A-3 | Prices, events, and courses change often after launch | Content changes need validation and regression checks | DEC-014 |
| A-4 | The MVP stores no personal data except form submissions | Phase 1 security scope stays small | DEC-009 |
| A-6 | Phase 1 is mostly pre-rendered pages with little client-side logic | Risk concentrates in content, layout, localization, integrations, and delivery, which shapes the pyramid (§5) | DEC-016 |

A-1, A-3, and A-4 are registered in development-plan §11. A-6 is new and is added there.

### 1.4 Gaps That Affect Testing

These are documented rather than filled in:

- **Stack and tools** (DEC-016, DEC-025) are undecided, so the tools in §6 are a proposal.
- **Quality targets** (DEC-024) are proposals; quality gates in §11 depend on them.
- **English scope** (DEC-002) decides whether the test matrix doubles.
- **Content management** (DEC-017): if content is published without a pull request, content changes skip CI.
- **Request mechanism** (DEC-009) decides whether Phase 1 has any server-side code to test.
- **Breakpoints** are not defined until the Figma tokens exist (T1.2.1.2).
- **Core journeys** are proposed, not confirmed (T1.7.1.1).
- **No owner** is defined for testing inside Iran, real devices, release approval, or defect tracking.
- **No coverage targets or defect severity scheme** exist yet (proposed in §10, §11).
- **Phases 2–4** have no architecture yet; their sections here are principles, to be detailed when each phase starts.

## 2. Testing Objectives and Scope

### 2.1 Objectives

1. Prevent defects that make the site unreachable, slow, or broken for visitors in Iran.
2. Make the Persian RTL experience correct by default, and English correct per DEC-002.
3. Protect trust content: accurate prices, hours, and contact details; children's media published only with consent (DEC-013).
4. Meet the accessibility, performance, and browser targets confirmed in DEC-024.
5. Validate every change in CI before merging, quickly enough that the workflow stays efficient (overview §2.2.1).
6. Keep the test setup extensible to Phases 2–4 without rework.

### 2.2 Scope

| Phase | In scope | Out of scope |
|---|---|---|
| 1 | All in-scope pages in both locales; localization; components; integrations (map, form, analytics, video, social links); SEO output; security headers; performance; accessibility; responsive and browser compatibility; delivery pipeline; reachability from Iran | Load testing (static pages; host and CDN capacity checked with the provider); penetration testing; internals of third-party services (only our integration and fallbacks are tested) |
| 2 | Integration of the album into PAGE-016, the data contract, performance and security at the boundary | Album internals, which the album project tests (phase-2-album §3) |
| 3 | Booking rules, concurrency, identification, notifications, data protection, load | Payment (Phase 4, unless DEC-029 decides otherwise) |
| 4 | Payment flow, failure modes, idempotency, reconciliation, payment security | Gateway internals |

## 3. Testing Methodology

### 3.1 Risk-Based Prioritization

Test effort follows risk: impact on visitors or the center multiplied by likelihood.

| Priority | Meaning | Examples |
|---|---|---|
| P1 | Required before the related release; automated wherever possible | Reachability without foreign resources, RTL layout, locale utilities, core journeys, accessibility scan, security headers |
| P2 | Required before launch; automated or manual | Visual regression, full browser matrix, mutation testing of utilities |
| P3 | Valuable, scheduled when capacity allows | Extended exploratory sessions, external-link monitoring |

### 3.2 Shift Left

- **In design (S1.2):** contrast is checked in the tokens (T1.2.1.2); every component defines its states, RTL and LTR behavior, and focus (T1.2.1.3). Design review catches accessibility and mirroring problems before code.
- **In requirements:** the acceptance criteria in the phase documents are the test oracles. An acceptance criterion that cannot be tested is rewritten before implementation.
- **In code:** tests are written in the same pull request as the code they verify.

### 3.3 Traceability

Test names start with the PAGE-ID or task ID they verify, for example `PAGE-008 contact › phone numbers are tappable links`. A search for an ID then shows its tests. Every acceptance criterion maps to an automated test or a manual checklist item.

### 3.4 White-Box Strategy

**Purpose:** verify internal logic and code paths using knowledge of the implementation.

| Aspect | Approach |
|---|---|
| Scope | Locale utilities; locale resolution and URL builders; content schema validation; component state logic; build-time generation (sitemap, hreflang, metadata, structured data); form validation and submission (if DEC-009 selects a form). Phase 3: booking rules and capacity logic. Phase 4: the payment state machine and verification |
| Techniques | Statement and branch coverage; condition analysis of utilities; mutation testing of critical modules; static analysis (types, lint, logical-properties lint, accessibility lint); review of test code; dependency and secret scanning |
| Phase | From S1.3 (first code) |

Examples:
- Persian normalization: one case per branch: ي → ی, ك → ک, Arabic-Indic and Latin digits, mixed input, empty input, and ZWNJ (U+200C) preserved.
- Locale fallback: what happens when an English counterpart does not exist (per DEC-002).
- Sitemap generation: each page and locale appears exactly once, with reciprocal hreflang entries.

### 3.5 Black-Box Strategy

**Purpose:** verify behavior against requirements without relying on the implementation.

| Technique | Application |
|---|---|
| Requirements-based testing | Every section listed for a page in `pages.md` is present; every acceptance criterion has a test |
| Equivalence partitioning and boundary values | Phone inputs, Solar Hijri date boundaries, price formatting, and in Phase 3, capacity values 0, 1, full, and full + 1 |
| Decision tables | Language switcher: the page has an English counterpart or not, and the visitor is on Persian or English |
| State transitions | Mobile menu and image viewer; booking states (Phase 3); payment states (Phase 4) |
| Journey testing | The core user journeys (T1.7.1.1) |
| Exploratory testing | Time-boxed sessions with written charters |
| Acceptance testing | The center's sign-off on content and behavior (T1.7.2.4) |

Example: equivalence classes for a phone field, if DEC-009 selects a form.

| Input | Class | Expected |
|---|---|---|
| `09123456789` | Valid mobile, Latin digits | Accepted |
| `۰۹۱۲۳۴۵۶۷۸۹` | Valid mobile, Persian digits | Accepted and normalized |
| `٠٩١٢٣٤٥٦٧٨٩` | Valid mobile, Arabic-Indic digits | Accepted and normalized |
| `+989123456789`, `00989123456789` | International format | Accepted and normalized |
| `0912 345 6789` | With spaces | Accepted and normalized |
| `0912345678` | One digit short | Rejected with a Persian error message |
| `02112345678` | Landline | Open question (§13.3) |
| empty or letters | Invalid | Rejected |

Example exploratory charters:
- Explore the Persian pages on a mid-range Android phone over a throttled connection with all foreign domains blocked, looking for layout breaks, missing content, and slow loading.
- Explore language switching from every page, looking for wrong direction, missing translations, and wrong destinations.
- Explore the gallery using only the keyboard, then TalkBack in Persian.

### 3.6 Automated and Manual Testing

Automate everything that is repeatable and deterministic. Keep manual work for what tools cannot judge:
- screen reader testing in Persian;
- real devices and Samsung Internet;
- Iranian mobile and fixed networks without a VPN;
- proofreading Persian copy;
- exploratory testing;
- acceptance testing by the center.

Manual checklists are kept as Markdown files in `docs/testing/` (proposed) so they are versioned with the code.

## 4. Test Types

Each type lists its purpose, scope, method, tools, examples, priority, and the stage where it starts. White-box and black-box are strategies that span these types (§3.4, §3.5). Two types are added beyond the requested list because they carry this project's highest risks: localization (§4.9) and Iran network resilience (§4.10). Tool names refer to the proposal in §6.

### 4.1 Unit Testing

- **Purpose:** fast, isolated verification of logic.
- **Scope (Phase 1):** locale utilities (digits, Solar Hijri dates, price formatting per DEC-015, normalization); URL and slug builders; locale resolution; metadata builders; content schema validators; form validators (if any). Presentational markup is not unit tested; component, page sweep, and visual tests cover it.
- **Method:** white-box, table-driven cases, a fixed clock with the `Asia/Tehran` time zone, Persian fixture strings, no network access.
- **Tools:** Vitest.
- **Priority:** P1. **Starts:** S1.3 (T1.3.3.2).

Illustrative example (function names depend on the implementation):

```ts
describe('T1.3.3.2 locale utilities', () => {
  it.each([
    ['1405', '۱۴۰۵'],
    ['09:30', '۰۹:۳۰'],
  ])('toPersianDigits(%s)', (input, expected) => {
    expect(toPersianDigits(input)).toBe(expected);
  });

  it('normalizes Arabic letters and keeps ZWNJ', () => {
    expect(normalizePersian('مي\u200Cكنم')).toBe('می\u200Cکنم');
  });
});
```

### 4.2 Integration Testing

- **Purpose:** verify that units work together and with their boundaries: rendering with translations, content loading, build output, and external services through fakes.
- **Scope:**
  - **Phase 1:**
    - components rendered in Persian and English (`dir`, accessible names, mirrored icons);
    - the content pipeline, including missing-translation behavior;
    - build output: every page and locale generated, sitemap, robots, canonical, reciprocal hreflang, and structured data that parses with its required fields;
    - the map fallback when the provider fails;
    - analytics disabled on staging;
    - the form handler with a fake delivery channel (if DEC-009 selects a form).
  - **Phase 2:** contract tests against the album's data or API (DEC-027, DEC-028).
  - **Phase 3:** API tests against a real database, booking rules, and concurrency; a fake SMS provider.
  - **Phase 4:** the gateway adapter against the sandbox; callback verification and idempotency.
- **Method:** white-box and grey-box; real collaborators inside the application; fakes only at external boundaries.
- **Tools:**
  - Vitest with Testing Library;
  - MSW for HTTP fakes;
  - html-validate for built HTML;
  - from Phase 3, a database service in CI.
- **Priority:** P1. **Starts:** S1.3; most work in S1.4–S1.6.

Examples:
- Every generated Persian page has `<html lang="fa" dir="rtl">`; every English page has `<html lang="en" dir="ltr">`.
- Every hreflang link points to a page that links back.
- The FAQ structured data contains the same questions as the visible FAQ on PAGE-012.

### 4.3 End-to-End Testing

- **Purpose:** verify the site as a visitor uses it, in real browser engines, against a production build.
- **Scope:** two kinds of test.
  - **Journey tests:** the core journeys in T1.7.1.1, once confirmed.
  - **Page sweep:** generated tests that run every in-scope PAGE-ID × locale × viewport and check:
    - HTTP 200, no console errors, no failed requests;
    - no requests to hosts outside the allowlist (§4.10);
    - title and description present, and one `h1`;
    - no horizontal overflow;
    - an accessibility scan (§4.7) and a screenshot (§4.4).
- **Method:**
  - Black-box, run against the built site in CI, with a smoke subset run against staging and production after each deployment.
  - Select elements by role and accessible name, with names taken from the translation files so the same test runs in both locales. Avoid CSS selectors and fixed waits.
  - Emulate the `fa-IR` locale and the `Asia/Tehran` time zone.
- **Tools:** Playwright.
- **Priority:** P1. **Starts:** harness in S1.4, journeys in S1.5, complete in S1.7 (T1.7.1.1).

Example journey (proposed journey 1 in T1.7.1.1):

```text
Given a parent on PAGE-001 in Persian on a mobile viewport
When they open a main activity and then the workshop courses page (PAGE-010)
Then each course shows age group, cost, and duration in Persian digits
And a visible path to registration or contact is available
```

### 4.4 Regression Testing

- **Purpose:** make sure changes to code, content, dependencies, or configuration do not break existing behavior.
- **Scope:** the full automated suite is the regression suite, plus visual regression and a short manual regression checklist for releases.
- **Method:**
  - Every pull request runs the full fast suite. The full browser matrix runs nightly and before releases.
  - Every fixed defect gets a test that fails without the fix and references the defect.
  - Dependency updates run the full suite.
  - If DEC-017 lets content be published without a pull request, add build-time content validation, a post-publish smoke test, and a scheduled crawl.
- **Visual regression:**
  - Capture screenshots of key pages per locale and viewport.
  - Generate baselines in the CI container so font rendering is consistent.
  - Mask dynamic regions.
  - Use fixture images, never real children's photos (DEC-013).
  - Every baseline update needs a stated reason in the pull request.
- **Tools:** the Playwright suite and its built-in screenshot comparison. This keeps baselines self-hosted and avoids foreign visual-testing services.
- **Priority:** P1 for the automated suite, P2 for visual regression. **Starts:** S1.4.

### 4.5 Security Testing

- **Purpose:** keep the attack surface small and verified, growing with each phase.

| Phase | Scope |
|---|---|
| 1 | HTTPS and HSTS; security headers, including a Content-Security-Policy, which also blocks unapproved foreign resources; dependency vulnerabilities; secrets in the repository; no sensitive data in shipped source maps; iframe restrictions for video and map embeds; staging excluded from search engines with restricted access (T1.7.3.2); form endpoint (if any): validation, output encoding, rate limiting, spam protection without reCAPTCHA |
| 2 | The album boundary: CSP `frame-src` and `connect-src`, CORS, origin isolation |
| 3 | Authentication and authorization (a visitor cannot read or change another person's booking), verification-code brute force, SMS abuse, rate limits, personal data exposure in responses and logs; threat model at the start of S3.2 |
| 4 | Amount and order tampering, forged or replayed callbacks, idempotency, server-side verification, secret storage, no card data on the platform; threat model at the start of S4.3; external review (T4.6.1.2) |

- **Method:** automated scans in CI (dependencies, secrets, header assertions); a dynamic baseline scan against staging; a security checklist in code review for server-side changes; manual review for Phases 3–4.
- **Tools:** OSV-Scanner or `npm audit`; gitleaks; OWASP ZAP baseline scan.
- **Priority:** P1. **Starts:** dependency and secret scanning in S1.3; full Phase 1 hardening in S1.7.

Examples:
- Every response sends `Content-Security-Policy`, `Strict-Transport-Security`, `X-Content-Type-Options: nosniff`, and `Referrer-Policy`. The CSP lists no hosts beyond those approved in `decisions.md`.
- The form endpoint (if any) rejects submissions above a set rate per IP.

### 4.6 Performance Testing

- **Purpose:** meet the performance targets in phase-1-mvp §7 on Iranian mobile networks.
- **Scope:**
  - **Phase 1:** Core Web Vitals in lab conditions, page weight budgets, image delivery, font loading, lazy loading of map and video, and server response time from inside Iran. After launch, real-user measurement if DEC-021 allows it.
  - **Phase 2:** the album's load cost and how fresh its data is on PAGE-016.
  - **Phase 3:** load and concurrency on booking endpoints, for example a spike when a popular workshop opens.
  - **Phase 4:** behavior under gateway timeouts.
- **Method:**
  1. Performance budgets in CI on the built site, with mobile emulation and throttling, taking the median of three runs.
  2. Scheduled measurements from inside Iran against staging, using a runner or server in Iran. Phase-1-mvp §7 requires measurement from an Iranian network.
  3. Real-user Web Vitals after launch, sent to the analytics tool chosen in DEC-021.
  4. From Phase 3, load tests against staging.
- **Tools:** Lighthouse CI; sitespeed.io (self-hostable) for measurements from Iran; the `web-vitals` library for real-user data; k6 from Phase 3.
- **Proposed page weight budgets** (DEC-024), to be calibrated after the first high-fidelity designs:
  - HTML, CSS, and JavaScript: at most 200 KB compressed per content page;
  - fonts: at most 150 KB WOFF2 in total;
  - the largest above-the-fold image: at most 200 KB.
- **Priority:** P1. **Starts:** budgets in CI in S1.4; verification in S1.7 (T1.7.3.1).

### 4.7 Accessibility Testing

- **Purpose:** meet the accessibility level confirmed in DEC-024 (proposed: WCAG 2.2 AA), in Persian RTL and English LTR.
- **Scope:**
  - all pages in both locales;
  - contrast, focus order and visible focus (mirrored in RTL), headings and landmarks;
  - `lang` on mixed-language text, alt text in both languages;
  - reflow at 320 CSS pixels and 200% zoom, target sizes, reduced motion;
  - form labels and errors.
- **Method:**
  - At design time: contrast and component states in Figma.
  - In code: accessibility lint rules, component tests with axe, and an axe scan of every page and locale in the page sweep.
  - Manually: keyboard walkthroughs, TalkBack (Android) and VoiceOver (iOS) in Persian, and NVDA spot checks on Windows (T1.7.2.3).
  - Automated tools find only part of the WCAG failures, so manual testing is required.
- **Tools:** axe-core with Playwright; html-validate; the Lighthouse accessibility score as a secondary signal.
- **Priority:** P1. **Starts:** S1.2 (design), S1.4 (code), S1.7 (manual).

Example: on PAGE-012, Enter and Space toggle a question, `aria-expanded` updates, focus stays on the toggle, and the axe scan reports no critical or serious violations in either locale.

### 4.8 Responsive Design and Browser Compatibility Testing

- **Purpose:** the site works and looks as designed on the supported browsers and devices.
- **Scope:**
  - the breakpoints from Figma (T1.2.1.2) and the browser matrix in phase-1-mvp §7 (DEC-024);
  - portrait and landscape orientation;
  - enlarged system font sizes on Android;
  - long English strings against shorter Persian ones;
  - Persian font fallback;
  - direction-dependent icons such as arrows.
- **Method:**
  - Automated: Chromium, Firefox, and WebKit (the engine behind iOS Safari) at mobile, tablet, and desktop viewports; a check for no horizontal overflow on every page; visual regression at each breakpoint.
  - Manual: real devices for what emulation cannot cover, including Samsung Internet and real iOS Safari.
  - Cloud device farms are foreign services that usually need international payment and may restrict Iranian users. Plan for physical devices, and evaluate a farm only through the iran-constraints §2 checklist.
- **Tools:** Playwright projects; a physical device set (DEC-034).
- **Proposed automated viewports** (replace with the Figma breakpoints when defined): 360×800 and 390×844 (phones), 768×1024 (tablet), 1366×768 and 1920×1080 (desktop).
- **Proposed manual device set:**
  - a mid-range Android phone with Chrome;
  - an older Android version, chosen from market data;
  - Samsung Internet;
  - an iPhone with Safari;
  - an iPad;
  - desktop Chrome, Edge, Firefox, and macOS Safari.
- **Priority:** P1. **Starts:** S1.4; complete in S1.7 (T1.7.2.1).

### 4.9 Localization and Content Testing

- **Purpose:** the Persian-first experience is correct, and content is accurate in both locales.
- **Scope:**
  - `lang` and `dir` per locale, and layout mirroring;
  - mixed-direction text, such as "LEGO Boost" inside Persian sentences, phone numbers, prices, and dates;
  - Persian digits in the Persian interface and Solar Hijri dates;
  - Toman/Rial formatting (DEC-015);
  - no Arabic ي or ك in content, and ZWNJ preserved through the whole pipeline, including minifiers and any CMS;
  - translation completeness per DEC-002, and language-switcher destinations;
  - metadata per locale.
- **Method:**
  - Automated content checks on every change.
  - Page-sweep checks on rendered text.
  - Unit tests of the utilities.
  - Manual proofreading and the center's sign-off on prices, hours, and contact details (T1.7.2.4).
- **Tools:** custom checks run by the unit test runner and Playwright.
- **Priority:** P1. **Starts:** S1.3.

Examples:
- Content files contain no U+064A (ي) or U+0643 (ك).
- Visible text on Persian pages contains no Latin digits, except in elements on an agreed allowlist (§13.3).
- Every Persian page in the English scope has an English counterpart, and the switcher opens it.

### 4.10 Iran Network and Resilience Testing

- **Purpose:** visitors in Iran can reach and use the site without a VPN, including during international disruptions.
- **Scope:**
  - every third-party request;
  - behavior with all foreign domains blocked;
  - reachability from Iranian mobile operators and fixed-line ISPs;
  - reachability from abroad, for search engine crawlers and the English audience (DEC-002);
  - DNS and SSL on staging and production.
- **Method:**
  - **Allowlist test:** every E2E run fails if the page requests a host that is not approved in `decisions.md`.
  - **Blocked-foreign mode:** the page sweep runs with all hosts other than the site's own blocked, and pages must still render completely. This automates the T1.7.2.2 condition.
  - **Network checks:** manual or scripted checks without a VPN on همراه اول, ایرانسل, and رایتل and at least one fixed-line ISP (T1.7.2.2).
  - **Monitoring:** checks from inside and outside Iran (T1.8.3.1).
- **Tools:** Playwright request interception; scripted checks from a server in Iran; uptime monitoring.
- **Priority:** P1. **Starts:** allowlist test in S1.4; network checks once staging exists (T1.3.5.2).

Illustrative allowlist test:

```ts
test('PAGE-001 requests only approved hosts', async ({ page, baseURL }) => {
  const approved = new Set([new URL(baseURL!).host /* plus hosts approved in decisions.md */]);
  const offenders: string[] = [];
  page.on('request', (request) => {
    const url = new URL(request.url());
    if (url.protocol.startsWith('http') && !approved.has(url.host)) offenders.push(url.href);
  });
  await page.goto('/');
  await page.waitForLoadState('networkidle');
  expect(offenders).toEqual([]);
});
```

### 4.11 Summary

| Type | Strategy | Priority | Starts | Automation | Runs |
|---|---|---|---|---|---|
| Unit | White-box | P1 | S1.3 | Full | Every pull request |
| Integration | White/grey-box | P1 | S1.3 | Full | Every pull request |
| End-to-end | Black-box | P1 | S1.4 | Full; manual journeys in acceptance | Every pull request; full matrix nightly; smoke after deploys |
| Regression | Both | P1 (visual P2) | S1.4 | Full plus a short manual checklist | Every pull request; before releases |
| Security | Both | P1 | S1.3 | Partial | Every pull request; staging; per phase reviews |
| Performance | Black-box | P1 | S1.4 | Partial | Every pull request (budgets); scheduled from Iran |
| Accessibility | Both | P1 | S1.2 | Partial | Every pull request; manual before release |
| Responsive and browsers | Black-box | P1 | S1.4 | Partial | Every pull request (Chromium); nightly matrix; manual devices |
| Localization and content | Both | P1 | S1.3 | Partial | Every pull request; proofreading before release |
| Iran network | Black-box | P1 | S1.4 | Partial | Every pull request (allowlist); staging and production checks |

## 5. Testing Pyramid

| Layer | Proposed share of hand-written tests | When it runs | Examples |
|---|---|---|---|
| Static analysis and content checks | Not counted; applies to every file | Every change, in seconds | Types, lint, logical CSS properties, content normalization, documentation link check |
| Unit | About 60–70% | Every pull request | Locale utilities, validators, URL builders |
| Integration and component | About 20–30% | Every pull request | Components in both locales, build output, SEO files, form handler |
| End-to-end journeys | About 5–10% | Every pull request (Chromium); nightly in all engines | The confirmed core journeys |
| Generated page sweep | Generated, not hand-written | Every pull request | Per page × locale × viewport checks |
| Manual and exploratory | Not automated | Before releases | Screen readers, real devices, Iranian networks, acceptance |

**Why this balance.** Unit tests are fast, precise, and stable, so most logic is verified there. Phase 1 has little logic (A-6), though. Much of its risk is in what the site renders: build output, both locales, and external boundaries. That is why integration tests and build-output checks carry more weight than in a logic-heavy application. End-to-end tests are slow and more fragile, so hand-written journeys stay few. The generated page sweep gives broad coverage of every page cheaply. The "inverted pyramid", with many end-to-end tests and few unit tests, is the pattern to avoid: slow pipelines, flaky results, and failures that are hard to diagnose.

**How it shifts in later phases.** Phases 3–4 add significant server-side logic. There, the share of integration tests grows: API tests with a real database, concurrency tests, contract tests, and the gateway sandbox. End-to-end tests stay limited to one journey per booking type and per payment outcome.

## 6. Recommended Tools

**Proposed (DEC-025).** This set assumes DEC-016 selects a JavaScript/TypeScript web stack; DEC-016 is undecided. Playwright, axe-core, Lighthouse CI, ZAP, and k6 work on any running website, so only the unit and integration tools change if the stack is different. Selection criteria: open source, self-hostable, usable from Iran without international payment, and fitting a Windows development environment.

| Purpose | Proposed tool | Rationale | Iran note | Alternatives |
|---|---|---|---|---|
| Unit and integration runner, coverage | Vitest | Fast, TypeScript-native, Jest-compatible API, built-in coverage | npm is generally reachable | Jest |
| Component tests | Testing Library | Queries by role and accessible name, which aligns tests with accessibility | — | Framework-specific test utilities |
| HTTP fakes | MSW | One set of fakes for unit, integration, and local development | — | Built-in mocks |
| E2E, visual regression, responsive | Playwright | Chromium, Firefox, and WebKit; device, locale, and time zone emulation; request interception for the allowlist and blocked-foreign mode; built-in screenshots; free | Browser binaries download from a Microsoft CDN; verify reachability in T1.3.4.1, and use a mirror (`PLAYWRIGHT_DOWNLOAD_HOST`) or the CI cache if needed | Cypress (weaker WebKit support) |
| Accessibility | axe-core (`@axe-core/playwright`) | Widely used rules engine, runs offline in the test suite | — | pa11y-ci |
| Performance | Lighthouse CI; sitespeed.io; `web-vitals` | Budgets in CI; self-hosted measurement from Iran; real-user data | All self-hostable | WebPageTest (self-hosted) |
| HTML validation | html-validate | Offline, configurable | The public W3C validator is a foreign service | Self-hosted Nu validator |
| Static analysis | TypeScript, ESLint, Stylelint with a logical-properties plugin, Prettier | Catches physical `left`/`right` CSS before review | — | — |
| Documentation | Markdown link checker (for example lychee) | Enforces the documentation rule that every relative link resolves | — | markdown-link-check |
| Security | OSV-Scanner or `npm audit`; gitleaks; OWASP ZAP baseline | Dependency, secret, and dynamic scanning without SaaS | The ZAP image is on Docker Hub, which is restricted in Iran; use a mirror | Trivy |
| Mutation testing | StrykerJS (targeted) | Measures whether tests detect faults (§10.4) | — | — |
| Load (Phase 3) | k6 | Scriptable, open source | — | Artillery |
| Contracts (Phases 2–3) | JSON Schema or OpenAPI validation; Pact if two teams evolve independently | Protects the boundary with the album project | — | — |

**Not recommended without approval:** hosted testing services such as cloud device farms, visual-testing SaaS, and hosted synthetic monitoring. They usually need international payment and may restrict Iranian users or IP addresses. If one is needed, evaluate it with the iran-constraints §2 checklist and record it in `decisions.md`.

## 7. Test Environments and Test Data

### 7.1 Environments

| Environment | Purpose | What runs there | Defined in |
|---|---|---|---|
| Local | Development | Static checks, unit and integration tests, E2E against a local build | T1.3.2.1 |
| CI | Validation of every change | Everything in the pull request pipeline (§8) | T1.3.4.1; DEC-020 |
| Preview (optional) | Per-pull-request review | Smoke tests and stakeholder review | Depends on DEC-018 |
| Staging | Pre-production in Iran | Smoke, security baseline, performance from Iran, Iran network checks, manual testing, acceptance | T1.3.5.2 |
| Production | Live site | Post-deploy smoke tests, monitoring | S1.8 |

CI runners hosted abroad may be unable to reach an Iran-hosted staging environment (iran-constraints §8). Tests against staging therefore need a runner inside Iran or the hosting provider's deployment tooling, which is decided in DEC-020.

### 7.2 Test Data

| Data | Approach |
|---|---|
| Content | A dedicated fixture content set in Persian and English for automated tests, separate from real content, so content edits do not break tests. Real content is checked by the page sweep with content-independent assertions |
| Persian edge cases | A shared corpus: ZWNJ words, Arabic ي/ك, Persian, Arabic-Indic, and Latin digits, mixed Persian and English phrases, very long words and titles, empty optional fields |
| Media | Fixture images without people. Real photos of children are used only with consent under DEC-013 and are never committed as test baselines |
| Dates and time | Fixed clock in `Asia/Tehran`. Cases: the Nowruz year change, Esfand 30 in leap years, the Gregorian year boundary, Saturday as week start, Friday as weekend |
| Prices | Zero, small, and very large amounts; formatting per DEC-015; a possible currency redenomination (iran-constraints §6) |
| Personal data (Phase 3) | Synthetic people only; test phone numbers in a provider test mode; no copies of production data; seeded and reset for each test |
| Payments (Phase 4) | Gateway sandbox credentials stored as CI secrets; no real cards; reserved test amounts |
| Secrets | Never in the repository; stored in the CI secret store; scanned by gitleaks |

## 8. Automation and CI/CD

**Proposed (DEC-020, DEC-025).**

| Trigger | Steps | Time budget | Blocking |
|---|---|---|---|
| Pull request | 1. Static checks and content checks · 2. Unit and integration tests with coverage · 3. Production build and build-output checks · 4. E2E journeys and page sweep in Chromium, mobile and desktop, both locales (includes accessibility, allowlist, overflow, metadata checks) · 5. Visual regression · 6. Performance budgets · 7. Documentation link check | 15 minutes or less | Yes; merging is blocked on failure (T1.3.4.1) |
| Merge to main | All pull request checks · deploy to staging · staging smoke tests · ZAP baseline scan | — | Blocks promotion to production |
| Nightly | Full browser matrix (Firefox, WebKit, all viewports) · dependency audit · external link check · performance from Iran | — | Opens a defect on failure |
| Release | Approval · deploy the same build that passed staging · production smoke tests · monitoring · rollback if smoke tests fail (T1.8.1.2) | — | Yes |

Principles:
- **Build once, promote the same artifact** from staging to production.
- **Fail fast:** the cheapest checks run first.
- **Deterministic tests:** no fixed waits; isolated data; fixed clock.
- **Flaky test policy:** a flaky test is quarantined with a named owner and fixed or removed within the time in §10.3. Retries are limited to one and reported, never hidden.
- **Evidence:** traces, screenshot diffs, coverage, and Lighthouse reports are kept as CI artifacts for review.
- **Iran:**
  - Verify, in T1.3.4.1, that package installs, Playwright browser downloads, and container images work from the CI environment.
  - Use mirrors where needed.
  - During an international disruption, foreign-hosted CI may be unable to deploy to Iran. A runner inside Iran reduces this risk (DEC-020).

## 9. Testing in the Development Workflow

### 9.1 During Development

- Tests are written in the same pull request as the code. Test-first is recommended for utilities and validators.
- Fast checks (lint, types, unit tests) run locally before pushing. An optional pre-commit hook runs them on changed files only.
- Every defect fix starts with a failing test.

### 9.2 Code Review Checklist (Proposed)

- [ ] Changed behavior has tests that fail without the change
- [ ] Assertions check behavior, not incidental markup; no large snapshot dumps
- [ ] Persian (RTL) and English (LTR) both checked; logical CSS properties only
- [ ] Screenshot baseline updates are intentional and explained
- [ ] No new third-party host, unless approved in `decisions.md`
- [ ] Accessibility: semantics, labels, focus, alt text in both languages
- [ ] Documentation updated per `.cursor/rules/documentation.mdc`

### 9.3 Definition of Done

Development-plan §13 defines Done at each level. This strategy defines what "tests pass" means at each level through the gates in §11.

### 9.4 Releases

Before each production release:
- staging is verified from an Iranian network;
- the manual regression checklist is completed for the changed areas;
- the center has signed off on any changed content.

After the release, monitoring and analytics are reviewed. Every escaped defect gets a root cause and a regression test.

## 10. Quality Goals and Coverage

### 10.1 Product Quality Targets

Targets for performance, accessibility, browsers, breakpoints, and SEO are defined in [phase-1-mvp.md §7](../phases/phase-1-mvp.md) and confirmed through DEC-024. They are not repeated here. **Proposed additions (DEC-024):**

| Goal | Target | Measured by |
|---|---|---|
| Requests to unapproved hosts | 0 on every page | Allowlist test (§4.10) |
| Rendering with foreign domains blocked | Every page renders completely | Blocked-foreign mode (§4.10) |
| Horizontal overflow | 0 at all tested viewports | Page sweep (§4.3) |
| Missing translations | 0 for pages in the English scope | Content checks (§4.9) |
| Broken internal links | 0 | Page sweep and link checker |
| Page weight | Budgets in §4.6 | Performance budgets in CI |

### 10.2 Coverage Targets

**Proposed (DEC-033).**

| Code area | Line | Branch | Additional |
|---|---|---|---|
| Locale and formatting utilities | ≥ 95% | ≥ 90% | Mutation score ≥ 80% |
| Validators (content schema, forms) | ≥ 90% | ≥ 85% | Every equivalence class has a case |
| Other application logic (routing, metadata, build helpers) | ≥ 80% | ≥ 70% | — |
| Presentational components and pages | No line target | — | Covered by component tests, page sweep, and visual regression |
| Changed code in a pull request | ≥ 80% | — | Coverage of the touched logic must not decrease |
| Phase 3 booking rules; Phase 4 payment logic | ≥ 90% | ≥ 90% | Every rule and state transition has a test; mutation testing |

Requirement coverage:
- 100% of in-scope PAGE-IDs × locales are in the page sweep.
- 100% of confirmed core journeys have E2E tests.
- Every acceptance criterion maps to an automated test or a manual checklist item.

### 10.3 Test Suite Health

**Proposed (DEC-033).**

| Metric | Target |
|---|---|
| Pull request pipeline duration | ≤ 15 minutes |
| Flaky test rate | < 2% of pipeline runs fail and then pass on retry |
| Quarantined tests | Fixed or removed within 5 working days |
| Escaped critical or high defects | Each one gets a root cause and a regression test |

### 10.4 Coverage Does Not Establish Test Quality

Coverage shows which code ran during tests, not whether the tests would detect a fault.
- A test without meaningful assertions can reach 100% coverage.
- Coverage cannot show missing behavior, such as a requirement that was never implemented.
- It cannot see visual or RTL defects, wrong content, browser differences, or network conditions.
- High targets on presentational code encourage brittle snapshot tests.

This strategy therefore complements coverage with:
- mutation testing of critical modules;
- requirement traceability (§3.3);
- review of test code (§9.2);
- the escaped-defect metric (§10.3);
- exploratory testing (§3.5).

## 11. Quality Gates and Exit Criteria

### 11.1 Gates

| Gate | When | Criteria |
|---|---|---|
| G1 Merge | Every pull request | All automated checks pass; coverage thresholds met; review approved with the §9.2 checklist; documentation updated |
| G2 Staging | After each merge to main | Deployment succeeded; staging smoke tests pass; no high-risk findings in the ZAP baseline |
| G3 Feature done | When a feature is completed | Development-plan §13 Feature criteria; Page Implementation Standard (phase-1-mvp §10) for pages |
| G4 Production release | Every release | G2 passed; manual regression of changed areas; no open critical or high defects; content sign-off; rollback ready; approval recorded |
| G5 MVP launch | End of S1.7 | Phase-1-mvp §11 criteria; T1.7.2.1–T1.7.2.4 and T1.7.3.1–T1.7.3.2 complete; no open critical or high defects; medium defects accepted in writing |

**Entry criteria for S1.7:** pages implemented (S1.5), integrations complete (S1.6), content approved (T1.1.4.2), and staging stable.

### 11.2 Defect Severity (Proposed)

| Severity | Definition | Examples | Release rule |
|---|---|---|---|
| Critical | Site or page unavailable or unusable for a main audience; security or privacy breach | Site fails to load in Iran without a VPN; a child's photo published without consent; Phase 4: payment confirmed without verification | Blocks release |
| High | Core content or journey wrong or broken | Wrong price, hours, or phone number; language switcher broken; keyboard trap | Blocks release |
| Medium | Noticeable defect with a workaround | Misaligned RTL section; overflow at one viewport | Allowed with written acceptance |
| Low | Cosmetic | Minor spacing difference from the design | Allowed |

## 12. Risks and Mitigations

| Risk | Impact | Likelihood | Mitigation | Related |
|---|---|---|---|---|
| Developers and testers use a VPN, hiding Iran-specific failures | High | High | Allowlist test and blocked-foreign mode in every run; mandatory no-VPN checks (T1.7.2.2) | DEC-034 |
| No one available to test on Iranian networks and real devices | High | Unknown | Decide who and how early | DEC-034 |
| CI cannot reach Iran-hosted staging, or tool downloads are restricted (browser binaries, container images) | Medium | Medium | Mirrors, CI caching, a runner inside Iran; verify in T1.3.4.1 | DEC-020 |
| Foreign testing services unavailable or impossible to pay for | Medium | High | Self-hosted, open-source tool set (§6) | DEC-025 |
| Content changes bypass CI | High | Medium | Build-time validation, post-publish smoke tests, scheduled crawl | DEC-017 |
| Bilingual scope doubles the test matrix | Medium | Medium | Decide DEC-002 early; generate locale permutations; Persian first | DEC-002 |
| Visual regression noise from font rendering or dynamic content | Medium | Medium | Baselines in a consistent CI container, fixture content, masks, thresholds | — |
| Flaky E2E tests erode trust in CI | Medium | Medium | Role-based selectors, no fixed waits, isolated data, quarantine policy | §10.3 |
| Automated accessibility checks give false confidence | Medium | High | Manual screen reader testing in Persian | T1.7.2.3 |
| Coverage targets are met with weak tests | Medium | Medium | Mutation testing, test review, escaped-defect tracking | §10.4 |
| Pending decisions delay test tooling | Medium | High | Start with the stack-independent layers (Playwright, axe, Lighthouse) | DEC-016, DEC-025 |
| Test baselines include children's images | High | Low | Fixture images only | DEC-013 |
| Overbooking under concurrent use (Phase 3) | High | Medium | Database-level constraints, concurrency integration tests, load tests | phase-3-booking §9 |
| Payment verification errors (Phase 4) | High | Medium | Sandbox tests of all failure modes, idempotency, reconciliation, external review | T4.6.1.1, T4.6.1.2 |
| An international disruption blocks foreign tools during testing or launch | High | Low to medium | Runner inside Iran, local backups, avoid scheduling launch around known risk periods | iran-constraints §1, §8 |

## 13. Open Questions and Required Decisions

### 13.1 Existing Decisions That Affect Testing

"Needed by" follows the decision register.

| Decision | Why it matters for testing | Needed by |
|---|---|---|
| DEC-016 Stack | Unit and integration tools, code structure | T1.3.1.1 |
| DEC-025 Testing tools | Approves or changes §6 | T1.3.1.1 |
| DEC-024 Quality targets | Values for the gates in §11 | T1.2.1.2 |
| DEC-020 CI/CD and deployment path | Where tests run; a runner inside Iran | T1.3.5.1 |
| DEC-018 Hosting | Staging tests, preview environments, performance from Iran | T1.3.5.1 |
| DEC-017 Content management | Whether content changes pass through CI | T1.3.1.1 |
| DEC-002 English scope | Size of the test matrix; translation completeness rules | T1.1.3.2 |
| DEC-009 Request mechanism | Whether Phase 1 has server-side code, form tests, and security tests | T1.2.2.1 |
| DEC-021 Analytics | Real-user performance data; excluding staging traffic | T1.6.3.1 |
| DEC-022 Map, DEC-011 Video | Allowlist entries and fallback tests | T1.2.2.2, T1.1.4.3 |
| DEC-013 Consent | Which media may appear in tests and baselines | T1.1.4.3 |
| DEC-015 Price display | Expected values in formatting tests | T1.2.2.2 |
| DEC-008 GEO | What, if anything, to test for GEO | T1.6.4.2 |

### 13.2 New Decisions Proposed by This Strategy

| ID | Decision needed |
|---|---|
| DEC-033 | Coverage and test suite health targets (§10.2, §10.3) |
| DEC-034 | Testing access inside Iran: who tests on Iranian mobile and fixed networks without a VPN, which physical devices are available, and whether a test runner or server inside Iran is provided |

### 13.3 Open Questions

- Who performs QA: a dedicated tester, the developers, center staff, or a combination?
- Who approves production releases (T1.8.1.2)?
- Where are defects tracked? This likely follows the Git hosting choice in DEC-020.
- Which numbers stay in Latin digits in the Persian interface, if any (for example LEGO set numbers)? This defines the digit allowlist in §4.9.
- Does the request form, if chosen, accept landline numbers?
- Which older Android and iOS versions are supported? Phase-1-mvp §7 defers this to market and analytics data.
- Phase 2: how current must the album's availability status be on PAGE-016, so staleness can be tested?
- Phase 3: does the chosen SMS provider offer a test mode?
- Phase 4: does the chosen gateway offer a sandbox that covers all the failure modes in T4.6.1.1?

## 14. Phased Implementation Roadmap

Existing task IDs are referenced. Items under "Proposed additions" are not yet in the phase documents and are added only after approval.

| Stage | Testing work | Existing tasks | Proposed additions |
|---|---|---|---|
| S1.1 | Approve this strategy; decide DEC-024, DEC-025, DEC-033, DEC-034; confirm the core journeys | T1.1.2.1, T1.7.1.1 (journeys) | Defect severity scheme; review checklist |
| S1.2 | Contrast checks, component states, RTL/LTR variants, and focus in Figma | T1.2.1.2, T1.2.1.3, T1.2.2.2 | Accessibility and mirroring review in design sign-off |
| S1.3 | Test runners; CI with static checks, unit tests, and build; locale utility tests; direction test; dependency audit; staging smoke tests; verify tool downloads from the CI network | T1.3.2.2, T1.3.3.1, T1.3.3.2, T1.3.4.1, T1.3.5.2 | Secret scanning; documentation link check; content checks |
| S1.4 | Component tests; page sweep harness (allowlist, blocked-foreign mode, axe, overflow, metadata); visual baselines; performance budgets in CI | T1.4.1.1, T1.4.2.1, T1.4.3.1–T1.4.3.3 | Page sweep; visual regression; performance budgets in CI |
| S1.5 | Every page joins the page sweep; page-specific tests; journeys implemented as pages land | S1.5 tasks; phase-1-mvp §10 | — |
| S1.6 | Map fallback, form, analytics exclusion, and SEO output tests | T1.6.1.1, T1.6.2.1, T1.6.3.1, T1.6.4.1 | — |
| S1.7 | Complete E2E; full browser matrix; real devices; Iranian networks; performance; security; manual accessibility; acceptance | T1.7.1.1–T1.7.3.2 | Mutation testing of locale utilities; exploratory sessions with charters |
| S1.8 | Production smoke tests; rollback test; monitoring; post-launch review including escaped defects | T1.8.1.2, T1.8.2.1, T1.8.3.1, T1.8.3.3 | — |
| Phase 2 | Contract tests with the album; integration E2E; PWA installation and offline checks; staleness tests | T2.3.1.2, T2.4.1.1 | Contract tests |
| Phase 3 | Threat model; API and database integration tests; concurrency and load tests; authorization tests; SMS test mode; calendar and time zone edge cases | T3.6.1.1–T3.6.1.3 | Threat model; load tests |
| Phase 4 | Threat model; sandbox E2E for every failure mode; idempotency and replay tests; reconciliation tests; external security review; controlled go-live | T4.6.1.1, T4.6.1.2, T4.7.1.1 | Threat model |

## 15. Proposals Requiring Approval

| # | Proposal | Section | Decision |
|---|---|---|---|
| 1 | Adopt this document as the project's testing baseline | All | Approval |
| 2 | Tool set and selection criteria | §6 | DEC-025 |
| 3 | Additional product quality targets and page weight budgets | §4.6, §10.1 | DEC-024 |
| 4 | Coverage and test suite health targets | §10.2, §10.3 | DEC-033 |
| 5 | Testing access inside Iran (people, networks, devices, runner) | §4.8, §4.10, §7.1 | DEC-034 |
| 6 | Pipeline structure and time budget | §8 | DEC-020, DEC-025 |
| 7 | Defect severity scheme and release rules | §11.2 | Approval |
| 8 | Code review checklist | §9.2 | Approval |
| 9 | Manual checklists stored in `docs/testing/` | §3.6 | Approval |
| 10 | New Phase 1 tasks listed under "Proposed additions" | §14 | Approval, then added to phase-1-mvp |
