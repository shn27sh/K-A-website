# Development Plan — LEGO Center Website (K-A-website)

**Status:** Draft for review  
**Scope of this document:** Guide future design, implementation, Iran launch, and post-MVP work.  
**Sources:** This conversation; `docs/project/project-overview.md`; `docs/project/pages.md`; current repository state.

---

## 1. Project overview and objectives

This project is a **Persian/Farsi-first, RTL, responsive website** for a LEGO center where children construct LEGO sets. The site should help visitors understand the center, its offerings, atmosphere, facilities, educational approach, and related activities.

### 1.1 Stated product purposes

From `docs/project/project-overview.md`:

1. Present the center: what it is, who it is for, atmosphere, activities, facilities, educational approach and values.
2. Display activities and programs: ساخت لگو, کارگاه‌های رباتیک, competitions.
3. Booking and registrations (**Phase 3**): رزرو برای ساخت, events, workshops with available capacity.
4. Build trust with parents: safety, instructors, educational benefits, policies, photos, FAQs.
5. Promote the center community: children’s projects, events, competitions, achievements; encourage repeat visits.
6. Give schools, teachers, business owners, organizations, and مهدکودک‌ها a way to request group activities, educational programs, or special events.

### 1.2 Intended delivery workflow

1. Design pages in Figma.
2. Implement designs in this repository with Cursor.
3. Launch the website in Iran, with explicit attention to connectivity, hosting, payments (later phases), testing, and related operational constraints.

### 1.3 Target visitors

| Audience | Role | What they need (documented) |
|---|---|---|
| Parents | Primary | Activities, age suitability, educational benefits, cost, safety, class times, how to register |
| Schools, teachers, business owners, مهدکودک‌ها | Secondary | Extracurricular programs, group visits, workshops, partnership opportunities |
| Children and teenagers | Tertiary | LEGO, construction, creativity, tech; center LEGO sets, related videos, challenges |

### 1.4 Language and direction

**Decision from this conversation (not yet written into the existing docs):** the public site is **Farsi-first and RTL**.

**Conflict with existing docs:** `project-overview.md` lists **Bilingual** under MVP launch requirements. Whether a second language ships in Phase 1, later, or not at all is **unresolved**. Until decided, implementation should not assume a locale switcher or English content.

---

## 2. Current project state

### 2.1 What exists

The repository is **documentation-only**. There is no application source, package manifest, CI config, design-system code, README, or hosting configuration.

Current tree (excluding `.git`):

```
K-A-website/
└── docs/
    └── project/
        ├── pages.md
        └── project-overview.md
```

| Artifact | Role |
|---|---|
| `docs/project/project-overview.md` | Product purpose, MVP checklist, audiences |
| `docs/project/pages.md` | Page inventory with PAGE-001 … PAGE-016 and content bullets |

Git remote: `https://github.com/shn27sh/K-A-website.git`, branch `main`. History is documentation commits only.

### 2.2 What does not exist (do not treat as completed)

- No Figma files or design tokens in this repo
- No chosen technology stack
- No UI implementation
- No backend, APIs, database, or authentication
- No CI/CD pipelines or automated tests
- No Iran hosting, CDN, domain, analytics, or payment integration
- No documented contract with the existing album PWA
- No `development-plan.md` on disk until this draft is approved and saved

**Existing functionality vs planned work:** there is **no completed website functionality**. All implementation tasks below are new. Completed work is limited to early product documentation.

---

## 3. Requirements and expected functionality

### 3.1 Phase 1 — MVP (in scope for first launch)

**Goal:** Simple pages that showcase the center, offerings, main activities, atmosphere, facilities, and related aspects. Visitors discover the center; they do not book or pay online yet.

**MVP launch items documented in `project-overview.md` §2.2:**

- Pages
- Responsive design (including mobile and tablet)
- FAQ
- Location and map
- Basic SEO
- Simple navigation
- Social media links
- Good performance and fast loading
- Analytics
- CI/CD: automated validation and deployment so changes are tested before merge and approved changes deploy consistently
- Testing: unit/integration for critical functionality; E2E for core user journeys; basic responsive and accessibility checks; all tests run in CI before deploy

