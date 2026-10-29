# Booking Workflow Requirements — SlotSure (fictional)

A product-requirements case study for an interview-slot booking flow at an invented business school. It shows how I take a messy manual process and turn it into personas, a user journey, testable requirements, explicit business rules, edge cases, test scenarios and a measurement plan.

**This is a documentation project, not a working application.** The organisation, people and numbers are fictional.

> **Before publishing — delete this box once true.** Drafted with AI assistance (Claude). Keep "My contribution" only after you have reviewed every rule and can defend each trade-off in an interview.

---

## The problem

Northfield Business School (fictional) books placement interviews through an email thread and a hand-maintained spreadsheet. The results: students double-booked into clashing interviews, recruiters left with empty slots, last-minute no-shows, and no record of why the placement office made exceptions.

## What's in the pack

| Document | Contents |
|---|---|
| [`docs/requirements.md`](docs/requirements.md) | 4 personas · student journey and booking-state diagrams · 9 user stories with 20 Given/When/Then acceptance criteria · 11 business rules with rationale · 10 edge cases · non-functional requirements (accessibility, privacy, audit, performance) |
| [`docs/test-scenarios.md`](docs/test-scenarios.md) | 32 test scenarios, each traced to an acceptance criterion or rule; boundary, concurrency, timing, security and accessibility cases |
| [`docs/test-scenarios.csv`](docs/test-scenarios.csv) | The same scenarios for import into a test tracker (generated) |
| [`docs/measurement-plan.md`](docs/measurement-plan.md) | Goals → metrics with formulas, guardrails, funnel, event instrumentation, analysis approach |
| [`scripts/check_traceability.py`](scripts/check_traceability.py) | Checks that every scenario points at a real requirement and every requirement has a scenario |

## Approach

1. **Start from the people.** Personas for the student, coordinator, recruiter and approver, each with a goal and a current frustration.
2. **Map the journey and the states.** A booking is a small state machine (held → confirmed → cancelled / attended / no-show). Drawing it exposed questions a list of features hides, such as what happens to a hold nobody confirms.
3. **Write testable requirements.** Every acceptance criterion is phrased so that a tester can say pass or fail.
4. **Make the rules explicit and numbered.** Cut-off times, limits and penalties sit in one table with a rationale, so they can be challenged and tuned rather than discovered in the code.
5. **Hunt for edge cases.** Simultaneous last-place bookings, capacity reduced below bookings, a student accepting an offer while on a waitlist.
6. **Decide how success will be measured before building.** Metrics, guardrails and the events needed to compute them.

## Testing

Nothing is implemented, so nothing has been executed against software. What *is* checked:

- `python scripts/check_traceability.py` — confirms all 32 scenarios reference defined requirements and all 20 acceptance criteria and 11 business rules have at least one scenario. Its first run found 9 untested requirements, which led to scenarios T-25 to T-32.

## Implemented vs. planned

| Done | Not done |
|---|---|
| Requirements, rules, edge cases, test scenarios, measurement plan | Any application code, UI design or prototype |
| Traceability check | Executed tests |
| | Validation of rules or targets with real users or data |

## Limitations

- The numbers in the rules (12-hour cut-off, 3 bookings, 2 no-shows) are reasoned proposals, not tested values.
- Measurement targets are illustrative; there is no baseline.
- Personas are assumptions, not research findings. A real project would start with interviews of each group.

## Possible improvements

- Validate personas and rules with 5–6 short interviews per user group.
- Low-fidelity wireframes for the student booking flow and the coordinator live view.
- A clickable prototype to test the hold → confirm step, the likeliest point of drop-off.

## My contribution

**[CONFIRM BEFORE PUBLISHING — keep only what is true]**

- Chose the scenario and the questions the pack had to answer.
- Drafted with AI assistance (Claude), then reviewed and edited the rules, edge cases and metrics.
- [FILL IN what you changed or added yourself]

## Tools

Markdown · Mermaid diagrams · Python (traceability check) · AI-assisted drafting (Claude)

## Licence

Text: CC BY 4.0. Script: MIT.
