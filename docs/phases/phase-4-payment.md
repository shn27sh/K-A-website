# Phase 4 — Payment

> **Status:** Not scheduled (post-MVP) · **Last updated:** 2026-10-26
> Roadmap: [development-plan.md](../development-plan.md) · Decisions: [decisions.md](../project/decisions.md) · Constraints: [iran-constraints.md](../project/iran-constraints.md) · Testing: [testing-strategy.md](../testing/testing-strategy.md)

## 1. Purpose

Introduce a secure payment system supporting bookings and sales.

## 2. Confirmed Requirements

| Requirement | Source |
|---|---|
| Secure payments for bookings, including workshops and set construction | Conversation |
| Purchases and sales through the platform | Conversation |

## 3. Scope

- **In scope:** payments for bookings and for purchases/sales; scope details pending (DEC-031).
- **Relation to existing pages:** PAGE-013 and PAGE-014 (Phase 1, no online payment) and PAGE-015 (unscheduled) are candidates for online sales, pending DEC-031 and DEC-032.
- **PAGE-IDs:** to be defined in `pages.md`.

## 4. Iran-Specific Context

Details: [iran-constraints.md §7, §10](../project/iran-constraints.md). In summary:

- Online card payments go through the national Shaparak network, using either a direct bank PSP gateway or a licensed payment facilitator (پرداخت‌یار).
- Gateways typically require an eNamad trust seal and business documents, and often require requests from an Iranian server IP (verify per provider).
- International payment methods are not available.
- Amounts are commonly handled in Rial at the API level (verify per provider).

## 5. Open Questions

- Gateway type and provider (DEC-030).
- Merchant prerequisites: business license (جواز کسب), eNamad, bank account, gateway contract — long lead times.
- Sales scope (DEC-031): products sold online, delivery or in-store pickup, inventory, returns.
- Booking payment: full payment or deposit; refunds and cancellations (aligned with Phase 3 rules).
- Whether event bookings require payment (only workshops and set construction are confirmed).
- Discounts (PAGE-002 mentions discounts for larger sets) and their online handling.
- Invoicing and tax obligations for online sales (verify with an accountant).
- Staff reporting and reconciliation needs.

## 6. Dependencies and Constraints

- Phase 3 for booking payments.
- Phase 1 website in production with the business details eNamad requires; domain registrant per DEC-019.
- Backend hosted in Iran (T3.2.1.1).

## 7. Expected Outcomes

Users pay online for bookings and purchases through an Iranian gateway; every payment is verified server-side and linked to its booking or order; staff can reconcile payments.

## 8. Stages (Provisional)

| Stage | Objective |
|---|---|
| S4.1 Merchant & Legal Prerequisites | eNamad, gateway contract, tax setup (can start before Phase 4 development) |
| S4.2 Requirements Definition | Scope, rules, PAGE-IDs |
| S4.3 Payment Architecture | Payment flow and data design |
| S4.4 UX Design (Figma) | Payment and checkout flows |
| S4.5 Implementation | Payment features |
| S4.6 QA & Security | Sandbox testing, failure modes, security review |
| S4.7 Launch | Controlled go-live |

## 9. Features, Development Tasks, and Subtasks

Provisional. Features marked *candidate* require confirmation.

### S4.1 — Merchant & Legal Prerequisites

#### F4.1.1 — Merchant Readiness

##### T4.1.1.1 — Obtain eNamad
- **Purpose:** Prerequisite for most Iranian payment gateways.
- **Acceptance criteria:** eNamad issued and displayed on the website as required.
- **Subtasks:**
  - [ ] Confirm current eNamad requirements (business license, domain ownership, published contact details)
  - [ ] Apply and complete verification

##### T4.1.1.2 — Select a gateway and sign the contract
- **Outcome:** DEC-030 decided.
- **Acceptance criteria:** Contract signed; sandbox and production credentials available and stored securely.

##### T4.1.1.3 — Clarify invoicing and tax obligations
- **Acceptance criteria:** Obligations confirmed with an accountant and documented.

### S4.2 — Requirements Definition

#### F4.2.1 — Payment Requirements

##### T4.2.1.1 — Resolve scope and open questions
- **Outcome:** DEC-031 and the §5 questions decided.
- **Acceptance criteria:** Every §5 question decided or explicitly deferred.

##### T4.2.1.2 — Define PAGE-IDs and flows
- **Acceptance criteria:** New pages added to `pages.md` with Phase 4; payment and checkout flows documented.

### S4.3 — Payment Architecture

#### F4.3.1 — Payment Flow Design

##### T4.3.1.1 — Design the payment flow
- **Acceptance criteria:** Documented flow: payment request → redirect to gateway → callback → server-side verification → booking or order confirmation; no card data handled or stored by the platform; idempotent handling of repeated callbacks; complete transaction log; reconciliation procedure.

### S4.4 — UX Design

#### F4.4.1 — Payment UX

##### T4.4.1.1 — Design payment and checkout flows
- **Acceptance criteria:** Mobile-first designs including success, failure, cancellation, and pending states; signed off.

### S4.5 — Implementation

#### F4.5.1 — Booking Payments

##### T4.5.1.1 — Implement payment for bookings
- **Acceptance criteria:** Workshop and set-construction bookings can be paid online; a booking is confirmed only after server-side payment verification.

#### F4.5.2 — Sales Checkout

##### T4.5.2.1 — Implement checkout for sales
- **Acceptance criteria:** Defined after DEC-031.

#### F4.5.3 — Refunds and Cancellations (Candidate)

##### T4.5.3.1 — Implement refunds and cancellations
- **Acceptance criteria:** Defined after T4.2.1.1.

#### F4.5.4 — Staff Reporting and Reconciliation (Candidate)

##### T4.5.4.1 — Implement payment reporting
- **Acceptance criteria:** Defined after T4.2.1.1.

### S4.6 — QA & Security

#### F4.6.1 — Payment Quality

##### T4.6.1.1 — Test with the gateway sandbox
- **Acceptance criteria:** E2E tests cover success, user cancellation, gateway failure, lost callback, duplicate callback, and timeout.

##### T4.6.1.2 — Review security
- **Acceptance criteria:** Payment endpoints, secrets handling, and verification logic reviewed; an external security review is recommended before go-live.

### S4.7 — Launch

#### F4.7.1 — Payment Release

##### T4.7.1.1 — Go live in a controlled way
- **Acceptance criteria:** Small real transactions verified end to end, including settlement; monitoring and alerts for payment failures in place; reconciliation procedure run once.

## 10. Completion Criteria (Provisional)

- [ ] Confirmed requirements in §2 available in production
- [ ] All payments verified server-side and reconciled
- [ ] Merchant prerequisites (eNamad, contract) complete
- [ ] Security review complete
