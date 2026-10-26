# Phase 2 — آلبوم (Album)

> **Status:** Not scheduled (post-MVP) · **Last updated:** 2026-10-26
> Roadmap: [development-plan.md](../development-plan.md) · Decisions: [decisions.md](../project/decisions.md) · Constraints: [iran-constraints.md](../project/iran-constraints.md) · Testing: [testing-strategy.md](../testing/testing-strategy.md)

## 1. Purpose

A Progressive Web App (PWA) serving as a digital album of the LEGO sets owned by the center, showing their specifications and availability. It is developed as a separate, independent project and integrated into a page of this website (PAGE-016).

## 2. Confirmed Requirements

| Requirement | Source |
|---|---|
| Developed independently as a PWA | Conversation (2026-10-18) |
| List of the center's LEGO sets with photos and set information | pages.md PAGE-016 |
| Specifications such as categories, age groups, number of elements (bricks), and other details | Conversation |
| Availability at any time: available to build (آزاد) or currently being built (در حال ساخت) | Conversation; pages.md PAGE-016 |
| Prediction of when a set becomes free | pages.md PAGE-016 |
| Integrated into a page of this website (PAGE-016) | Conversation; pages.md |

## 3. Scope

- **This repository:** integrating the album into PAGE-016 and related website changes (navigation, links from PAGE-003).
- **Album project:** the album itself. Its specifications will live in that project's documentation and be linked here once it exists.
- **Out of scope:** reserving a set (Phase 3), even though the album shows availability.

## 4. Pending Decisions and Open Questions

| Topic | Question | Tracking |
|---|---|---|
| Timeline | When does the album project start, relative to Phases 1 and 3? | DEC-027 |
| Integration | Link, subdomain, embedding, shared components, or consuming an API? | DEC-027 |
| Set data | One source of set data for PAGE-003, the album, and Phase 3 set booking? | DEC-028 |
| Availability source | Who updates the status, how, and how current it must be | Open (promote to DEC when the phase starts) |
| Predicted free time | What the prediction is based on | Open |
| Stack, architecture, hosting | Undetermined | Album project |
| Languages | Persian only or Persian/English? | Open |
| PWA expectations | Installability, offline behavior | Open |
| Data maintenance | Who maintains the set catalog | Open |

## 5. Dependencies and Constraints

- Phase 1 website in production (PAGE-016 lives in it).
- Progress of the album project.
- Iran constraints: hosting reachable in Iran, no runtime dependency on foreign resources. A PWA is attractive in Iran because native app-store distribution is constrained for Iranian developers (verify the current situation); iOS installation goes through Safari's "Add to Home Screen".

## 6. Expected Outcomes

Visitors open the album from the website, browse the center's sets with their specifications, and see whether each set is available or being built.

## 7. Stages (Provisional)

| Stage | Objective |
|---|---|
| S2.1 Definition | Detailed requirements, integration contract, data ownership, PAGE-IDs |
| S2.2 Album Project Delivery | Album built in its own project (tracked there) |
| S2.3 Website Integration | PAGE-016 integration in this repository |
| S2.4 QA & Release | Verification and release |

## 8. Features, Development Tasks, and Subtasks

Provisional. Detailed when the phase starts.

### S2.1 — Definition

#### F2.1.1 — Requirements and Integration Contract

##### T2.1.1.1 — Detail the album requirements
- **Purpose:** Turn §2 into a complete specification.
- **Outcome:** A requirements document (in the album project, linked here).
- **Acceptance criteria:** Each confirmed requirement specified in detail; open questions in §4 decided or registered as DECs.

##### T2.1.1.2 — Decide the integration method
- **Outcome:** DEC-027 decided.
- **Acceptance criteria:** Decision defines URL and navigation, visual consistency (RTL, branding), performance impact, hosting in Iran, and responsibility boundaries between the two projects.

##### T2.1.1.3 — Decide set data ownership
- **Outcome:** DEC-028 decided.
- **Acceptance criteria:** One documented owner and format for set data; PAGE-003 and Phase 3 implications described.

##### T2.1.1.4 — Update `pages.md`
- **Acceptance criteria:** PAGE-016 details updated; any new pages added with new PAGE-IDs.

### S2.2 — Album Project Delivery

Features below define the requirements interface with the album project. Their tasks and subtasks are defined in that project's documentation.

- **F2.2.1 — Set catalog:** list of sets with photos and information.
- **F2.2.2 — Set specifications:** categories, age groups, number of elements, other details (to be defined).
- **F2.2.3 — Availability status:** available to build or being built, current at any time.
- **F2.2.4 — Predicted free time:** estimate of when a set becomes free.
- **F2.2.5 — PWA capabilities:** to be defined (§4).

### S2.3 — Website Integration

#### F2.3.1 — PAGE-016 Integration

##### T2.3.1.1 — Implement the integration
- **Depends on:** T2.1.1.2, S2.2
- **Acceptance criteria:** The album is reachable from the website navigation and PAGE-003 (per the updated sitemap); consistent with the website's RTL layout and branding; works in Iran without VPN; all existing website tests still pass.

##### T2.3.1.2 — Add integration tests
- **Acceptance criteria:** E2E journey "visitor opens the album from the website and sees set availability" runs in CI.

### S2.4 — QA & Release

#### F2.4.1 — Release

##### T2.4.1.1 — Verify on Iranian networks and devices
- **Acceptance criteria:** Album and integration verified without VPN on mobile and fixed networks; PWA installation checked on Android and iOS.

##### T2.4.1.2 — Release and update documentation
- **Acceptance criteria:** Released to production; development plan and `pages.md` updated.

## 9. Completion Criteria (Provisional)

- [ ] All confirmed requirements in §2 available to visitors through PAGE-016
- [ ] Integration verified from inside Iran without VPN
- [ ] Decisions DEC-027 and DEC-028 recorded