**Additional Phase 1 requirements from this conversation:**

- Farsi-first content and **RTL** layout
- Design in Figma first, then implement from those designs
- Launch in **Iran**, planning for connectivity, server infrastructure, testing, and related operational constraints
- Payment systems are **not** Phase 1; they belong to Phase 4, but Iran payment constraints should be **anticipated** so later work is not blocked by architecture choices

### 3.2 Phase 1 page inventory

Use `pages.md` as the sitemap. Phase assignment below is inferred from page content plus this conversation. Pages not labeled TBD in `pages.md` are treated as **candidates for Phase 1 content**, except آلبوم which this conversation assigned to Phase 2.

| Page ID | Page | Phase 1 expectation |
|---|---|---|
| PAGE-001 | صفحه اصلی | Hero, short intro, main activities, events (informational) |
| PAGE-002 | معرفی خدمات | Skills each activity develops; cost and discounts for larger sets; authenticity of LEGO sets |
| PAGE-003 | ساخت لگو | Introduce LEGO sets |
| PAGE-004 | کارگاه لگو بوست | Workshop intro |
| PAGE-006 | گالری | Venue photos, children’s builds, workshop photos |
| PAGE-007 | درباره ما | Origin, history, goals, educational approach, authentic sets, opening photos/video |
| PAGE-008 | تماس با ما | Address and map, contact channels, hours, social pages |
| PAGE-009 | کارن و کیانا | Dedicated page (content beyond “صفحه اختصاصی” not specified) |
| PAGE-010 | معرفی دوره‌های کارگاهی | Age categories, cost, capacity, duration, instructor background, dedicated videos — **display only**; live booking is Phase 3 |
| PAGE-011 | همکاری | Values (creativity, problem-solving, teamwork, hands-on learning); partnership models; contact / meeting-request form |
| PAGE-012 | پرسش‌های متداول | Age, prerequisites, level, what to bring, child safety |
| PAGE-013 | فروش | Purchase guidance (informational). Transactional checkout is Phase 4 |
| PAGE-014 | ست / خرید لگو بوست | See unresolved ID conflict in §11. Content relates to Boost sets / purchase guidance |

**Explicitly out of Phase 1 (labeled TBD in `pages.md`):**

| Page ID | Page | Notes |
|---|---|---|
| PAGE-005 | بازی‌سازی با سوپرماریو | Planned future enhancement |
| PAGE-015 | قطعه | LEGO pieces by part codes; planned future enhancement |

**Assigned to Phase 2 by this conversation:**

| Page ID | Page | Notes |
|---|---|---|
| PAGE-016 | آلبوم | Integrate existing PWA: set photos/specs, availability (free vs being built), predicted free time |

### 3.3 Phase 2 — آلبوم

An **existing separate PWA** already shows the center’s LEGO sets (categories, age groups, brick counts, other details) and availability. Phase 2 integrates that project **into a page of this website** (PAGE-016). How integration works (embed, rewrite, shared API, iframe, subdomain) is **unresolved**.

### 3.4 Phase 3 — Booking

Add booking for:

- Events
- Workshops (including viewing available capacity)
- Set construction appointments (رزرو برای ساخت)

Users reserve spots and book building appointments. No booking system exists in this repo.

### 3.5 Phase 4 — Payment

Secure payment for:

- Bookings (workshops and set construction)
- Purchases and sales through the platform

Iran-specific payment systems are required and must be planned carefully. No payment implementation exists.

### 3.6 Requirements that are named but not specified

These appear in docs or conversation but lack enough detail to implement without later decisions:

- Exact copy, imagery, and Figma layouts
- Exact bilingual policy
- Analytics product
- Map provider (must work for users in Iran)
- CMS vs static content
- Domain, TLS, and Iranian hosting vendor
- Album PWA location, stack, and integration method
- Whether PAGE-010 “ظرفیت” is static copy in MVP or live data (live capacity belongs with Phase 3)
- Whether PAGE-013/014 are marketing-only in MVP

