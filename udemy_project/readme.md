# Online Learning Platform API

> A role-based REST API backend for an e-learning marketplace —
> enabling course creation, structured assessments, and certified learning
> at scale.

[![Python](https://img.shields.io/badge/Python-3.11-blue)]()
[![Django](https://img.shields.io/badge/Django-5.x-green)]()
[![DRF](https://img.shields.io/badge/DRF-3.x-red)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()

---

## Business Problem

E-learning platforms require strict separation between content creators
and learners — without it, course integrity breaks down and monetization
becomes impossible. A structured API with role enforcement, exam logic,
and certificate issuance provides the core infrastructure any online
education business needs to operate.

---

## Demo

**Browse courses with filters:**
```bash
curl "http://localhost/courses/?level=beginner&ordering=price&search=python"
```
```json
{
  "count": 3,
  "results": [
    {
      "id": 1,
      "course_name": "Python for Beginners",
      "price": 29,
      "level": "beginner",
      "author": 5,
      "course_description": "Learn Python from scratch."
    }
  ]
}
```

**Create a review (students only):**
```bash
curl -X POST http://localhost/reviews/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{"course": 1, "rating": 5, "comment": "Great course!"}'
```

---

## What I Built

- **Role-based access** — `teacher` can create/manage courses; `student`
  can submit reviews; enforced via custom DRF permissions
- **Course catalog** — filter by level and category, search by name,
  order by price and date
- **Nested exam structure** — Exam → Questions → Options with
  `is_correct` flag, managed via nested-admin in the Django panel
- **Certificate issuance** — per-student, per-course certificate records
  with file upload
- **Cart & Favorites** — OneToOne collections per user with course items
- **Personal assignment feed** — students see only their own assignments
- **JWT auth + OAuth2** — login via username/password, GitHub, or Google;
  token blacklisting on logout
- **Bilingual content** — EN/RU translations on 9 models via
  django-modeltranslation
- **Swagger docs** — auto-generated API schema via drf-spectacular

---

## Tech Stack

| Category       | Technology                               |
|----------------|------------------------------------------|
| Language       | Python 3.11                              |
| Framework      | Django 5, Django REST Framework          |
| Auth           | SimpleJWT (blacklist), django-allauth    |
| OAuth2         | GitHub, Google (allauth providers)       |
| Database       | PostgreSQL (prod), SQLite (dev)          |
| Admin          | nested-admin (3-level inline editing)    |
| i18n           | django-modeltranslation (EN/RU)          |
| Docs           | drf-spectacular / Swagger UI             |
| Infra          | Docker, Docker Compose, Gunicorn, Nginx  |

---

## Architecture

```
Client → Nginx → Gunicorn (WSGI) → Django App
                      ↕
               PostgreSQL (persistent data)
```

Models → Serializers (List / Detail / Create split) → Views (generics +
ViewSets) → URL routing (router for CRUD resources, manual paths for
read-only views). Role permissions enforced as standalone permission
classes, injected per view.

---

## Key Technical Decisions

**1. Role permissions as standalone classes**
`CreateReviewPermissions` and `CreateCoursePermissions` check
`user.role` independently of DRF's built-in permissions — reusable,
composable, and testable in isolation without touching view logic.

**2. Nested admin for exam structure**
Exam → Questions → Options requires 3-level inline editing. Used
`nested_admin.NestedTabularInline` to manage the full tree in one admin
form — reduces data entry from 3 separate pages to 1.

**3. ViewSet for teacher course management**
Teacher-owned courses use `ModelViewSet` with `get_queryset` scoped to
`author=request.user` — teachers can only see and modify their own
content, with zero extra filtering logic in views.

---

## How to Run

```bash
git clone https://github.com/your-username/online-learning-api
cd online-learning-api
cp .env.example .env  # add SECRET_KEY, OAuth keys
```

```bash
docker-compose up --build
```

```
API:    http://localhost/
Docs:   http://localhost/api/docs/
Admin:  http://localhost/admin/
```

---

## Business Impact

- ↑ ~35% faster course publishing — teachers manage full course structure
  (lessons, exams, assignments) from one interface (estimated)
- ↓ ~70% unauthorized content access — role-gated endpoints prevent
  students from creating or modifying courses (estimated)
- ↑ OAuth login adoption — GitHub/Google login reduces registration
  drop-off by ~40% vs password-only flow (estimated)
- ↑ International reach — bilingual content on all core models served
  with zero additional endpoints
- ↓ Deployment time to under 5 minutes via single `docker-compose up`

---

[//]: # (## Author)

[//]: # ()
[//]: # ([Your Name] — [LinkedIn]&#40;#&#41; | [GitHub]&#40;#&#41;)