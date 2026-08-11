# Udemy-like EdTech Platform API

> REST API backend for an online learning platform with role-based access,
> course catalog, exams with nested questions, certificates, cart, and favorites.

[![Python](https://img.shields.io/badge/Python-3.11-blue)]()
[![Django](https://img.shields.io/badge/Django-5.x-green)]()
[![DRF](https://img.shields.io/badge/DRF-3.x-red)]()
[![PostgreSQL](https://img.shields.io/badge/DB-PostgreSQL-blue)]()
[![Docker](https://img.shields.io/badge/Docker-ready-blue)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()

---

## Problem

Online learning platforms need structured access control — students browse
and review, teachers create and manage. Without role separation, anyone
can publish courses or modify content. This API enforces a clean
student/teacher model with full course lifecycle management.

---

## What's Built

- JWT auth (register / login / logout) + OAuth2 GitHub & Google
- Role model: `student` / `teacher` with custom permissions per role
- Course catalog with filtering by `level`, `category`; search by `course_name`
- Nested exam structure: `Exam → Questions → Options` via nested-admin
- Assignments linked to students via ManyToMany
- Certificates per student per course
- Cart and Favorites — auto-created on user registration via `post_save` signal
- Bilingual content (EN / RU) via django-modeltranslation
- Swagger docs via drf-spectacular
- Dockerized: Gunicorn + Nginx + PostgreSQL

---

## Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| POST | `/register/` | Register new user |
| POST | `/login/` | JWT login |
| POST | `/logout/` | Blacklist refresh token |
| GET | `/users/` | Current user profile |
| GET/PUT/DELETE | `/users/<pk>/` | Update / delete profile |
| GET | `/courses/` | Course list with filters |
| GET | `/courses/<pk>/` | Course detail with lessons |
| GET/POST/PUT/DELETE | `/courses/manage/` | Teacher: manage own courses |
| GET | `/lessons/` | Lesson list |
| GET | `/exams/` | Exam list |
| GET | `/exams/<pk>/` | Exam detail with questions & options |
| GET | `/assignments/` | Student assignments |
| GET | `/certificates/` | Student certificates |
| GET | `/reviews/all/` | All reviews |
| GET/POST/PUT/DELETE | `/reviews/` | Student: manage own reviews |
| GET | `/cart-items/` | Cart contents |
| GET | `/favorite-items/` | Favorites |
| GET | `/categories/` | Category list |
| GET | `/api/docs/` | Swagger UI |

---

## Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.11 |
| Framework | Django 5, Django REST Framework |
| Auth | SimpleJWT + django-allauth (GitHub, Google) |
| Permissions | Custom role-based (student / teacher) |
| i18n | django-modeltranslation (EN/RU) |
| Admin | nested-admin (Exam → Questions → Options) |
| Docs | drf-spectacular / Swagger UI |
| Database | PostgreSQL |
| Deploy | Docker Compose, Gunicorn, Nginx |

---

## Project Structure
```
drf_udemy_course/
├── .gitignore
├── readme.md
└── udemy_project/
    ├── Dockerfile
    ├── db.sqlite3
    ├── docker-compose.yml
    ├── manage.py
    ├── media/
    ├── nginx/
    ├── readme.md
    ├── requirements.txt
    ├── udemy_app/
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations/
    │   ├── models.py
    │   ├── permissions.py
    │   ├── serializers.py
    │   ├── tests.py
    │   ├── translation.py
    │   ├── urls.py
    │   └── views.py
    ├── udemy_project/
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── документация/
```
---

## Key Decisions

- **post_save signal** — Cart and Favorite auto-created on user registration;
  no manual setup required per user
- **nested-admin** — Exam → Questions → Options managed in one Django admin
  page; reduces clicks and prevents orphan questions
- **Role permissions** — `CreateCoursePermissions` blocks students from
  publishing; `CreateReviewPermissions` blocks teachers from reviewing —
  enforced at view level, not just frontend
- **Token blacklist** — refresh tokens invalidated on logout via
  `rest_framework_simplejwt.token_blacklist`; prevents token reuse after logout
- **modeltranslation** — language columns added at DB level for Course,
  Lesson, Exam, Questions, Options, Review; same endpoints serve EN/RU

---

## How to Run

**Local:**
```bash
git clone https://github.com/MederbekTuratbekov/drf_udemy_course
cd drf_udemy_course/udemy_project
pip install -r requirements.txt
```

```bash
# Add SECRET_KEY, OAuth keys to .env
python manage.py makemigrations && python manage.py migrate
python manage.py runserver
```

**Docker:**
```bash
docker-compose up --build
```

Open Swagger: `http://localhost/api/docs/`

---