Do not invent answers for these in implementation sessions.

---

## 4. Technical architecture and repository structure

### 4.1 Current architecture

None. The repo holds planning documents only.

### 4.2 Architecture decisions that are deferred (do not invent)

From this conversation: **technology stack and tools will be chosen when those decisions become necessary.** This plan therefore does **not** prescribe Next.js, WordPress, a CMS, a database, or a specific host.

When the stack is chosen, record it in this document (or a sibling architecture note) **before** large-scale implementation.

### 4.3 Constraints the future stack must satisfy

These are requirements, not product choices:

| Constraint | Why |
|---|---|
| Farsi typography and **RTL** as the default layout direction | Conversation requirement |
| Responsive layouts matching Figma (mobile, tablet, desktop) | MVP + conversation |
| Suitable for launch and operation **in Iran** (hosting, DNS, TLS, likely blocked third-party CDNs/fonts/analytics/maps) | Conversation requirement |
| Fast loading on typical Iranian connectivity | MVP “good performance” + Iran context |
| Ability to add آلبوم (Phase 2), booking (Phase 3), and Iranian payment (Phase 4) without a full rewrite | Stated post-MVP expansion |
| Automated tests and deploy in CI | `project-overview.md` §2.2.1–2.2.2 |
| Designs originate in Figma and are implemented in code | Conversation workflow |

### 4.4 Iran launch (cross-cutting architecture)

This is a first-class concern, not a deploy afterthought. Before coding, document (in a later dedicated note if needed) at least:

- Where HTML/CSS/JS and media will be hosted (Iran vs abroad vs hybrid)
- Which third-party services are unreliable or blocked from inside Iran (common examples to **evaluate**, not prescribe: Google Fonts, Google Maps, Google Analytics, international CDNs)
- Fonts: how Farsi webfonts will be self-hosted or otherwise delivered
- Images/video: size, formats, and hosting that remain reachable
- Map on PAGE-008: a provider that works for visitors in Iran
- Analytics that work in Iran and satisfy “Analytics” in the MVP list
- How CI (likely GitHub today) relates to production servers that Iranian users actually hit
- How production will be tested **from inside Iran**, not only from outside
- Payment (Phase 4): Iranian gateways and legal/operational constraints; do not wire a foreign processor as the default path

**Unresolved:** no hosting, DNS, CDN, or monitoring vendor is chosen.

### 4.5 Expected future repository shape (illustrative only)

Do not create this structure until implementation starts. A later stack decision should define the real tree. Documentation should remain the source of product truth:

```
docs/project/
  project-overview.md
  pages.md
  development-plan.md          # this document, after approval
```

Application folders, Figma export locations, and infra config are **not** defined yet.

### 4.6 Backend, APIs, database, authentication

| Phase | Backend need (from known requirements) |
|---|---|
| Phase 1 | Not specified. Content may be static. PAGE-011 needs a **contact / meeting-request form**; delivery mechanism (email, form backend, third-party) is **unresolved**. |
| Phase 2 | Depends on the existing PWA (unknown stack). May need an API for set inventory and availability. |
| Phase 3 | Booking data, capacity, appointments — requires persistence and likely auth for staff and/or users. Not designed. |
| Phase 4 | Payment callbacks, order records, security controls. Not designed. |

Do not build a generic auth/admin platform in Phase 1 unless a later explicit decision requires it.

---

## 5. Features and development tasks

**Convention:** every task below is **planned**. Nothing in the application layer is “existing.”

For each major task: purpose, expected outcome, relevant files (when identifiable), dependencies, acceptance criteria.

### Task 0 — Align product docs before design/build

