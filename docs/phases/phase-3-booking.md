# Phase 3 — Booking

> **Status:** Not scheduled (post-MVP) · **Last updated:** 2026-10-26
> Roadmap: [development-plan.md](../development-plan.md) · Decisions: [decisions.md](../project/decisions.md) · Constraints: [iran-constraints.md](../project/iran-constraints.md) · Testing: [testing-strategy.md](../testing/testing-strategy.md)

## 1. Purpose

Add a booking system for events, workshops, and set construction (رزرو برای ساخت).

## 2. Confirmed Requirements

| Requirement | Source |
|---|---|
| Reserve spots at events | overview §1.3; conversation |
| Reserve spots at workshops | overview §1.3; conversation |
| View available workshop capacity (نمایش ظرفیت خالی) | overview §1.3; conversation |
| Book building appointments (رزرو برای ساخت) | overview §1.3; conversation |

## 3. Scope

- **In scope:** the requirements in §2 and their integration into existing pages (PAGE-010 capacity, booking entry points, events per DEC-005).
- **Out of scope:** online payment (Phase 4), unless DEC-029 decides otherwise.
- **PAGE-IDs:** to be defined in `pages.md` (T3.1.1.3).

## 4. Open Questions

To be promoted to DECs when the phase starts:

- **User identification:** accounts, guest booking, or phone-number verification; does a parent book on behalf of a child?
- **Booking rules:** capacity limits, waiting lists, cancellation and rescheduling, deadlines, no-shows.
- **Set construction booking:** booked per set (requires set availability — DEC-028) or per time slot?
- **Staff tools:** how staff manage events, workshops, slots, and capacity, and view bookings.
- **Notifications:** confirmations and reminders by SMS (Iranian providers), messaging apps, or email.
- **Payment before Phase 4:** free reservation, payment at the center, or other (DEC-029).
- **Personal data:** which data about children is collected, where it is stored (Iran), and retention.
- **Calendar:** Solar Hijri dates, Asia/Tehran time zone, Iranian holidays, center working hours.
- **Architecture:** backend, database, authentication; relation to the Phase 1 stack (DEC-016) and the album.
- **Languages:** booking in Persian only or Persian/English?

## 5. Dependencies and Constraints

- Phase 1 website in production.
- Architecture decisions (S3.2).
- Set data (DEC-028) for set-construction booking; events placement (DEC-005).
- Iran constraints: SMS providers, Iran-hosted data storage, localization ([iran-constraints.md §6–7](../project/iran-constraints.md)).

## 6. Expected Outcomes

Visitors can reserve event and workshop spots and building appointments online; workshop capacity is shown from live data; staff can manage bookings (scope pending).

## 7. Stages (Provisional)

| Stage | Objective |
|---|---|
| S3.1 Requirements Definition | Resolve open questions; booking rules; PAGE-IDs |
| S3.2 Architecture | Backend, database, identification, notifications, data protection |
| S3.3 UX Design (Figma) | Booking flows for each booking type |
| S3.4 Implementation | Booking features |
| S3.5 Website Integration | Connect booking to existing pages |
| S3.6 QA & Security | Testing, security, Iranian network verification |
| S3.7 Launch | Release and operations |

## 8. Features, Development Tasks, and Subtasks

Provisional. Features marked *candidate* are likely needed but require confirmation.

### S3.1 — Requirements Definition

#### F3.1.1 — Booking Requirements

##### T3.1.1.1 — Resolve open questions
- **Outcome:** Questions in §4 recorded as decided DECs, including DEC-029.
- **Acceptance criteria:** Every §4 question decided or explicitly deferred.

##### T3.1.1.2 — Document booking rules
- **Acceptance criteria:** Rules for capacity, cancellation, rescheduling, deadlines, and no-shows documented for each booking type and approved by the center.

##### T3.1.1.3 — Define PAGE-IDs and user flows
- **Acceptance criteria:** New pages added to `pages.md` with Phase 3; a user flow documented for each booking type.

### S3.2 — Architecture

#### F3.2.1 — Booking Architecture

##### T3.2.1.1 — Decide backend, database, and user identification
- **Acceptance criteria:** Decision recorded with rationale; hosted in Iran; compatible with Phase 4 payment integration.

##### T3.2.1.2 — Decide the notification provider
- **Acceptance criteria:** Provider chosen and tested for delivery to Iranian mobile numbers.

##### T3.2.1.3 — Define the data protection approach
- **Acceptance criteria:** Collected data minimized and documented; storage location, access, and retention defined.

### S3.3 — UX Design

#### F3.3.1 — Booking Flows Design

##### T3.3.1.1 — Design the booking flows
- **Acceptance criteria:** Mobile-first designs for each booking type and for staff tools (if in scope), using the Phase 1 design system; signed off.

### S3.4 — Implementation

#### F3.4.1 — Event Booking

##### T3.4.1.1 — Implement event booking
- **Acceptance criteria:** A visitor reserves a spot at an event; reservations never exceed capacity, including under concurrent bookings; confirmation shown.

#### F3.4.2 — Workshop Booking and Capacity

##### T3.4.2.1 — Implement workshop booking with live capacity
- **Acceptance criteria:** Available capacity shown from live data; a visitor reserves a spot; no overbooking under concurrent bookings.

#### F3.4.3 — Set Construction Booking

##### T3.4.3.1 — Implement building appointment booking
- **Acceptance criteria:** A visitor books a building appointment according to the rules in T3.1.1.2; no double booking.

#### F3.4.4 — Staff Booking Management (Candidate)

##### T3.4.4.1 — Implement staff tools
- **Acceptance criteria:** Defined after T3.1.1.1.

#### F3.4.5 — Notifications (Candidate)

##### T3.4.5.1 — Implement booking notifications
- **Acceptance criteria:** Defined after T3.2.1.2.

#### F3.4.6 — User Identification (Candidate)

##### T3.4.6.1 — Implement user identification
- **Acceptance criteria:** Defined after T3.2.1.1.

### S3.5 — Website Integration

#### F3.5.1 — Booking Entry Points

##### T3.5.1.1 — Integrate booking into existing pages
- **Acceptance criteria:** PAGE-010 shows live capacity instead of static values (DEC-004); booking entry points added to relevant pages per the updated sitemap; existing tests pass.

### S3.6 — QA & Security

#### F3.6.1 — Booking Quality

##### T3.6.1.1 — Automate booking tests
- **Acceptance criteria:** E2E tests for each booking journey; concurrency tests for capacity limits; all in CI.

##### T3.6.1.2 — Review security
- **Acceptance criteria:** Authentication and authorization reviewed; rate limiting on booking and verification endpoints; common web vulnerabilities checked; personal data access restricted.

##### T3.6.1.3 — Verify on Iranian networks
- **Acceptance criteria:** Booking journeys and notifications verified without VPN on mobile and fixed networks.

### S3.7 — Launch

#### F3.7.1 — Booking Release

##### T3.7.1.1 — Release the booking system
- **Acceptance criteria:** Released to production; backups include booking data; monitoring and alerts in place; staff trained (if staff tools are in scope).

## 9. Completion Criteria (Provisional)

- [ ] All confirmed requirements in §2 available in production
- [ ] No overbooking under concurrent use (tested)
- [ ] Verified from inside Iran without VPN
- [ ] Phase 3 PAGE-IDs and decisions documented
