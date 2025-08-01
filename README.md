# FastAPI Django-like Template

A project template for structuring (async) FastAPI apps like a Django project — modular, scalable, and clean.

---

Feel free to fork this and adapt it for your team or project.

## 📚 Table of Contents

- [✨ Features](#-features)
- [🧠 Layered Architecture](#-layered-architecture)
- [📁 Folder Structure](#-folder-structure)
- [🗂️ File Responsibilities](#file-responsibilities)
- [🚀 Server QuickStart](#server-quick-start)
- [🛠️ Installation](#️-installation)
- [⚙️ Makefile Commands](#️-makefile-commands)
- [🔧 Migrations with Alembic](#-migrations-with-alembic)
- [🐚 Interactive Shell](#-interactive-shell)
- [🧪 Unit Testing](#-unittesting)

## ✨ Features

- Django-style folder layout (`apps/`, `api/`, `config/`)
- Versioned APIs (`v1`, `v2`, etc.)
- [`poetry`](https://python-poetry.org/) for dependency management
- [`alembic`](https://alembic.sqlalchemy.org/) for database migrations
- [`pytest`](https://docs.pytest.org/) for testing
- Built-in support for [`pre-commit`](https://pre-commit.com/)
- IPython shell (`make shell`) similar to Django's shell
- Developer-friendly `Makefile` commands for common tasks

## 🧠 Layered Architecture

> 🔗 Inspired by [HackSoft’s Django Styleguide](https://github.com/HackSoftware/Django-Styleguide-Example) — adapted to FastAPI.

```shell

        Request-Response Flow (User/API)
                   │
     [ API Layer (apis/*.py) ]
                   │
                   │ use
                   ▼ 
     [ Service Layer (services/*.py) ]
                   │
                   │ use
                   ▼ 
     [ Repository Layer (repositories/*.py) ]
                   │
                   │ use
                   ▼ 
         [ Models / Database ]

────────────────────────────────────────────

      ╭────────────────────────────╮
      │      Cross-App Usage       │
      │  (e.g. user/, chat/, etc.) │
      ╰────────────┬───────────────╯
                   │
     [ Interface Layer (interfaces/*.py) ]  ◄── Used by other subapps
                   │
                   │ use
                   ▼
     [ Service Layer (services/*.py) ]      ◄── Business logic
                   │
                   │ use
                   ▼
 [ Repository Layer (repositories/*.py) ]    ◄── DB access only
                   │
                   │ use
                   ▼
         [ Models / Database ]
```

- **`services/*.py`** – Bussiness-focused logic and coordination using repositories.
- **`repositories/*.py`** – Pure DB access. No business logic.

- **`interfaces/*.py`** – Public entrypoints for other subapps. Keeps boundaries clean and prepares for future microservice separation.

## 📁 Folder Structure

```shell
.
├── Dockerfile
├── Makefile
├── README.md
├── alembic
│   ├── README
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       └── 7235dcd2cce6_example_migration_file_alembic.py
├── alembic.ini
├── api
│   ├── exceptions.py
│   ├── pagination.py
│   └── urls.py
├── apps
│   ├── example
│   │   ├── apis
│   │   │   ├── v1
│   │   │   │   └── views.py
│   │   │   └── v2
│   │   │       └── views.py
│   │   ├── interfaces
│   │   │   └── core.py
│   │   ├── models
│   │   │   └── somemodel.py
│   │   ├── repositories
│   │   │   └── somemodel_repo.py
│   │   ├── schemas
│   │   │   └── somemodel_schema.py
│   │   ├── services
│   │   │   └── core_service.py
│   │   └── tests
│   │       ├── api
│   │       │   └── test_api_v1.py
│   │       ├── factories.py
│   │       ├── test_repositories.py
│   │       └── test_services.py
│   └── example_app
│       ├── apis
│       │   └── v1
│       │       └── views.py
│       ├── interfaces
│       │   └── core.py
│       ├── models
│       ├── repositories
│       ├── services
│       │   └── core_service.py
│       └── tests
│           ├── api
│           │   └── test_api_v1.py
│           ├── factories.py
│           ├── test_repositories.py
│           └── test_services.py
├── common
│   ├── mixins
│   │   └── models.py
│   ├── repository
│   │   └── base.py
│   ├── schemas
│   │   ├── enums.py
│   │   └── response.py
│   ├── tests
│   │   └── test_repository.py
│   └── utils
├── config
│   ├── db.py
│   ├── redis.py
│   ├── settings.py
│   └── urls.py
├── conftest.py
├── docker-compose.yml
├── initdb
├── main.py
├── poetry.lock
├── pyproject.toml
├── pytest.ini
├── scripts
│   └── shell.py
└── tox.ini

```

## 🗂️ File Responsibilities

Each subapp in `apps/` (e.g. `user`, `chat`) follows this common structure:

- **models/*.py** – Defines database models using SQLModel.
- **schemas/*.py** – Defines request and response validation schemas (Pydantic models). Same as Django REST Framework serializers.
- **services/*.py** – Business logic layer, using repositories to implement use cases.
- **repositores/*.py** (optional) – Low-level database queries. Used by Selectors & Services.
- **apis/`<version>`/views.py** – HTTP route handlers for versioned APIs, similar to Django views.
- **interfaces/*.py** – When *other services/subapps* import any logic from a subapp, they import these files. Super useful when separating into microservices later.


This modular structure ensures separation of concerns, testability, and scalability.

## Server Quick Start

#### Prerequisites

- `docker compose`
- `make` (for Makefile support)

To quickly start the server locally with [Docker Compose](https://docs.docker.com/compose/install/):

```bash
# up server, this will create docker images & containers
make compose

# down server,
make compose_down
```

Otherwise continue with [installation](#️-installation) below.

## 🛠️ Installation

### 🔧 Install Poetry

#### Prerequisites

- Python `3.13`
- [`Poetry`](https://python-poetry.org/docs/#installation)
- `make` (for Makefile support)

> This project uses **Python 3.13**, but you can change to any version you prefer.

If you don't have Poetry, install it using the [official instructions](https://python-poetry.org/docs/#installation). For most systems, this works:

**MacOS/Linux:**

```bash
curl -sSL https://install.python-poetry.org | python3.13 -
```

You may need to restart your shell or manually add Poetry to your PATH. Add the following to your .bashrc, .zshrc, or equivalent:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

Then restart your terminal and verify it works:

```bash
poetry --version
```

To run python commands in poetry environment, just append `poetry run` before everything:

```bash
poetry run python
poetry run pip list
poetry run pip install
# and so on...
```

#### With poetry, when adding new python package, instead of pip just do:

```bash
# same dir as pyproject.toml
poetry add <package-name> # e.g. poetry add alembic

# this will update poetry.lock, commit this file to version control too
```

#### You can also install pre-commit hooks (come with black, isort, flake8)

```bash
poetry run pre-commit install
```

### Test Run Server

#### Migrations

Do migration (upgrade/downgrade) with:

```bash
make uprade
make downgrade
```

#### Populate environment variables

Remember to create & populate environment variables file `.env`.
Check out example file at `.env.example`

#### Run local server

Start the local server with:

```bash
make run_dev
# (aka. poetry run fastapi dev)
```

## ⚙️ Makefile Commands

Use `make <command>` to run common development tasks:

```make
make rundev         # Start the FastAPI app
make migrations     # Run Alembic migration files
make upgrade        # Upgrade Alembic migration
make downgrade      # Downgrade Alembic migration
shell               # Start an interactive shell (IPython)
test                # Run tests with pytest
```

## 🔧 Migrations with Alembic

Alembic is preconfigured with SQLModel support.

To create a migration files:

```bash
make migrations msg="add SomeModel"
```

To upgrade/downgrade

```bash
make upgrade_all
```

For more commands, take a look at `Makefile`. Play around!

## 🐚 Interactive Shell

### For those who love django shell

To start shell:

```bash
# at src/backend/
make shell
```

You can customize the behaviour by modifying `scripts/shell.py`

Shell comes preloaded with:

- session: SQLModel sync session

- async_session: async session factory

- arun(coro): run async functions

- Your models (e.g., SomeModel, etc.)

## 🧪 Unittesting

We're using `pytest` for running tests, `factory-boy` for factories.

To run all tests

```bash
make test_all
```