**Purpose:** Remove contradictions so Figma and code do not lock in the wrong IA.  
**Expected outcome:** `pages.md` and `project-overview.md` match the phased roadmap and language policy.  
**Relevant files:** `docs/project/pages.md`, `docs/project/project-overview.md` (and this plan after approval).  
**Dependencies:** Product decisions listed in §11.  
**Acceptance criteria:**

- PAGE-014 is unique (or the two Boost/sales concepts have distinct IDs).
- Each page has a phase: MVP, Phase 2, Phase 3, Phase 4, or TBD.
- Bilingual vs Farsi-first is stated in one place and not contradicted.
- PAGE-016 is labeled Phase 2.
- Booking/payment are not implied as Phase 1 page flows.

### Task 1 — Iran launch constraints brief

**Purpose:** Prevent stack and third-party choices that fail for users in Iran.  
**Expected outcome:** A written constraints list (hosting, fonts, maps, analytics, CI-to-prod, in-country testing, later payments). May live in this plan’s §4.4 or a future sibling doc — **file not created until requested**.  
**Dependencies:** None.  
**Acceptance criteria:** Each MVP third-party need (map, analytics, fonts, media, hosting) has an Iran-reachable option or an explicit “undecided, evaluate X vs Y.”

### Task 2 — Figma design for Phase 1 pages

**Purpose:** Design RTL, Farsi-first, responsive screens before code.  
**Expected outcome:** Figma frames for all Phase 1 pages (table in §3.2), covering mobile, tablet, and desktop; shared navigation/footer; states for empty gallery if needed; contact and cooperation forms.  
**Relevant files:** None in repo today.  
**Dependencies:** Task 0 recommended; content/assets from the center.  
**Acceptance criteria:**

- Default `dir` is RTL; Farsi type is specified.
- PAGE-001 through Phase 1 set are designed (excluding PAGE-005, PAGE-015, PAGE-016 unless stubs are explicitly requested).
- Breakpoints cover mobile and tablet as required by MVP.
- Visual language is consistent across pages.
- No booking checkout or payment UI in Phase 1 screens unless marked “future.”

### Task 3 — Choose stack, tooling, and repo layout

**Purpose:** Enable implementation, CI, and Iran-compatible hosting.  
**Expected outcome:** Recorded decision: rendering model (static vs server), CSS approach, hosting, CI, test runner.  
**Dependencies:** Tasks 1–2 strongly recommended so choices fit design and Iran constraints.  
**Acceptance criteria:** Decision is written; hello-world deploy path to the intended Iran-facing host is identified; Farsi/RTL and static assets are feasible.

### Task 4 — Project bootstrap

**Purpose:** Create the implementable app from the chosen stack.  
**Expected outcome:** Runnable local project, lint/format, RTL/Farsi baseline (document `dir`/`lang`), placeholder routes for Phase 1 pages.  
**Relevant files:** Not present yet.  
**Dependencies:** Task 3.  
**Acceptance criteria:** Local run works; `lang` appropriate for Farsi; default layout is RTL; Phase 1 routes exist as shells.

### Task 5 — Shared chrome: navigation, footer, social links

**Purpose:** MVP “simple navigation” and “social media links.”  
**Dependencies:** Tasks 2 and 4.  
**Acceptance criteria:** All Phase 1 pages share nav/footer; social links match PAGE-008 sources; active page is clear; usable on mobile (e.g. RTL-aware menu). Destination URLs may be placeholders if the center has not provided them — placeholders must be listed as such.

### Task 6 — Implement Phase 1 pages from Figma

Implement only pages in the Phase 1 table. Suggested order (homepage first, then trust/contact, then programs, then secondary):

1. PAGE-001 صفحه اصلی  
2. PAGE-008 تماس با ما (map, hours, social — high-trust)  
3. PAGE-012 پرسش‌های متداول  
4. PAGE-002 / PAGE-003 / PAGE-004 خدمات and LEGO / Boost  
5. PAGE-010 دوره‌های کارگاهی (static info)  
6. PAGE-006 گالری  
7. PAGE-007 درباره ما  
8. PAGE-009 کارن و کیانا  
9. PAGE-011 همکاری + form  
10. PAGE-013 / PAGE-014 sales guidance only, after ID conflict is resolved  

