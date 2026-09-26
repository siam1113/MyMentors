# MyMentors

MyMentors is a Django web application that connects mentees with mentors. It provides dashboards, mentor requests, and notifications to support the mentoring relationship.

## Features

- Browse and connect with mentors
- Ask questions and make mentorship requests
- A dashboard for tracking mentorship activity
- Notifications to keep users updated

## Project structure (Django apps)

- `Home` — landing pages and general site views
- `Dashboard` — user dashboard views
- `Mentors` — mentor profiles and listings
- `Ask` — mentee requests/questions to mentors
- `Notifications` — user notifications
- `MyMentors` — the main Django project settings

## Getting started

```bash
python manage.py migrate
python manage.py runserver
```

## Tech stack

- Python / Django
- SQLite (development database)
