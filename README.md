# FastAPI Django-like Template

A project template for structuring FastAPI apps like a Django project — modular, scalable, and clean.

## ✨ Features

- Django-style folder layout (`apps/`, `api/`, `config/`)
- Versioned APIs (`v1`, `v2`, etc.)
- [`poetry`](https://python-poetry.org/) for dependency management
- [`alembic`](https://alembic.sqlalchemy.org/) for database migrations
- Built-in support for [`pre-commit`](https://pre-commit.com/)

## 🧠 Layered Architecture

> 🔗 Inspired by [HackSoft’s Django Styleguide](https://github.com/HackSoftware/Django-Styleguide-Example) — adapted to FastAPI.

```
[ API Layer (views.py) ]
    ↓
[ Service / Selector Layer ]
    ↓
[ Repository Layer (optional) ]
    ↓
[ Models / Database ]
```

- **`selectors.py`** – Read-focused business logic using repository functions.
- **`services.py`** – Write-focused logic and coordination using repositories.
- **`repository.py`** – Pure DB access. No business logic.

> ✅ You can skip `repository.py` for smaller projects and keep logic directly in `services`/`selectors`.

## 📁 Folder Structure

```
.
├── README.md
├── poetry.lock
├── pyproject.toml
├── src
│   └── backend
│       ├── alembic
│       ├── api
│       │   ├── exceptions.py
│       │   ├── pagination.py
│       │   └── urls.py
│       ├── apps
│       │   ├── hello
│       │   │   ├── apis
│       │   │   │   ├── v1
│       │   │   │   │   └── views.py
│       │   │   │   └── v2
│       │   │   │       └── views.py
│       │   │   ├── models.py
│       │   │   ├── repository.py
│       │   │   ├── schemas.py
│       │   │   ├── selectors.py
│       │   │   ├── services.py
│       │   │   └── tests
│       │   └── voting
│       │       ├── apis
│       │       │   └── v1
│       │       │       └── views.py
│       │       ├── models.py
│       │       ├── repository.py
│       │       ├── schemas.py
│       │       ├── selectors.py
│       │       ├── services.py
│       │       └── tests
│       ├── config
│       │   ├── settings.py
│       │   └── urls.py
│       └── main.py
├── tests
└── tox.ini
└── .pre-commit-config.yaml 
```

## File Responsibilities

Each subapp in `apps/` (e.g. `hello_world`, `voting`) follows this common structure:

- **models.py** – Defines database models using SQLModel.
- **schemas.py** – Defines request and response validation schemas (Pydantic models).
- **repository.py** – Low-level database queries, like `.filter()`, `.get()`, `.create()`.
- **selectors.py** *(optional)* – Read-only data access patterns (e.g. list filters, aggregations).
- **services.py** – Business logic layer, combines repositories/selectors to implement use cases.
- **apis/v1/views.py** – HTTP route handlers for versioned APIs, similar to Django views.

This modular structure ensures separation of concerns, testability, and scalability.

---

Feel free to fork this and adapt it for your team or project.