**Purpose:** Match Figma and `pages.md` bullets.  
**Expected outcome:** Responsive RTL pages with the documented sections.  
**Dependencies:** Tasks 2, 4, 5; real copy/media or clearly labeled placeholders.  
**Acceptance criteria (per page):**

- Documented sections from `pages.md` are present (or an explicit content gap is noted).
- Layout matches the approved Figma frame at the designed breakpoints.
- No live booking or payment.
- PAGE-005, PAGE-015, PAGE-016 are not built as full features in Phase 1 (optional “coming soon” only if product asks).

### Task 7 — Contact and cooperation forms

**Purpose:** PAGE-011 meeting request; PAGE-008 contact channels. Whether PAGE-008 includes a form is **not specified** — only address, map, channels, hours, social.  
**Dependencies:** Task 3 (how forms are submitted); Task 6.  
**Acceptance criteria:** Cooperation form can be completed in Farsi; submission path is documented; user sees success or error; no spam-open relay of secrets in the client. Exact fields are **unspecified** beyond the partnership intent.

### Task 8 — Map, SEO, analytics, performance baseline

**Purpose:** MVP location/map, basic SEO, analytics, fast loading.  
**Dependencies:** Task 1 (Iran-reachable vendors); Task 6.  
**Acceptance criteria:**

- PAGE-008 shows address and a map that is usable from Iran (provider decided in Task 1).
- Each Phase 1 page has appropriate `lang`, title, and basic meta description (copy source **unspecified** — use approved Farsi content when provided).
- Analytics loads from an Iran-reachable solution or fails gracefully.
- Performance: document a target after stack choice; at minimum, heavy images are sized for mobile and not loaded from blocked CDNs.

### Task 9 — CI/CD and automated tests (Phase 1)

**Purpose:** `project-overview.md` §2.2.1–2.2.2.  
**Dependencies:** Task 4; enough pages to test journeys.  
**Acceptance criteria:**

- CI runs on the main collaboration branch before merge.
- Automated checks include: build; unit/integration for any critical logic (forms, nav); E2E for core journeys (open home, navigate to contact, open FAQ, submit cooperation form if present).
- Basic responsive and accessibility checks run in CI.
- Deployment happens only after those checks pass, to the environment Iranian users will use.

### Task 10 — Phase 1 launch in Iran

**Purpose:** Production site reachable, tested, and operable inside Iran.  
**Dependencies:** Tasks 1, 6–9.  
**Acceptance criteria:**

- HTTPS site serves Phase 1 pages from a host reachable in Iran.
- In-country (or in-country-representative) checks of home, contact/map, gallery media, and fonts.
- Monitoring/analytics receiving data (or a documented exception).
- Rollback or republish path is known.

### Task 11 — Phase 2 آلبوم integration (after MVP)

**Purpose:** PAGE-016 via the existing PWA.  
**Dependencies:** MVP launched or stable; access to the PWA repo/API (not in this repository today).  
**Acceptance criteria:** Users can see set photos and specs (categories, age, element counts, other existing PWA details), availability (آزاد vs در حال ساخت), and predicted free time; presented as a page of this site. Method is whatever is later decided — do not assume a rewrite.

### Task 12 — Phase 3 booking

**Purpose:** Reserve events, workshops (with capacity), and ساخت appointments.  
**Dependencies:** Phase 2 optional; needs data model and likely staff tooling — **undesigned**.  
**Acceptance criteria:** User can see capacity and complete a reservation for the three booking types documented. Auth and admin UX are **unspecified**.

### Task 13 — Phase 4 payment

**Purpose:** Pay for bookings and platform sales.  
**Dependencies:** Phase 3; Iranian payment provider decision.  
**Acceptance criteria:** Documented booking types and in-scope sales can be paid through a secure Iranian-capable flow. PCI/legal details **unspecified**.

---

