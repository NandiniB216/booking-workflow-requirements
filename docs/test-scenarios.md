# SlotSure — Test Scenarios

Each scenario traces to an acceptance criterion (AC) or business rule (BR). These are written test cases for a future build; none has been executed because nothing is implemented. The same table is in `test-scenarios.csv` for import into a test tracker.

| ID | Traces to | Given | When | Then | Type |
|---|---|---|---|---|---|
| T-01 | AC-01.1 | Eligible student, slot capacity 2, 0 booked | Student confirms | Booking Confirmed; remaining capacity 1; .ics offered | Happy path |
| T-02 | AC-01.2, E-01 | Slot capacity 1, two students holding the same slot | Both confirm within the same second | Exactly one Confirmed; other offered waitlist; capacity never negative | Concurrency |
| T-03 | AC-01.3, BR-09 | Student holds a slot | 5 minutes pass without confirming | Hold released; slot shows as available to others | Timing |
| T-04 | AC-02.1, BR-01 | Drive minimum CGPA 7.0; student CGPA 6.8 | Student opens drive | Slots hidden; message names the CGPA rule and both values | Negative |
| T-05 | AC-02.1, BR-02 | Drive disallows backlogs; student has 1 active backlog | Student opens drive | Slots hidden; message names the backlog rule | Negative |
| T-06 | BR-01 boundary | Minimum 7.0; student CGPA exactly 7.0 | Student opens drive | Eligible | Boundary |
| T-07 | AC-03.1, BR-05 | Student booked 10:00–10:30 | Books 10:30–11:00 | Refused (inside 15-min buffer); clashing booking shown | Negative |
| T-08 | BR-05 boundary | Student booked 10:00–10:30 | Books 10:45–11:15 | Allowed (buffer exactly met) | Boundary |
| T-09 | BR-04 | Student has 3 confirmed future bookings | Tries a 4th | Refused with the limit explained | Negative |
| T-10 | BR-04 | Student has 3 bookings, one of them in the past | Tries a new booking | Allowed (only future bookings count) | Boundary |
| T-11 | AC-04.1, BR-07 | Slot is 12 h 1 min away | Student cancels | Cancelled; first waitlisted student gets a hold | Happy path |
| T-12 | AC-04.2, BR-07 | Slot is exactly 12 h away | Student tries to cancel | Disabled; told to contact coordinator | Boundary |
| T-13 | AC-04.3 | Booked in slot A; slot B full | Student reschedules A → B | Refused; booking in A unchanged | Negative |
| T-14 | AC-05.2 | Waitlist: S1, S2; a place frees | S1 does not confirm within 5 min | Offer passes to S2 | Timing |
| T-15 | AC-05.3, E-06 | Offer made at 12 h 2 min before slot | Student confirms at 11 h 58 min | Confirmed | Boundary |
| T-16 | BR-03, E-05 | Student with 2 bookings and 1 waitlist place accepts an offer | Offer acceptance recorded | All bookings cancelled; waitlist place removed; waitlists promoted | Integration |
| T-17 | BR-08 | Student has 2 no-shows this season | Tries to book | Refused; told booking is suspended and who can lift it | Negative |
| T-18 | AC-07.1, BR-11 | Coordinator cancels a booking after cut-off | Reason "Student unwell" (14 chars) entered | Cancelled; audit log row has who, when, before, after, reason | Audit |
| T-19 | AC-07.1 | Coordinator override | Reason "ok" entered | Refused: reason must be at least 10 characters | Negative |
| T-20 | E-10, NFR performance | 500 simulated students when the window opens | All attempt to book within 60 seconds | No slot over capacity; p95 confirmation < 2 s | Load |
| T-21 | AC-09.1 | Recruiter from Company A | Opens Company B's slot URL directly | Access denied | Security |
| T-22 | AC-09.2 | Booking not marked present | 30 min after slot end | Status No-show; coordinator can reverse within 24 h with reason | Timing |
| T-23 | E-03 | Slot capacity 3 with 3 confirmed | Recruiter sets capacity to 2 | Refused with explanation | Negative |
| T-24 | NFR accessibility | Keyboard-only user | Completes a booking end to end | Possible without a mouse; confirmation announced by screen reader | Accessibility |
| T-25 | AC-02.2 | Ineligible student | Inspects the refusal message and page source | No other student's name, CGPA or booking appears | Privacy |
| T-26 | AC-05.1 | Slot full with 2 on the waitlist | Third student joins | Shown position 3 | Happy path |
| T-27 | AC-06.1 | Coordinator creates a drive with no slots | Clicks Publish | Refused; missing fields listed | Negative |
| T-28 | AC-06.2, BR-06 | Drive created Monday, window opens Wednesday 10:00 | Wednesday 09:59 and 10:00 | No notification or booking at 09:59; all eligible students notified and able to book at 10:00 | Timing |
| T-29 | AC-07.2 | Slot full | Coordinator books a student by override without changing capacity | Refused; told to increase capacity first | Negative |
| T-30 | AC-08.1 | Drive with mixed booking states | Coordinator opens live view | Per-slot counts of capacity, confirmed, waitlisted, attended, no-show match the bookings | Reporting |
| T-31 | AC-08.2 | Same drive | Coordinator exports CSV | One row per booking; counts reconcile with T-30 | Reporting |
| T-32 | BR-10, E-09 | Recruiter's device set to London time | Opens their schedule | Slot times shown in IST with local time alongside; stored time unchanged | Time zone |
