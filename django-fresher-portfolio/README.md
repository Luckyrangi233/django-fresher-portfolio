# Django Fresher Portfolio: HelpDesk

A practical starter portfolio built around a realistic support-ticket workflow. It is designed to help a new Python developer learn to discover a problem, build a useful solution, test it, explain trade-offs, and present the work honestly to interviewers.

## What is included

- `helpdesk/`: runnable Django 5.2 application with sign-in, ticket creation, ownership, status and priority filters, ticket details, and staff status updates.
- `PROJECT_PLAYBOOK.md`: problem discovery, scope, data modeling, implementation, testing, deployment, and project management workflow.
- `PROJECT_IDEAS.md`: three follow-on real-world projects with user needs, MVPs, stretch goals, and acceptance criteria.
- `INTERVIEW_GUIDE.md`: concise project explanation, likely interview questions, and honest answers to adapt after building.
- `RESUME_GUIDE.md`: fresher resume template and achievement bullets with placeholders; never claim unbuilt features.
- `CONTRIBUTING.md`: suggested issue, branching, commit, and pull-request habits.

## Run locally

Python 3.10+ is required.

```bash
cd helpdesk
python -m venv .venv
# Windows: .venv\Scripts\activate
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open http://127.0.0.1:8000/. The first user is created via `createsuperuser`; sign in at `/accounts/login/`. SQLite is used for the local learning setup. Do not deploy with `DEBUG=True` or the example secret key.

## The capstone problem

Small teams often lose customer issues across email, chat, and spreadsheets. HelpDesk gives authenticated staff one place to record a request, assign an urgency, track its status, and find the current state. This starter uses tickets and Django's built-in user model. It intentionally keeps the first version small enough to understand and extend.

## Suggested build sequence

1. Read `PROJECT_PLAYBOOK.md` and write down a target user and one painful workflow.
2. Run the app and inspect the models, forms, views, URLs, templates, and tests.
3. Change one requirement yourself (for example, add due dates); write acceptance criteria first.
4. Run `python manage.py test` after each change.
5. Add a README screenshot, a deployment guide, and a short demo only after verifying those features.
6. Use `INTERVIEW_GUIDE.md` and `RESUME_GUIDE.md` to describe what you actually built.

## Safety and production limits

This is a learning MVP, not a production helpdesk. It has no email notifications, file uploads, SLA enforcement, audit log, or hardened deployment settings. Before public deployment, configure environment-based secrets, production static files, HTTPS, secure cookies, allowed hosts, database backups, logging, and abuse controls. Review every change and test access rules before storing real customer data.

## GitHub

The folder is repository-ready. Create a repository named `django-helpdesk-portfolio`, add these files, and push the initial commit. Keep it public only if you are comfortable sharing the source and have removed secrets or personal data. The included example secret is for local development only.
