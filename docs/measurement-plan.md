# SlotSure — Measurement Plan

How the placement office would know whether SlotSure works. Because the scenario is fictional there is **no baseline data**; every target below is illustrative and would be replaced by a measured baseline from one placement season before launch.

## 1. Goals → metrics

| Goal | Primary metric | Definition | Illustrative target |
|---|---|---|---|
| Fill recruiters' time | **Slot fill rate** | Confirmed bookings at slot start ÷ total slot capacity | ≥ 90% |
| Reduce wasted slots | **No-show rate** | No-show bookings ÷ bookings that reached slot time | < 5% |
| Free slots early enough to reuse | **Late-cancellation share** | Cancellations within 12 h ÷ all cancellations | < 10% |
| Make booking easy | **Booking completion rate** | Bookings confirmed ÷ eligible students who opened a slot list | ≥ 80% |
| Make booking fast | **Median time to book** | Drive page opened → booking confirmed, per student | < 2 min |
| Use the waitlist | **Waitlist conversion** | Waitlist offers confirmed ÷ waitlist offers made | ≥ 60% |
| Reduce coordinator workload | **Manual interventions per 100 bookings** | Coordinator overrides ÷ bookings × 100 | Trend down season on season |

### Guardrail metrics (must not get worse)

- **Clash incidents reported on the day** — should be 0 with BR-05 enforced.
- **Over-capacity slots** — must be 0 (any non-zero value is a defect).
- **Support requests per 100 students** — watch for confusion after launch.
- **Eligibility disputes** — students contesting a refusal; a spike suggests unclear messages (AC-02.1).

## 2. Funnel

```
Drive notification sent
  → Drive page opened            (open rate)
  → Eligible                     (eligibility rate — not a UX metric; driven by criteria)
  → Slot list viewed
  → Slot held                    (hold rate)
  → Booking confirmed            (hold → confirm conversion; abandoned holds)
  → Attended                     (attendance rate)
```

Drop-off between *Slot held* and *Booking confirmed* is the best signal of UX friction; drop-off between *Confirmed* and *Attended* is a behaviour and policy signal (cut-off, reminders, no-show rule).

## 3. Events to instrument

| Event | Key properties |
|---|---|
| `drive_published` | drive_id, slot_count, total_capacity, window_open_at |
| `drive_viewed` | drive_id, student_id (hashed), eligible (bool), failed_rule |
| `slot_held` | slot_id, hold_expires_at |
| `hold_released` | slot_id, reason (expired / cancelled) |
| `booking_confirmed` | booking_id, slot_id, seconds_from_first_view, source (self / waitlist / override) |
| `booking_cancelled` | booking_id, hours_before_slot, actor (student / coordinator), reason |
| `booking_refused` | rule_id (BR-04, BR-05, BR-08 …) |
| `waitlist_joined` / `waitlist_offer_made` / `waitlist_offer_confirmed` | slot_id, position |
| `attendance_marked` / `no_show_recorded` / `no_show_reversed` | booking_id, actor |

`booking_refused` with a `rule_id` lets the office see which rules users hit most — a direct input to whether a rule is set at the right level.

## 4. Analysis approach

- **Season-on-season comparison** of fill rate and no-show rate, segmented by company size and slot time-of-day (early-morning and post-lunch slots typically behave differently).
- **No causal claims from a before/after comparison alone.** Placement seasons differ in company mix and student numbers. Where possible, roll out one change at a time (for example, reminder timing) and compare drives in the same season.
- **Rule tuning:** if BR-07's 12-hour cut-off produces a high late-cancellation share *and* low waitlist conversion, test 24 hours on a subset of drives.

## 5. Reporting

- Live coordinator view (AC-08.1) for the day.
- Weekly summary during placement season: fill rate, no-show rate, top refusal reasons, open issues.
- End-of-season review with the placement head: metrics vs targets, rule changes proposed for next season.
