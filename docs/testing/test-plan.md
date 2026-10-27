# Master Test Plan

> **Status:** Draft — proposals require approval · **Last updated:** 2026-10-27
> Strategy: [testing-strategy.md](testing-strategy.md) · Roadmap: [development-plan.md](../development-plan.md) · Requirements: [project-overview.md](../project/project-overview.md), [pages.md](../project/pages.md) · Phase 1: [phase-1-mvp.md](../phases/phase-1-mvp.md) · Decisions: [decisions.md](../project/decisions.md) · Constraints: [iran-constraints.md](../project/iran-constraints.md)

This plan defines **what** is tested, **when**, **by whom**, and against **which criteria**, from Phase 1 through Phase 4. **How** testing is done (test types, tools, pyramid, coverage targets) is defined in the [testing strategy](testing-strategy.md) and is not repeated here. Tasks and their checkboxes stay in the phase documents.

**Conventions**
- Placeholders appear as **[TBD: what — resolved by]**. They mark unknown dates, owners, URLs, and devices; nothing in them is a commitment.
- Items marked **Proposed** need approval (§19).
- "Phase" and "Stage" keep their project meaning (development-plan §3). The plan's testing periods are called **test cycles** (§9).
- Test priorities P1–P3 follow [strategy §3.1](testing-strategy.md#31-risk-based-prioritization). Gates G1–G5 follow [strategy §11.1](testing-strategy.md#111-gates).

## Contents

1. [Scope and Objectives](#1-scope-and-objectives)
2. [Features in Scope and Out of Scope](#2-features-in-scope-and-out-of-scope)
3. [Testing Levels and Methodologies](#3-testing-levels-and-methodologies)
4. [Test Priorities: Business Impact and Risk](#4-test-priorities-business-impact-and-risk)
5. [Risk-Based Test Matrix](#5-risk-based-test-matrix)
6. [Feature-to-Test Traceability](#6-feature-to-test-traceability)
7. [Test Environments and Supported Browsers](#7-test-environments-and-supported-browsers)
8. [Test Data and Account Management](#8-test-data-and-account-management)
9. [Test Cycles: Entry and Exit Criteria](#9-test-cycles-entry-and-exit-criteria)
10. [Test Schedule](#10-test-schedule)
11. [Manual and Automated Testing Responsibilities](#11-manual-and-automated-testing-responsibilities)
12. [Defect Management: Severity and Priority](#12-defect-management-severity-and-priority)
13. [Regression Testing Policy](#13-regression-testing-policy)
14. [CI/CD Quality Gates](#14-cicd-quality-gates)
15. [Test Reporting and Metrics](#15-test-reporting-and-metrics)
16. [Release Readiness Criteria](#16-release-readiness-criteria)
17. [Risks, Dependencies, and Mitigations](#17-risks-dependencies-and-mitigations)
18. [Assumptions and Open Questions](#18-assumptions-and-open-questions)
19. [Proposals Requiring Approval](#19-proposals-requiring-approval)

## 1. Scope and Objectives

**Product:** a Persian-first (RTL), bilingual, responsive website for a LEGO center, launched in Iran (development-plan §2).

**Current state (2026-10-27):** no application code exists. The only automated check is the "Documentation links" job in CI (`.github/workflows/ci.yml`). Every test in this plan is planned work.

**Objectives of this plan**
1. Every in-scope feature is tested at the priority its risk requires (§4, §5) before the release that contains it.
2. Every acceptance criterion in the phase documents maps to at least one automated test or manual check (§6).
3. Testing runs on a schedule tied to development stages, with explicit entry and exit criteria (§9, §10).
4. Release decisions rest on measured results, not on missing checks (§14, §16).
5. The site is verified from inside Iran without a VPN before every production release (§9, §16).

Quality objectives and targets: [strategy §2.1](testing-strategy.md#21-objectives) and [strategy §10](testing-strategy.md#10-quality-goals-and-coverage).

## 2. Features in Scope and Out of Scope

### 2.1 In Scope — Phase 1 (MVP)

Feature IDs are those in [phase-1-mvp.md](../phases/phase-1-mvp.md).

| Area | Features |
|---|---|
| Localization foundation | F1.3.3 locale routing, text direction, language switcher, locale utilities, self-hosted fonts |
| Design system and shell | F1.4.1 tokens, F1.4.2 shared components, F1.4.3 header, navigation, footer, page template, 404 |
| Pages | F1.5.1–F1.5.12: PAGE-001, 002, 003, 004, 006, 007, 008, 009, 010, 011, 012, 013, 014 |
| Integrations | F1.6.1 map, F1.6.2 request handling (only if DEC-009 selects a form), F1.6.3 analytics, F1.6.4 SEO and GEO; video (DEC-011); social links (DEC-010) |
| Non-functional | Performance, accessibility, browser and device compatibility, security hardening (F1.7.3), reachability from Iran |
| Delivery | F1.3.4 CI, F1.3.5 environments and domain, F1.8.1 production, rollback, F1.8.3 monitoring |
| Content | Accuracy of prices, hours, contact details; Persian copy quality; consent for children's media (DEC-013); content publishing path (DEC-017) |

### 2.2 In Scope — Post-MVP (Provisional)

Detailed when each phase starts. Feature IDs are those in the phase documents.

| Phase | Features |
|---|---|
| 2 | F2.3.1 integration of the album into PAGE-016; the data contract with the album project (DEC-027, DEC-028) |
| 3 | F3.4.1 event booking, F3.4.2 workshop booking with live capacity, F3.4.3 set construction booking, F3.4.4 staff tools, F3.4.5 notifications, F3.4.6 user identification (the last three are candidates) |
| 4 | F4.5.1 booking payments, F4.5.2 sales checkout, F4.5.3 refunds, F4.5.4 reconciliation (the last two are candidates) |

### 2.3 Out of Scope

| Item | Reason |
|---|---|
| Booking, payment, and user accounts in Phase 1 | Not part of the MVP (phase-1-mvp §3.3) |
| PAGE-005, PAGE-015 | Unscheduled (DEC-032) |
| Internals of the album project | Tested by that project (phase-2-album §3) |
| Internals of third-party services (map, analytics, video, gateway) | Only the integration and fallbacks are tested |
| Load testing and penetration testing in Phase 1 | Static content site ([strategy §2.2](testing-strategy.md#22-scope)). Load tests are planned for Phase 3; Phases 3–4 have security reviews (T3.6.1.2, T4.6.1.2), and T4.6.1.2 recommends an external review |
| Testing with real personal or payment data | Prohibited; synthetic data only (§8) |

## 3. Testing Levels and Methodologies

| Level | What it verifies | Method | Defined in |
|---|---|---|---|
| Static analysis and content checks | Code and content rules before execution | Automated, white-box | [Strategy §5](testing-strategy.md#5-testing-pyramid) |
| Unit | Isolated logic: locale utilities, validators, builders | Automated, white-box | [Strategy §4.1](testing-strategy.md#41-unit-testing) |
| Integration and component | Components in both locales, build output, boundaries with fakes | Automated, white- and grey-box | [Strategy §4.2](testing-strategy.md#42-integration-testing) |
| System (end-to-end) | Journeys and the page sweep in real browser engines | Automated, black-box | [Strategy §4.3](testing-strategy.md#43-end-to-end-testing) |
| Non-functional | Security, performance, accessibility, browsers, localization, Iran networks | Automated and manual | [Strategy §4.5–4.10](testing-strategy.md#4-test-types) |
| Acceptance | Content and behavior accepted by the center | Manual, black-box | T1.7.2.4 |

Methods: risk-based prioritization, requirements-based testing, equivalence partitioning and boundary values, state transition testing, exploratory testing with charters ([strategy §3](testing-strategy.md#3-testing-methodology)).

## 4. Test Priorities: Business Impact and Risk

Each feature receives an **impact** and a **likelihood** rating. Together they give its **risk**, which sets the priority of each relevant test type.

| Rating | Impact (business) | Likelihood (of defects) |
|---|---|---|
| High | Affects reachability, trust content (prices, ages, contact details), a core journey (T1.7.1.1), privacy or children's consent, security, or money | New or complex logic; depends on Iran conditions, an external service, or a pending decision; changes often |
| Medium | Degrades one page or a secondary journey | Moderate complexity or change rate |
| Low | Cosmetic or peripheral | Simple and stable |

| Impact ↓ / Likelihood → | High | Medium | Low |
|---|---|---|---|
| **High** | High | High | Medium |
| **Medium** | High | Medium | Low |
| **Low** | Medium | Low | Low |

**From risk to test priority:**
- **Default:** a High-risk feature's relevant test types are P1, a Medium-risk feature's are P2, and a Low-risk feature's are P3.
- **Raised to P1** when a type covers a core journey, or when the feature's typical failures for that type would be Critical or High defects ([strategy §11.2](testing-strategy.md#112-defect-severity-proposed)), for example wrong contact details on PAGE-008.
- **Baseline for every page:** the page sweep (accessibility scan, foreign-request allowlist, horizontal overflow, metadata) runs at P1 regardless of risk ([strategy §4.3](testing-strategy.md#43-end-to-end-testing)).

The strategy rates risk by area ([strategy §1.2](testing-strategy.md#12-planned-features-and-integrations)). This plan refines those ratings per feature using business impact.

## 5. Risk-Based Test Matrix

Columns: **U** unit · **I** integration and component · **E2E** end-to-end journeys · **Vis** visual regression · **Sec** security · **Perf** performance · **A11y** accessibility · **Br** responsive and browser compatibility · **L10n** localization and content · **Iran** Iran network and resilience. "—" means not applicable beyond the page sweep baseline.

### 5.1 Phase 1

| Feature | Impact | Likelihood | Risk | U | I | E2E | Vis | Sec | Perf | A11y | Br | L10n | Iran |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F1.3.3 Locale routing, direction, language switcher (T1.3.3.1) | High | High | High | P1 | P1 | P1 | P2 | — | — | P1 | P1 | P1 | — |
| F1.3.3 Locale utilities: digits, Solar Hijri dates, prices, normalization (T1.3.3.2) | High | High | High | P1 | P1 | P2 | — | — | — | — | — | P1 | — |
| F1.3.3 Self-hosted fonts (T1.3.3.2) | Medium | Medium | Medium | — | P2 | — | P2 | — | P2 | — | P2 | P2 | P1 |
| F1.4.3 Site shell: header, mobile menu, footer, 404 | Medium | Medium | Medium | — | P2 | P1 | P2 | — | — | P1 | P1 | P2 | — |
| F1.4.2 Shared components: FAQ accordion, image viewer, cards, price display | Medium | Medium | Medium | P3 | P1 | P2 | P2 | — | — | P1 | P2 | P2 | — |
| F1.5.1 PAGE-001 home | High | Medium | High | — | P2 | P1 | P2 | — | P1 | P1 | P1 | P1 | P1 |
| F1.5.2–F1.5.5 PAGE-002, 003, 004, 010 services, building, Boost workshop, courses | High | Medium | High | P2 | P1 | P1 | P2 | — | P2 | P1 | P1 | P1 | P1 |
| F1.5.6 PAGE-013, 014 sales, Boost set | Medium | Medium | Medium | — | P2 | P1 | P2 | — | P2 | P2 | P2 | P1 | P2 |
| F1.5.7 PAGE-006 gallery | High | Medium | High | — | P2 | P2 | P2 | — | P1 | P1 | P1 | P1 | P1 |
| F1.5.8 PAGE-007 about | Low | Low | Low | — | P3 | — | P3 | — | P3 | P3 | P3 | P3 | P3 |
| F1.5.9 PAGE-008 contact | High | Medium | High | P2 | P2 | P1 | P2 | — | P2 | P1 | P1 | P1 | P1 |
| F1.5.10 PAGE-009 کارن و کیانا | [TBD: DEC-007] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| F1.5.11 PAGE-011 collaboration | Medium | Medium | Medium | — | P3 | P1 | P3 | — | — | P2 | P2 | P2 | P2 |
| F1.5.12 PAGE-012 FAQ | Medium | Medium | Medium | — | P2 | P2 | P3 | — | — | P1 | P2 | P2 | — |
| F1.6.1 Map and location | High | High | High | — | P1 | P1 | P3 | P2 | P1 | P2 | P1 | P2 | P1 |
| F1.6.2 Request form (only if DEC-009 selects one) | High | High | High | P1 | P1 | P1 | P3 | P1 | — | P1 | P1 | P1 | P1 |
| Video embeds (DEC-011) | Medium | Medium | Medium | — | P2 | P3 | — | P2 | P2 | P2 | P2 | — | P1 |
| Social links (DEC-010) | Low | Low | Low | — | — | P3 | — | — | — | P3 | — | — | P2 |
| F1.6.3 Analytics | Medium | Medium | Medium | — | P2 | P3 | — | P2 | P2 | — | — | — | P1 |
| F1.6.4 Technical SEO (T1.6.4.1) | Medium | Medium | Medium | P2 | P2 | — | — | — | — | — | — | P2 | — |
| F1.6.4 GEO (T1.6.4.2) | [TBD: DEC-008] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] | [TBD] |
| Content publishing path (DEC-017) | High | Medium | High | — | P1 | P2 | P2 | P2 | — | — | — | P1 | — |
| F1.7.3 Security hardening: HTTPS, headers, dependencies | High | Low | Medium | — | — | — | — | P1 | — | — | — | — | — |
| F1.3.4, F1.3.5, F1.8.1, F1.8.3 Delivery: CI, staging, production, rollback, monitoring | High | Medium | High | — | — | P1 | — | P2 | P2 | — | — | — | P1 |
| Cross-cutting: reachability and speed from Iran (T1.7.2.2, T1.7.3.1) | High | High | High | — | — | P1 | — | — | P1 | — | P1 | — | P1 |

Notes:
- **Security hardening** is Medium risk but P1. The checks are cheap, and a failure could be Critical.
- **Content publishing** values assume DEC-017 allows publishing without a pull request. If all content goes through pull requests, its I and L10n checks are already covered by the page rows.
- **PAGE-009 and GEO** are rated after DEC-007 and DEC-008.

### 5.2 Phases 2–4 (Provisional)

Re-rated when each phase is detailed.

| Feature | Impact | Likelihood | Risk | U | I | E2E | Vis | Sec | Perf | A11y | Br | L10n | Iran |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F2.3.1 Album integration (PAGE-016) | Medium | High | High | — | P1 | P1 | P2 | P2 | P2 | P2 | P2 | P2 | P1 |
| F3.4.1, F3.4.2 Event and workshop booking, live capacity | High | High | High | P1 | P1 | P1 | P2 | P1 | P1 | P1 | P1 | P1 | P1 |
| F3.4.3 Set construction booking | High | High | High | P1 | P1 | P1 | P2 | P1 | P1 | P1 | P1 | P1 | P1 |
| F3.4.4–F3.4.6 Staff tools, notifications, identification | High | Medium | High | P1 | P1 | P2 | P3 | P1 | P2 | P2 | P2 | P2 | P1 |
| F4.5.1 Booking payments | High | High | High | P1 | P1 | P1 | P2 | P1 | P2 | P1 | P1 | P1 | P1 |
| F4.5.2–F4.5.4 Sales checkout, refunds, reconciliation | High | Medium | High | P1 | P1 | P1 | P3 | P1 | P2 | P2 | P2 | P1 | P1 |

## 6. Feature-to-Test Traceability

Test names start with the PAGE-ID or task ID they verify ([strategy §3.3](testing-strategy.md#33-traceability)), so a search for an ID finds its tests. The journeys are the proposed ones in T1.7.1.1, numbered as listed there. "Page sweep" is the generated per-page check set ([strategy §4.3](testing-strategy.md#43-end-to-end-testing)). Status values: Not started · In progress · Passing · Failing · Blocked.

### 6.1 Phase 1

| Feature | Requirement source | Acceptance criteria | Planned automated tests | Planned manual checks | Status |
|---|---|---|---|---|---|
| F1.3.3 Locale routing and direction | overview §2.2; DEC-002 | T1.3.3.1 | `lang`/`dir` per locale (integration); switcher destinations (E2E, journey 4); overflow per viewport (page sweep) | RTL review on real devices | Not started |
| F1.3.3 Locale utilities and fonts | iran-constraints §6; DEC-015, DEC-023 | T1.3.3.2 | Table-driven unit tests; no external font requests (allowlist) | Typography review | Not started |
| F1.4.1, F1.4.2 Tokens and components | Figma component inventory | T1.4.1.1, T1.4.2.1 | Component tests in both locales; axe per component; visual baselines | Keyboard and screen reader checks of interactive components | Not started |
| F1.4.3 Site shell | Sitemap (T1.1.3.1) | T1.4.3.1–T1.4.3.3 | Navigation E2E; mobile menu keyboard and touch; 404 per locale | Device check of the mobile menu | Not started |
| F1.5.1 PAGE-001 | pages.md PAGE-001 | T1.5.1.1 | Page sweep; journeys 1 and 3 start here | Content proofreading; exploratory session | Not started |
| F1.5.2 PAGE-002 | pages.md PAGE-002 | T1.5.2.1 | Page sweep; price formatting (unit); links to service pages (E2E) | Price confirmation by the center | Not started |
| F1.5.3 PAGE-003 | pages.md PAGE-003; DEC-028 | T1.5.3.1 | Page sweep; set content schema validation (integration) | Content proofreading | Not started |
| F1.5.4 PAGE-004 | pages.md PAGE-004; DEC-001 | T1.5.4.1 | Page sweep; link to PAGE-014 (E2E, journey 5) | Content proofreading | Not started |
| F1.5.5 PAGE-010 | pages.md PAGE-010; DEC-004 | T1.5.5.1 | Page sweep; journey 1; course data validation (integration) | Course data confirmed by the center | Not started |
| F1.5.6 PAGE-013, 014 | pages.md PAGE-013, 014; DEC-001, DEC-003 | T1.5.6.1 | Page sweep; journey 5 | Purchase path reviewed by the center | Not started |
| F1.5.7 PAGE-006 | pages.md PAGE-006; DEC-013 | T1.5.7.1 | Page sweep; image viewer keyboard (component); image performance budget | Consent check of every identifiable child; screen reader check | Not started |
| F1.5.8 PAGE-007 | pages.md PAGE-007; DEC-011 | T1.5.8.1 | Page sweep | Content proofreading | Not started |
| F1.5.9 PAGE-008 | pages.md PAGE-008; DEC-010, DEC-022 | T1.5.9.1 | Page sweep; journey 2; `tel:` links (E2E) | Contact details and hours confirmed by the center; tap test on phones | Not started |
| F1.5.10 PAGE-009 | DEC-007 | T1.5.10.1 (blocked) | [TBD: after DEC-007] | [TBD: after DEC-007] | Blocked |
| F1.5.11 PAGE-011 | pages.md PAGE-011; DEC-009 | T1.5.11.1 | Page sweep; journey 3 | Request path reviewed by the center | Not started |
| F1.5.12 PAGE-012 | pages.md PAGE-012 | T1.5.12.1 | Page sweep; accordion keyboard (component); FAQ structured data matches visible FAQ (integration) | Screen reader check | Not started |
| F1.6.1 Map | overview §2.2; DEC-022 | T1.6.1.1 | Fallback when the provider fails (integration); lazy loading (performance); allowlist | Map loads on Iranian networks without VPN | Not started |
| F1.6.2 Request form | overview §1.6; DEC-009 | T1.6.2.1 | Validator partitions (unit); handler and delivery with fakes (integration); journey 3; rate limiting (security) | Real delivery to the test destination; spam probe | Not started (conditional) |
| F1.6.3 Analytics | overview §2.2; DEC-021 | T1.6.3.1 | Disabled on staging (integration); allowlist; performance budget | Data received from an Iranian network | Not started |
| F1.6.4 SEO, GEO | overview §2.2; DEC-008 | T1.6.4.1, T1.6.4.2 | Metadata per locale, canonical, hreflang reciprocity, sitemap, structured data (integration) | Search engine verification (T1.8.2.2) | Not started |
| F1.7.1 Automated testing | overview §2.2.2 | T1.7.1.1–T1.7.1.3 | Journeys 1–5 once confirmed; accessibility scan of every page and locale in CI | — | Not started |
| F1.7.2 Manual verification | overview §2.2; phase-1-mvp §7 | T1.7.2.1–T1.7.2.4 | — | Browser and device matrix; Iranian networks; manual accessibility; proofreading and acceptance | Not started |
| F1.7.3 Performance and security | overview §2.2; phase-1-mvp §7 | T1.7.3.1, T1.7.3.2 | Performance budgets in CI; header assertions; dependency and secret scanning; ZAP baseline on staging | Performance measured from an Iranian network | Not started |
| F1.3.4 CI | overview §2.2.1 | T1.3.4.1 | "Documentation links" job (exists); further checks as code appears (§14) | — | In progress (documentation check only) |
| F1.3.5, F1.8.1 Environments and production | DEC-018, DEC-019, DEC-020 | T1.3.5.1–T1.3.5.3, T1.8.1.1, T1.8.1.2 | Post-deploy smoke tests on staging and production | Rollback test; backup restore test | Not started |
| F1.8.3 Monitoring | — | T1.8.3.1 | Uptime checks from inside and outside Iran | Alert delivery test | Not started |

### 6.2 Phases 2–4 (Provisional)

| Feature | Acceptance criteria | Planned tests |
|---|---|---|
| F2.3.1 Album integration | T2.3.1.1, T2.3.1.2, T2.4.1.1 | Contract tests; E2E "visitor opens the album and sees set availability"; PWA installation on Android and iOS |
| F3.4.1–F3.4.3 Bookings | T3.4.1.1, T3.4.2.1, T3.4.3.1, T3.6.1.1 | Booking rule unit tests; concurrency integration tests (no overbooking); E2E per booking type; load tests |
| F3.4.4–F3.4.6 Staff tools, notifications, identification | Defined after T3.1.1.1, T3.2.1.1, T3.2.1.2 | [TBD: when the phase starts] |
| F4.5.1 Booking payments | T4.5.1.1, T4.6.1.1 | Sandbox E2E for success, cancellation, gateway failure, lost and duplicate callbacks, timeout; idempotency tests |
| F4.5.2–F4.5.4 Sales, refunds, reconciliation | Defined after DEC-031, T4.2.1.1 | [TBD: when the phase starts] |

## 7. Test Environments and Supported Browsers

### 7.1 Environments

Purpose and use of each environment: [strategy §7.1](testing-strategy.md#71-environments).

| Environment | Address | Status | Owner |
|---|---|---|---|
| Local | Developer machines (Windows) | Available for documentation checks; no application yet | [TBD: developers] |
| CI | GitHub Actions, repository `shn27sh/K-A-website` | Active: "Documentation links" job | [TBD: CI owner] |
| Preview (optional) | [TBD: DEC-018] | Not decided | [TBD] |
| Staging | [TBD: URL — DEC-018, T1.3.5.2] | Not set up | [TBD] |
| Production | [TBD: domain — DEC-019, T1.3.5.3] | Not set up | [TBD] |

### 7.2 Supported Browsers

Versions and support policy: phase-1-mvp §7 (DEC-024). This table defines **how** each browser is tested.

| Browser | Platform | Automated coverage | Manual coverage |
|---|---|---|---|
| Chrome for Android | Android | Chromium engine with mobile emulation, every pull request | Real mid-range and older Android devices |
| Samsung Internet | Android | None (not automatable with the proposed tools) | Real device |
| Safari | iOS, iPadOS | WebKit engine with mobile emulation, nightly | Real iPhone and iPad |
| Chrome | Desktop | Chromium, every pull request | Spot check |
| Edge | Desktop | Chromium, every pull request | Spot check |
| Firefox | Desktop | Firefox engine, nightly | Spot check |
| Safari | macOS | WebKit engine, nightly | Spot check on a Mac [TBD: availability — DEC-034] |

Older-version support is decided from market and analytics data (phase-1-mvp §7).

### 7.3 Devices, Viewports, and Networks

- **Automated viewports:** [strategy §4.8](testing-strategy.md#48-responsive-design-and-browser-compatibility-testing), replaced by the Figma breakpoints once defined (T1.2.1.2).
- **Physical devices:** [TBD: device list and owner — DEC-034]. The strategy's proposed manual device set is the starting point.
- **Iranian networks (without VPN):** T1.7.2.2 requires at least one mobile operator and one fixed-line ISP. Covering all three operators is proposed ([strategy §4.10](testing-strategy.md#410-iran-network-and-resilience-testing), DEC-034).
  - همراه اول: [TBD: tester — DEC-034]
  - ایرانسل: [TBD: tester — DEC-034]
  - رایتل: [TBD: tester — DEC-034]
  - fixed-line ISP: [TBD: ISP and tester — DEC-034]
- **Outside Iran:** [TBD: who checks reachability from abroad, relevant to DEC-002 and search crawlers].

## 8. Test Data and Account Management

**Test data** follows [strategy §7.2](testing-strategy.md#72-test-data): fixture content in both locales, a Persian edge-case corpus, fixture images without people, a fixed clock in `Asia/Tehran`, and synthetic personal and payment data in later phases.

**Rules for accounts and credentials**
- Every account has a named owner and the least privilege needed.
- Credentials live in GitHub Secrets (for CI) or [TBD: password manager — owner]. They never appear in the repository, test reports, screenshots, or defect reports.
- Staging access is restricted (T1.7.3.2). Test access is removed when it is no longer needed and rotated when people change roles.
- Tests never use production customer data or real payment cards. Form and notification tests send to dedicated test destinations, never to the center's real inbox or real visitors.
- Defect reports and screenshots never include identifiable children unless consent is recorded (DEC-013).

| Account or credential | Purpose | Phase | Storage | Owner | Status |
|---|---|---|---|---|---|
| GitHub repository and Actions | Code, CI, defect tracking (if approved, §12) | 1 | GitHub | [TBD] | Exists |
| CI secrets | None required today | — | GitHub Secrets | — | None |
| Staging access | Stakeholder review and testing | 1 | [TBD] | [TBD] | Not set up (T1.3.5.2) |
| Hosting provider console | Deployment, logs | 1 | [TBD] | [TBD] | Not decided (DEC-018) |
| Analytics administration | Verifying tracking | 1 | [TBD] | [TBD] | Not decided (DEC-021) |
| Map provider key, if any | Map integration | 1 | GitHub Secrets or host configuration | [TBD] | Not decided (DEC-022) |
| Form delivery test destination | Request form tests | 1 | [TBD] | [TBD] | Conditional (DEC-009) |
| Iranian SIM cards and ISP connections | Network testing without VPN | 1 | — | [TBD] | Not decided (DEC-034) |
| Test visitor and staff accounts | Booking tests | 3 | Seeded per test run | [TBD] | Not designed (T3.2.1.1) |
| SMS provider test mode | Notification tests | 3 | GitHub Secrets | [TBD] | Not decided (T3.2.1.2) |
| Gateway sandbox merchant credentials | Payment tests | 4 | GitHub Secrets | [TBD] | Not decided (DEC-030) |

## 9. Test Cycles: Entry and Exit Criteria

| Test cycle | When | Entry criteria | Exit criteria |
|---|---|---|---|
| 1. Continuous developer testing (static, unit, integration) | From S1.3, on every change | Application scaffolded (T1.3.2.1); test runners configured (DEC-025) | Gate G1 passes for every merged change |
| 2. Component and shell testing | S1.4 | Design foundations and components signed off (T1.2.1.2, T1.2.1.3); tokens implemented (T1.4.1.1) | Every inventory component tested in both locales; page sweep harness and visual baselines in CI |
| 3. Feature and page testing | S1.5–S1.6, per feature | Page design signed off (T1.2.2.3); approved content (T1.1.4.2); related decisions recorded | Gate G3 for each feature; traceability row status Passing |
| 4. System testing | S1.7 | Strategy entry criteria for S1.7 ([§11.1](testing-strategy.md#111-gates)); staging stable | Confirmed journeys pass in all engines; T1.7.1.1–T1.7.1.3 and T1.7.3.1–T1.7.3.2 complete; no open critical or high defects |
| 5. Iran network testing | S1.7, and before every production release | Staging deployed with the release candidate; testers and networks available (DEC-034) | T1.7.2.2 criteria met on every listed network; results recorded |
| 6. User acceptance testing | S1.7 | System testing exit met; final content on staging | Written sign-off by the center (T1.7.2.4) |
| 7. Production verification | S1.8, every release | Release readiness criteria met (§16); approval recorded | Production smoke tests pass from inside Iran; monitoring active; rollback tested once (T1.8.1.2) |
| 8. Post-launch monitoring | After each release | Production verification passed | Post-launch review held (T1.8.3.3); escaped defects triaged |

**Suspension and resumption**

| Suspend when | Resume when |
|---|---|
| Staging is unavailable or unreachable from Iran | Staging is reachable and the smoke tests pass |
| More than [TBD: number — QA lead] critical or high defects are open in the cycle | They are fixed and verified |
| The build under test differs from the release candidate | A new candidate is deployed, and affected tests are repeated |
| A blocking decision is unresolved (for example DEC-007 for PAGE-009) | The decision is recorded in `decisions.md` |

## 10. Test Schedule

No dates are set. Development stages have no dates yet, and Phases 2–4 are not scheduled (development-plan §6). Dates are added when S1.1 completes and each stage is planned. Test activities per stage: [strategy §14](testing-strategy.md#14-phased-implementation-roadmap).

| Stage | Test cycles | Key testing milestones | Start | End | Status |
|---|---|---|---|---|---|
| S1.1 Foundation and requirements | — | Strategy and this plan approved; core journeys confirmed | [TBD] | [TBD] | In progress |
| S1.2 UX and visual design | — | DEC-024 decided (by T1.2.1.2); accessibility and mirroring reviewed in design sign-off | [TBD] | [TBD] | Not started |
| S1.3 Technical foundation | 1 | DEC-025, DEC-033, DEC-034 decided; CI runs lint, types, unit tests, and build; staging smoke tests | [TBD] | [TBD] | Not started (documentation check active) |
| S1.4 Design system and shell | 1, 2 | Page sweep and visual regression in CI | [TBD] | [TBD] | Not started |
| S1.5 Page implementation | 1, 3 | Every page passes G3 | [TBD] | [TBD] | Not started |
| S1.6 Integrations, SEO, analytics | 1, 3 | Integration tests for map, form, analytics, SEO | [TBD] | [TBD] | Not started |
| S1.7 Quality assurance | 4, 5, 6 | System testing, Iran network testing, acceptance complete | [TBD] | [TBD] | Not started |
| S1.8 Launch in Iran | 7, 8 | Go/no-go decision; production verified | [TBD: MVP launch date] | [TBD] | Not started |
| Phase 2 | 1–8 as applicable | [TBD: DEC-027] | [TBD] | [TBD] | Not scheduled |
| Phase 3 | 1–8 as applicable | [TBD] | [TBD] | [TBD] | Not scheduled |
| Phase 4 | 1–8 as applicable | [TBD] | [TBD] | [TBD] | Not scheduled |

This plan is reviewed at the end of every stage and whenever a decision changes its scope.

## 11. Manual and Automated Testing Responsibilities

Team composition is not defined ([strategy §13.3](testing-strategy.md#133-open-questions)). Roles are listed; people are assigned when known.

| Role | Responsibilities | Assigned to |
|---|---|---|
| QA lead | Owns this plan; triage; test reports; release readiness recommendation | [TBD] |
| Developers | Write and maintain automated tests with the code; keep CI green; fix defects | [TBD] |
| Designer | Contrast, states, focus, RTL and LTR variants in Figma | [TBD] |
| Content owner (the center) | Confirms prices, hours, contact details, and media consent; acceptance sign-off | [TBD: DEC-014] |
| Iran network tester | Checks without VPN on Iranian networks and devices | [TBD: DEC-034] |
| Accessibility reviewer | Manual keyboard and screen reader checks in Persian | [TBD] |
| Release approver | Approves production releases | [TBD: T1.8.1.2] |

| Activity | Mode | Performed by | When |
|---|---|---|---|
| Static, unit, integration, component tests | Automated | Developers (write); CI (run) | Every pull request |
| Journeys and page sweep | Automated | Developers and QA lead (write); CI (run) | Every pull request; full matrix nightly |
| Visual regression baseline review | Automated with manual approval | Developers; reviewed in code review | When baselines change |
| Performance budgets; dependency and secret scanning | Automated | CI | Every pull request |
| ZAP baseline; staging smoke tests | Automated | CI or a runner inside Iran (DEC-020) | After each staging deployment |
| Exploratory testing with charters | Manual | QA lead | Per stage; before releases |
| Real devices and Samsung Internet | Manual | QA lead or Iran network tester | S1.7; before releases |
| Iranian networks without VPN | Manual or scripted | Iran network tester | S1.7; before every release |
| Screen reader testing | Manual | Accessibility reviewer | S1.7; after major UI changes |
| Proofreading and content confirmation | Manual | Content owner | S1.7; on content changes |
| Acceptance | Manual | Content owner | S1.7 |
| Go/no-go recommendation and decision | Manual | QA lead (recommends); release approver (decides) | Each production release |

## 12. Defect Management: Severity and Priority

**Severity** (impact of the defect): [strategy §11.2](testing-strategy.md#112-defect-severity-proposed). Critical and High block releases; Medium needs written acceptance.

**Priority** (order of fixing). **Proposed:**

| Priority | Meaning | Default for |
|---|---|---|
| Immediate | Fix before other work; hotfix if in production | Critical |
| High | Fix before the next release | High |
| Normal | Fix within the current stage | Medium |
| Low | Backlog; fix when convenient | Low |

Severity and priority can differ, with the reason recorded. For example, a Low-severity typo in the home page hero may get High priority. A Medium defect on an unreleased page may get Low priority until the page is scheduled.

**Lifecycle (Proposed):** New → Triaged → In progress → Fixed → Verified → Closed. A defect that fails verification returns to In progress (Reopened). A defect accepted for release with a written reason becomes Deferred.

**Defect report fields:**
- a title starting with the PAGE-ID or feature ID;
- environment and build;
- browser, device, and viewport;
- locale (fa or en);
- network, naming the Iranian operator or ISP and confirming the VPN was off;
- steps, expected result, actual result;
- evidence, following the rules in §8;
- severity and priority.

**Tracking (Proposed):** GitHub Issues with labels `defect`, `severity:critical|high|medium|low`, `priority:immediate|high|normal|low`, and the PAGE-ID. This depends on DEC-020 (§18). Triage cadence: [TBD: QA lead].

## 13. Regression Testing Policy

Regression methods: [strategy §4.4](testing-strategy.md#44-regression-testing).

| Trigger | Regression scope |
|---|---|
| Every pull request | Full automated fast suite: static checks, unit, integration, journeys and page sweep in Chromium, visual regression |
| Nightly | Full browser matrix, dependency audit, external link check, performance from Iran |
| Defect fix | A test that fails without the fix, plus the suite for the affected feature |
| Dependency or action update (Dependabot) | Full pull request suite |
| Content change (DEC-017) | Through a pull request: full suite. Outside pull requests: build-time validation, post-publish smoke tests, scheduled crawl |
| Release candidate | Full matrix; manual regression checklist for changed areas; Iran network checks |
| Hotfix | Smoke tests and the affected feature's suite before release; full suite afterwards |

Rules:
- A failing regression test is never skipped to release; it is fixed, or the defect is formally deferred (§12).
- Quarantined flaky tests follow [strategy §10.3](testing-strategy.md#103-test-suite-health) and are listed in the test report.
- Manual regression checklists live in `docs/testing/` (proposed in strategy §3.6) and are added when the first pages exist.

## 14. CI/CD Quality Gates

Gate definitions: [strategy §11.1](testing-strategy.md#111-gates). Pipeline: [strategy §8](testing-strategy.md#8-automation-and-cicd). A gate counts only when its checks actually run. A missing check is reported as **Not active**, never as passed.

| Gate | Checks today | Becomes fully active | Enforcement today |
|---|---|---|---|
| G1 Merge | "Documentation links" job only | When lint, types, tests, and build exist (T1.3.4.1, S1.3–S1.4) | Not enforced: branch protection on `main` is not configured (T1.3.4.1) |
| G2 Staging | Not active | When staging exists (T1.3.5.2) | — |
| G3 Feature done | Not active | First feature in S1.4–S1.5 | — |
| G4 Production release | Not active | First production release (S1.8) | — |
| G5 MVP launch readiness | Not active | End of S1.7 | — |

**Recommended (a repository setting, changed by the repository owner):** protect `main` and require the "Documentation links" check now. Add each new required check as it is introduced.

## 15. Test Reporting and Metrics

| Report | Content | Frequency | Audience | Location |
|---|---|---|---|---|
| CI results | Check status, annotations on changed lines, job summary, artifacts | Every run | Developers, reviewers | GitHub Actions |
| Stage test summary | Tests run, passed, failed, blocked; traceability status (§6); open defects by severity; risks | End of each stage | Project stakeholders | [TBD: e.g. `docs/testing/reports/`] |
| Release readiness report | Gate status, open defects, deferred items, Iran network results, recommendation | Each production release | Release approver | [TBD] |
| Post-launch report | Escaped defects, monitoring and analytics findings, actions | After each release (T1.8.3.3) | Project stakeholders | [TBD] |

| Metric | Definition | Target | Source |
|---|---|---|---|
| Requirement coverage | Share of §6 rows with planned tests in place and passing | 100% of in-scope rows before launch | §6 |
| Test execution | Passed, failed, blocked, not run, per cycle | No failed or blocked P1 tests at exit | CI and manual records |
| Open defects by severity | Count at each report | 0 critical and 0 high at release | Defect tracker |
| Defect arrival and closure | New against closed per week | Closure keeps pace before S1.7 exit | Defect tracker |
| Reopen rate | Share of fixed defects that fail verification | [TBD: target — QA lead] | Defect tracker |
| Escaped defects | Defects found in production | Each has a root cause and a regression test | Defect tracker |
| Pipeline duration and flaky rate | — | [Strategy §10.3](testing-strategy.md#103-test-suite-health) | CI |
| Code coverage | — | [Strategy §10.2](testing-strategy.md#102-coverage-targets) | CI |
| Product quality targets | Performance, accessibility, browsers | Phase-1-mvp §7 and [strategy §10.1](testing-strategy.md#101-product-quality-targets) | CI, manual checks |

Coverage is reported together with requirement coverage and escaped defects, because coverage alone does not show test quality ([strategy §10.4](testing-strategy.md#104-coverage-does-not-establish-test-quality)).

## 16. Release Readiness Criteria

### 16.1 MVP Launch Readiness (Gate G5, End of S1.7)

- [ ] All Phase 1 traceability rows (§6.1) Passing, or Blocked or Deferred with a recorded decision
- [ ] All P1 and P2 cells in the matrix (§5.1) covered by passing tests or completed checks; any P2 gap deferred in writing ([strategy §3.1](testing-strategy.md#31-risk-based-prioritization))
- [ ] T1.7.1.1–T1.7.1.3 automated testing complete and passing in CI
- [ ] T1.7.2.1 browser and device matrix passed
- [ ] T1.7.2.2 Iranian networks without VPN passed (at least one mobile operator and one fixed-line ISP)
- [ ] T1.7.2.3 manual accessibility review passed
- [ ] T1.7.3.1 performance and T1.7.3.2 security criteria met
- [ ] T1.7.2.4 acceptance signed off by the center
- [ ] No open critical or high defects; medium defects accepted in writing
- [ ] Release readiness report reviewed at a go/no-go meeting. Participants: [TBD]. Date: [TBD]

### 16.2 Go-Live (S1.8, Test Cycle 7)

- [ ] Production provisioned with SSL and backups; one restore tested (T1.8.1.1)
- [ ] Approval-based deployment and rollback tested (T1.8.1.2)
- [ ] Production smoke tests pass from inside Iran without VPN (T1.8.2.1)
- [ ] Monitoring active from inside and outside Iran (T1.8.3.1)

Phase 1 is complete when the phase-1-mvp §11 criteria are met, including production verification and handover.

### 16.3 Later Releases (Gate G4)

G4 criteria ([strategy §11.1](testing-strategy.md#111-gates)), Iran network checks on the release candidate (test cycle 5), and a recorded approval. Phases 2–4 add their phase completion criteria (phase-2-album §9, phase-3-booking §9, phase-4-payment §10).

## 17. Risks, Dependencies, and Mitigations

Testing risks in general: [strategy §12](testing-strategy.md#12-risks-and-mitigations). Risks specific to executing this plan:

| Risk | Impact | Mitigation | Related |
|---|---|---|---|
| No assigned QA lead or testers | Testing is skipped or done late | Assign the roles in §11 during S1.1 | §18 |
| Dates unknown; S1.7 compressed if earlier stages slip | Incomplete testing at launch | Test continuously from S1.3; G5 criteria are not reduced to meet a date | §10 |
| Content delivered late | Acceptance testing compressed; placeholder text at launch | Content inventory with due dates (T1.1.4.1); page testing needs approved content (§9) | DEC-014 |
| Pending decisions block test design | Tests written late or reworked | Track the blocking decisions in §17 dependencies; write stack-independent tests first | §18 |
| No access to Iranian networks or devices | Iran-specific failures found after launch | Decide DEC-034 early; scripted checks from a server in Iran | DEC-034 |
| Branch protection not enabled | Failing checks can still be merged | Enable it now for the existing check (§14) | T1.3.4.1 |

| Dependency | Needed for | Source | Status |
|---|---|---|---|
| Stack and testing tools | Test cycle 1 onward | DEC-016, DEC-025 | Pending |
| Quality targets | Exit criteria and gates | DEC-024 | Pending |
| Coverage targets | Gate G1 thresholds | DEC-033 | Pending |
| Testing access in Iran | Test cycle 5 | DEC-034 | Pending |
| Hosting, staging, deployment path | Test cycles 4, 5, 7 | DEC-018, DEC-020; T1.3.5.2 | Pending |
| English scope | Size of every test run | DEC-002 | Pending |
| Content management | Regression policy for content | DEC-017 | Pending |
| Request mechanism | F1.6.2 tests, security scope | DEC-009 | Pending |
| Map, video, analytics providers | Allowlist entries and fallback tests | DEC-022, DEC-011, DEC-021 | Pending |
| Signed-off designs | Visual baselines, test cycle 2–3 entry | T1.2.2.3 | Not started |
| Approved content | Test cycle 3 entry, acceptance | T1.1.4.2 | Not started |
| Confirmed core journeys | E2E scope | T1.7.1.1 | Proposed |

## 18. Assumptions and Open Questions

**Assumptions** (registered in development-plan §11): A-1 mostly mobile visitors in Iran; A-2 the center provides all content; A-3 frequent content changes; A-4 no personal data in the MVP except form submissions; A-6 mostly pre-rendered pages; A-7 GitHub hosts the repository and GitHub Actions runs CI. This plan adds no new assumptions. Unknowns are placeholders instead.

**Open questions**

| Question | Affects | Resolved by |
|---|---|---|
| Who fills the roles in §11? | Every test cycle | [TBD: project owner] |
| What are the stage dates and the MVP launch date? | §10 | S1.1 planning |
| Who approves production releases? | §11, §16 | T1.8.1.2 |
| Is GitHub Issues the defect tracker? | §12 | DEC-020 or approval of §12 |
| Which devices, SIM cards, and ISPs are available, and who tests from inside Iran? | §7.3, test cycle 5 | DEC-034 |
| Where are stage and release reports stored? | §15 | Approval of §15 |
| What suspension threshold and reopen-rate target apply? | §9, §15 | QA lead |
| Are older Android and iOS versions supported? | §7.2 | Phase-1-mvp §7; DEC-024 |
| Who checks reachability from outside Iran? | §7.3 | DEC-002; DEC-034 |

Further testing questions: [strategy §13](testing-strategy.md#13-open-questions-and-required-decisions).

## 19. Proposals Requiring Approval

Proposals shared with the strategy (tools, targets, pipeline, severity scheme): [strategy §15](testing-strategy.md#15-proposals-requiring-approval). Proposals added by this plan:

| # | Proposal | Section |
|---|---|---|
| 1 | Adopt this document as the master test plan | All |
| 2 | Risk rating method and the risk-based test matrix | §4, §5 |
| 3 | Test cycles with their entry, exit, and suspension criteria | §9 |
| 4 | Roles and the split of manual and automated responsibilities | §11 |
| 5 | Defect priority scale, lifecycle, report fields, and GitHub Issues as the tracker | §12 |
| 6 | Regression policy by trigger | §13 |
| 7 | Reports, metrics, and their targets | §15 |
| 8 | Release readiness checklist and go/no-go meeting | §16 |
| 9 | Enable branch protection on `main` requiring "Documentation links" (repository setting) | §14 |