## 6. Implementation phases and recommended task order

```
Task 0  Docs alignment
Task 1  Iran constraints brief
Task 2  Figma (Phase 1)
Task 3  Stack + hosting decision
Task 4  Bootstrap
Task 5  Nav/footer
Task 6  Phase 1 pages (order in Task 6)
Task 7  Forms
Task 8  Map, SEO, analytics, performance
Task 9  CI/CD + tests
Task 10 Iran launch
—— MVP freeze ——
Task 11 آلبوم
Task 12 Booking
Task 13 Payment
```

Do not implement Phase 2–4 UI as if they were MVP. Optional footer links to “coming later” are a product choice, not a requirement.

---

## 7. UI/UX, responsive design, accessibility, and browser compatibility

### 7.1 UI/UX

- Figma is the visual source of truth for Phase 1.
- Content outlines live in `pages.md`.
- Default experience is Farsi and RTL (conversation).
- Parents are the primary audience: cost, age, safety, schedule, and trust content should be easy to find (overview §3.1).
- PAGE-009 (“کارن و کیانا”) has no UX spec beyond a dedicated page.

### 7.2 Responsive design

MVP requires responsive design plus mobile and tablet. Desktop is implied by a public website and Figma workflow but not named as its own bullet. Implement all three if Figma provides them; if Figma omits a breakpoint, treat that as a design gap, not a silent guess.

### 7.3 Accessibility

`project-overview.md` requires **basic** accessibility checks in CI. No WCAG level is specified. Minimum verifiable bar unless later specified:

- Valid heading structure
- Form labels
- Visible focus
- Alt text for meaningful images
- Keyboard access to navigation and forms
- Sufficient contrast as designed in Figma
- RTL does not break reading order or focus order

### 7.4 Browser compatibility

Not specified in the repo. **Assumption (labeled):** reasonably current mobile and desktop browsers used in Iran (Chromium-based, Firefox, Safari). Do not assume Google-only APIs.

---

## 8. Testing, validation, and quality assurance

Phase 1 quality bar (from overview + conversation):

| Layer | What to validate |
|---|---|
| Unit / integration | Critical logic only (likely forms, any content helpers). There is no domain logic yet. |
| E2E | Core journeys: home → activities/services → FAQ → contact; cooperation form submit |
| Responsive | Mobile and tablet (and desktop once designed) |
| Accessibility | Basic checks in CI |
| Iran | Fonts, map, media, analytics, and host reachable from inside Iran |
| Visual | Implementation vs Figma |

No test framework is chosen. Choose it in Task 3.

---

## 9. Performance, security, and maintainability

### 9.1 Performance

MVP requires good performance and fast loading. No numeric budget exists. After stack choice, set budgets (e.g. image weight, font strategy). Prefer self-hosted or Iran-reachable assets over blocked third-party CDNs.

### 9.2 Security (Phase 1)

Applicable even without accounts:

- HTTPS in production
- Safe form handling (no open mail relays; server-side validation when a backend exists)
- No secrets in the client or git
- Dependency hygiene once a package manager exists

Auth, booking abuse, and payment security apply in Phases 3–4 and are not designed.

### 9.3 Maintainability

- Keep `pages.md` / `project-overview.md` / this plan in sync when IA changes.
- Do not encode Phase 3–4 domain models into Phase 1 static pages beyond informational content.
- Prefer a content approach that the team can update (unspecified: markdown, CMS, or code).

---

## 10. Risks, unresolved questions, assumptions, and technical debt

### 10.1 Risks

| Risk | Why it matters |
|---|---|
| Blocked third-party fonts, maps, analytics, or CDNs | Pages look broken or unusable in Iran |
| Hosting abroad with poor connectivity | Misses MVP performance and launch-in-Iran goal |
| Designing booking/payment into MVP | Scope creep; contradicts stated phases |
| Duplicate PAGE-014 | Wrong sales/Boost IA in Figma |
| Unknown album PWA architecture | Phase 2 may force a rewrite if Phase 1 is inflexible |
| Bilingual vs Farsi-only mismatch | Duplicate layouts and delayed launch |
| Content/media not ready | Cannot finish gallery, about, or Boost pages |
| Form backend undecided | PAGE-011 cannot be completed |

