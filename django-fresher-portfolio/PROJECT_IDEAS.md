# Three Real-World Project Briefs

Build one polished, tested project before collecting many unfinished demos. These ideas are intentionally different in their workflow and give a fresher room to show Django fundamentals.

## 1. HelpDesk: support request tracker (included)

**Users/problem:** A small organization loses service requests in chat or email and cannot tell what is still open.

**MVP:** Sign in, create requests, select priority, list/filter personal requests, update status, protect record ownership.

**Stretch:** Staff assignment and role permissions, comments, email notification, search, dashboard metrics, audit history, API, PostgreSQL deployment.

**Acceptance checks:** An anonymous visitor cannot access the tracker; a user only sees their own tickets; valid status changes save; invalid status does not change a record; tests cover these cases.

**What it demonstrates:** Django models, forms, authentication, CRUD, ORM filtering, templates, access control, migrations, tests.

## 2. Community pantry inventory

**Users/problem:** Volunteers have limited visibility into stock levels and expiry dates, causing shortages or avoidable waste.

**MVP:** Staff login, item catalog, quantity adjustments, expiry dates, low-stock and soon-to-expire views, movement history.

**Stretch:** CSV import/export, role permissions, notifications, batch/lot tracking, accessibility improvements, charts.

**Acceptance checks:** Stock never becomes negative without an explicit policy; every adjustment records who changed it and when; filters show only matching records; an unauthorized user cannot change inventory.

**Engineering questions:** Use a transaction when changing quantity and recording movement; how will duplicate imports be detected? How will a volunteer correct a mistaken count without deleting history?

## 3. Appointment booking for a local service

**Users/problem:** A small service provider double-books time slots and spends time confirming appointments by message.

**MVP:** Service catalog and duration, available slots, booking and cancellation, owner schedule view, server-side overlap validation.

**Stretch:** Time zones, reminder email, rescheduling rules, waitlist, calendar export, payment integration (only in a sandbox).

**Acceptance checks:** Two simultaneous requests cannot reserve the same slot; past slots cannot be booked; a customer can only cancel their own booking; unavailable slots are explained clearly.

**Engineering questions:** How does a database constraint or transaction prevent race conditions? How are local times stored? What happens when a service duration changes after a booking exists?

## 4. Choosing your own problem

Use this quick score (1-5) before choosing: can you reach users, how often does the problem happen, how costly is the workaround, can an MVP be built in 2-4 weeks, and can you demonstrate results without sensitive data? Choose the highest-impact problem you can validate, not the most complicated architecture.
