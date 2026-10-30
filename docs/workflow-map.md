# SlotSure — Workflow and booking states

This page visualises the proposed workflow described in the requirements. It is a specification aid, not a diagram of a built application.

## Student booking journey

```mermaid
flowchart TD
    A[Open placement drive] --> B{Eligible?}
    B -- No --> C[Show eligibility reason]
    B -- Yes --> D[View available slots]
    D --> E{Slot available?}
    E -- No --> F[Join waitlist if available]
    E -- Yes --> G[Place temporary hold]
    G --> H{Confirm before hold expires?}
    H -- No --> I[Release hold]
    H -- Yes --> J[Confirm booking]
    J --> K[Attend interview]
    J --> L[Cancel within permitted window]
    K --> M[Mark attendance]
    K --> N[Record no-show if absent]
```

## Booking lifecycle (conceptual)

```mermaid
stateDiagram-v2
    [*] --> Held
    Held --> Confirmed: confirmed before hold expiry
    Held --> Available: hold expires
    Confirmed --> Cancelled: permitted cancellation
    Confirmed --> Attended: attendance recorded
    Confirmed --> NoShow: no-show recorded
    Cancelled --> [*]
    Attended --> [*]
    NoShow --> [*]
```

## Reading this diagram

- Eligibility is checked before the student can hold a slot.
- A hold is temporary and must be confirmed before expiry.
- A waitlist is an alternative when capacity is full; the detailed offer and promotion rules remain in the requirements document.
- Cancellation, attendance and no-show behaviour are governed by the numbered business rules and acceptance criteria.

For exact behaviour and boundary cases, use [requirements.md](requirements.md) and [test-scenarios.md](test-scenarios.md). These diagrams summarise the proposal and do not replace those specifications.
