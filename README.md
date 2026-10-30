# SlotSure — Booking Workflow Requirements

**A product requirements case study for an interview-slot booking workflow.**

SlotSure is a fictional web booking flow for Northfield Business School, an invented institution that currently coordinates placement interviews through email threads and a manually maintained spreadsheet.

This repository demonstrates business analysis and product documentation: turning a loosely defined operational problem into personas, a journey, testable requirements, explicit business rules, edge cases, test scenarios and a measurement plan.

> **Documentation-only case study:** no booking application has been built. The organisation, people, operating rules, targets and examples are fictional proposals, not research findings or validated policy.

## Start here

| Document | What you will find |
|---|---|
| [Requirements](docs/requirements.md) | Personas, journey and booking states, user stories, acceptance criteria, business rules, edge cases and non-functional requirements |
| [Test scenarios](docs/test-scenarios.md) | 32 Given/When/Then scenarios, including boundary, concurrency, timing, security, privacy and accessibility cases |
| [Test scenarios CSV](docs/test-scenarios.csv) | Scenario table in a format suitable for importing into a test tracker |
| [Measurement plan](docs/measurement-plan.md) | Goals, KPI definitions, illustrative targets, guardrails, funnel events and analysis approach |
| [Traceability checker](scripts/check_traceability.py) | Python script that checks requirement-to-test references and regenerates the CSV |

## The problem

The fictional placement office faces four operational problems:

- Students can be double-booked into clashing interviews.
- Recruiters can be left with empty interview slots.
- Last-minute cancellations and no-shows waste recruiter time.
- Staff exceptions are difficult to audit when decisions live in email and spreadsheets.

The proposed workflow introduces time-limited slot holds, eligibility checks, booking limits, cancellation rules, waitlists and a staff-facing live view.

## How the analysis is structured

1. Understand users and current pain points.
2. Map the user journey and booking states.
3. Define user stories and testable acceptance criteria.
4. Make business rules explicit and explain their rationale.
5. Identify edge cases and non-functional requirements.
6. Write traceable test scenarios.
7. Define KPIs, guardrails and events before implementation.

## Scope represented in the requirements

- Student booking and cancellation
- Eligibility checks
- Slot capacity and temporary holds
- Booking clash prevention
- Waitlist promotion
- Coordinator overrides and audit trail
- Attendance and no-show recording
- Operational reporting and CSV export

## Traceability and validation

The pack currently contains:
- 4 personas
- 9 user stories and 20 Given/When/Then acceptance criteria
- 11 business rules
- 10 edge cases
- 32 test scenarios

Run the consistency check:

    python scripts/check_traceability.py

The script verifies that scenario references point to defined acceptance criteria, business rules or edge cases, and that every acceptance criterion and business rule is covered by at least one scenario. It also regenerates docs/test-scenarios.csv from the Markdown table.

**Important:** this is a documentation consistency check, not execution of tests against a working application. No application exists in this repository.

## Example measurement framework

The measurement plan proposes metrics such as slot fill rate, no-show rate, booking completion, waitlist conversion and manual interventions per 100 bookings. The targets are illustrative only: there is no baseline dataset, and targets would need to be replaced after measuring an actual placement season.

The plan also distinguishes product funnel events from operational outcomes and warns against making causal claims from a simple before/after comparison.

## Key assumptions and limitations

- Personas are reasoned assumptions, not findings from user interviews.
- Policy values such as a 12-hour cancellation cut-off, five-minute holds and booking limits are proposals for discussion.
- KPI targets are illustrative and have not been validated against historical data.
- Scenarios are written test cases; they have not been executed against software.
- Performance and accessibility requirements are specifications, not verified outcomes.

## Suggested next steps

1. Validate the personas and policy proposals through interviews with students, coordinators and recruiters.
2. Prototype the student booking and coordinator live-view journeys.
3. Usability-test the hold-to-confirm flow.
4. Baseline the current process before setting launch targets.
5. Implement the workflow and execute the scenarios against the application.

## Contribution and AI-use disclosure

I defined the fictional business problem and scope for the requirements pack, including the need for traceable acceptance criteria, business rules, edge cases, test scenarios and measurement. The documentation was drafted with AI assistance (Claude). The scenario and policy assumptions are explicitly labelled as fictional and unvalidated.

## Tools and licences

Markdown · Mermaid (planned diagrams) · Python (traceability script)

Documentation: CC BY 4.0. Traceability script: MIT.