### 10.2 Unresolved questions

1. Is Phase 1 Farsi-only, or bilingual as in `project-overview.md`?
2. How is PAGE-014 duplicated resolved?
3. What is PAGE-009 (کارن و کیانا) — characters, founders, or something else?
4. Are PAGE-013/014 in MVP as guides only, or delayed until Phase 4?
5. Should PAGE-016 appear in Phase 1 nav as “coming soon”?
6. What is the album PWA’s repo, stack, and integration method?
7. Which Iranian host, domain, DNS, and TLS setup?
8. Which map and analytics tools?
9. How does the PAGE-011 form get delivered?
10. Is there a CMS in Phase 1?
11. What is the WCAG target, if any, beyond “basic”?
12. What are Core Web Vitals or other numeric performance targets?
13. Exact Figma file location and handoff rules (Dev Mode, tokens, assets)?
14. Who supplies legal copy (policies mentioned under parent trust)?
15. Phase 3: guest vs account booking? Staff admin?
16. Phase 4: which Iranian PSP, and which products are sold?

### 10.3 Assumptions (used only where the repo is silent)

- No website code exists; all implementation is new.
- Phase 1 is content/marketing; not booking or payment.
- PAGE-010 capacity/cost in MVP is **editorial**, not a live inventory API.
- PAGE-005 and PAGE-015 stay out of MVP as labeled TBD.
- Stack remains unchosen until Task 3.
- “Competitions” and “رباتیک” in the overview appear on home/services as the design dictates; they do not have their own PAGE-IDs.
- GitHub remains the collaboration remote unless changed.

### 10.4 Technical debt

None in application code. Documentation debt:

- Typos in overview (`Loacation`, `Achivements`, `valiadation`, `deployement`, `ctitical`, `Oweners`, `Partnershop`, etc.)
- Inconsistent `Page ID` formatting in `pages.md`
- Typo «قعطه» under PAGE-015
- Phase labels missing on most pages
- Iran launch and album/payment/booking not represented in the two existing docs

---

## 11. Completion criteria and definition of done

### 11.1 Phase 1 (MVP) is done when

1. Figma for Phase 1 pages is approved by the project owner.
2. All Phase 1 pages in §3.2 are implemented to those designs, Farsi-first and RTL, responsive on mobile and tablet (and desktop if designed).
3. Documented MVP capabilities exist: FAQ, location and map, basic SEO, simple navigation, social links, analytics (or a written exception), performance acceptable on a representative Iran connection.
4. PAGE-005, PAGE-015, and full آلبوم/booking/payment are **not** required.
5. CI validates build, basic a11y/responsive checks, and E2E core journeys before deploy.
6. Production is launched and smoke-tested for Iranian reachability (fonts, map, media, forms).
7. Known placeholders (missing photos, social URLs, copy) are listed, not silently omitted.

### 11.2 Later phases

- **Phase 2 done:** PAGE-016 shows set specs and availability from the existing PWA capability, as a page of this site.
- **Phase 3 done:** Users can book events, workshops (with visible capacity), and ساخت appointments.
- **Phase 4 done:** Those bookings and in-scope sales can be paid through a secure, Iran-appropriate payment flow.

### 11.3 Definition of done for a single implementation session

- Only tasks from the agreed phase
- No new undocumented pages or stack changes
- Matches Figma and `pages.md` for the pages touched
- Does not invent copy, APIs, or Iran vendors
- Leaves docs updated if IA or decisions changed
- Does not start the next phase unless explicitly requested

---

## 12. Out of scope for the next implementation session

This plan itself is **not** an instruction to implement. After approval it should be saved as `docs/project/development-plan.md` only. Coding, Figma work, stack selection, and doc fixes happen only when separately requested.
