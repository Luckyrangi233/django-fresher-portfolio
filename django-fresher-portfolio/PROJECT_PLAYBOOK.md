# How to Find and Solve a Real Problem

Use this repeatable process for HelpDesk and every portfolio project. A project is convincing when you can explain who has the problem, how you checked it exists, what you deliberately left out, and how you know your solution works.

## 1. Find a problem before choosing technology

Start near people you can speak with: a student club, family business, volunteer group, or a workflow you experience yourself. Look for repeated workarounds: copying the same data, losing requests, missing deadlines, or asking for status updates.

Ask 3-5 people open questions: “Tell me about the last time this happened”, “What did you do next?”, “Where did it get stuck?”, “How often does that happen?”, and “What do you use now?” Ask for a recent example, not whether they like your idea. Record answers without personal or confidential details. Do not invent interviews; if you cannot interview anyone, say the need is a hypothesis and validate it later.

Write a one-sentence problem statement: “When [user/context], [observable difficulty] happens, causing [impact]. Today they [workaround].” Example: “When a small club receives repair requests in several chat threads, volunteers lose track of ownership and members repeat follow-ups.”

## 2. Turn the problem into a testable scope

Pick one user and one workflow. Define a success signal (for example, a user can create a request and later find its status without searching chat). List acceptance criteria before coding. Keep a “not now” list so you finish the smallest useful version.

For HelpDesk, the first release must let a user sign in, submit a request with title/description/priority, see their requests, and update status. A different user must not see or change those records. Anything else is optional until these criteria work.

## 3. Sketch data and permissions

Use nouns from the workflow as candidate models and verbs as actions. Here, `Ticket` belongs to one `User`; title and description are text; status and priority are constrained choices; timestamps support sorting. Ask: “Who can read, create, update, and delete each record?” Enforce that answer in every query, not only in the interface.

Draw a small diagram or write the relationship in plain text before adding fields. Avoid speculative fields. Add one field only when a user need or acceptance criterion requires it.

## 4. Build in small vertical slices

1. Create the project, app, and first migration; run migrations.
2. Add a model and Django admin registration; inspect records locally.
3. Add one form and a view; validate server-side and save ownership from the signed-in user, never from a submitted user ID.
4. Add URLs and a template; verify the full browser journey.
5. Add authentication and ownership filters; test with two separate users.
6. Add filters or small quality improvements only after the core flow works.

After each slice, run the app and tests. Read Django's error page locally, identify the failing layer (URL, view, template, database, permission), then make one focused fix.

## 5. Test expected behavior and abuse cases

Use this test-design checklist:

- Happy path: a valid request is created and appears in the list.
- Validation: blank title, too-long title, invalid choice, and malformed input are handled safely.
- Authentication: anonymous users are redirected to sign in.
- Authorization: user A cannot read or update user B's record, even by changing the URL.
- Method safety: state changes require POST and CSRF protection.
- Filtering: a known valid filter narrows results; unknown filters do not crash.
- Regression: rerun the suite after each change.

This starter includes tests for core access rules and status changes. Extend tests alongside each feature; a green suite is evidence for the cases tested, not proof that no bugs exist.

## 6. Organize work like a small team

Create a GitHub issue for each user-visible slice. Give it a short problem description, acceptance criteria, and edge cases. Use a branch such as `feature/ticket-search`. Commit small coherent changes with messages like `Add owner-scoped ticket list`. In a pull request, explain what changed, how you tested it, and what remains. Keep a `NOTES.md` with decisions and open questions; do not write a diary instead of shipping working increments.

## 7. Finish the portfolio story

Before presenting, include setup steps, screenshots captured from the real app, a concise feature list, data model, tests, known limitations, and deployment link only if the deployment truly works. Make a short screen recording if useful. Provide no sample passwords for deployed accounts. Never put secrets, real support messages, or private user information in GitHub.

## 8. Improve from evidence

Ask one or two target users to try a task without coaching. Watch where they hesitate. Record the task, what happened, and one next improvement. Prioritize by user impact, frequency, risk, and effort. Do not add a feature because it sounds impressive if no user need justifies it.

## 9. Deploy safely (later milestone)

Deployment is a separate skill. Before a public release, use environment variables for `SECRET_KEY`, turn `DEBUG` off, configure exact `ALLOWED_HOSTS`, HTTPS and secure cookies, a production database, static-file handling, backups, error logging, dependency updates, and data deletion/retention practices. Test a clean install and the deployed permission boundaries. Do not store real customer information until security and privacy requirements are understood.
