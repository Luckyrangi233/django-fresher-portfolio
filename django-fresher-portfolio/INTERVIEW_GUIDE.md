# Interview Guide: Explain Your Project Clearly

Do not memorize a script. Replace bracketed prompts with facts from your own research, implementation, and test runs. Never claim a user count, speed improvement, or production deployment you did not measure.

## 60-second explanation

“I built **HelpDesk**, a Django web app for [specific user group] who [validated problem or clearly labeled hypothesis]. A user can sign in, create and prioritize a request, track its status, and filter their own requests. I used Django's built-in authentication, a relational `Ticket` model, model forms, templates, and SQLite for the learning version. A key design decision was scoping every ticket lookup to the signed-in user, then testing that a second user cannot access the first user's record by changing the URL. The current limitations are [honest limitations]. My next step is [evidence-based improvement].”

## STAR story prompts

- **Situation:** Who had the problem? What recent example did you observe?
- **Task:** What small outcome did you decide to deliver first?
- **Action:** How did you model data, choose a Django feature, protect access, and test it?
- **Result:** What can a user do now? What did tests verify? What did a user try? Be precise about evidence.

## Common questions to practice

**Why Django?** Explain the project needs Django addresses (authentication, ORM, forms, admin, conventions). Mention alternatives you considered only if you actually evaluated them.

**How is a ticket linked to a user?** It has a foreign key to the configured `AUTH_USER_MODEL`; the view assigns the current authenticated user during save. The submitted form does not choose an owner.

**How do you prevent one user from seeing another user's ticket?** The detail and update lookups filter by both ticket ID and `created_by=request.user`. The list is owner-scoped too. Tests check the cross-user detail case. Explain the remaining tests you would add.

**Why use POST for status updates?** It changes server state. GET should be safe to repeat and must not mutate data. The form includes a CSRF token.

**What happens when invalid status data is sent?** The view checks against Django's declared status values and does not save invalid input. A production app could additionally show a validation message and log suspicious requests.

**What would you change for many tickets?** Add pagination, inspect query counts, use database indexes based on measured query patterns, and consider search. Do not optimize before measuring.

**How would you deploy it?** Turn debug off, move secrets to environment configuration, use production hosts/database/static-file handling, enable HTTPS and secure cookies, configure logging and backups, and test permissions on the live service.

**What was a bug or challenge?** Choose a real example. Describe the symptom, how you narrowed down the layer, the fix, and a regression test. If you have not hit a meaningful bug yet, discuss a design risk rather than inventing a story.

**What would you build next?** Pick the highest-value missing workflow based on user feedback and explain its acceptance tests. Avoid naming a list of trendy technologies without a reason.

## Demo order (3-5 minutes)

1. State the target user and problem evidence or hypothesis.
2. Sign in as one user and create a request.
3. Filter and change status.
4. Explain owner-scoping and show the relevant automated tests.
5. State one known limitation and one next step.

Use a fresh local database and harmless sample data. Never expose real users' requests or credentials in an interview demo.
