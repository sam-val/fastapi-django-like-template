# FastAPI Django-like Template

A project template for structuring FastAPI apps like a Django project — modular, scalable, and clean.


## ✨ Features

- Django-style folder layout (`apps/`, `api/`, `config/`)
- Versioned APIs (`v1`, `v2`, etc.)
- [`poetry`](https://python-poetry.org/) for dependency management
- [`alembic`](https://alembic.sqlalchemy.org/) for database migrations
- [`pytest`](https://docs.pytest.org/) for testing
- Built-in support for [`pre-commit`](https://pre-commit.com/)
- IPython shell (`make shell`) similar to Django's shell
- Developer-friendly `Makefile` commands for common tasks

## 🛠️ Installation

> This project uses **Python 3.13**, but you can change to any version you prefer.

### 🔧 Install Poetry

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

#### To add new python package, instead of pip just do:
```bash
# this will update poetry.lock, commit this file to version control too

# at src/backend, same dir as pyproject.toml
poetry add <package-name>

# e.g poetry add alembic
```

#### You can also install pre-commit hooks (come with black, isort, flak8)
```bash
poetry run pre-commit install
```

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
├── README.md
├── poetry.lock
├── pyproject.toml
├── src
│   └── backend
│       ├── Makefile
│       ├── alembic
│       │   ├── README
│       │   ├── env.py
│       │   ├── script.py.mako
│       │   └── versions
│       │       └── 7235dcd2cce6_example_migration_file_alembic.py
│       ├── alembic.ini
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
│       │   └── world
│       │       ├── apis
│       │       │   └── v1
│       │       │       └── views.py
│       │       ├── models.py
│       │       ├── repository.py
│       │       ├── schemas.py
│       │       ├── selectors.py
│       │       ├── services.py
│       │       └── tests
│       ├── common
│       │   └── mixins
│       │       └── models.py
│       ├── config
│       │   ├── db.py
│       │   ├── settings.py
│       │   └── urls.py
│       ├── main.py
│       └── scripts
│           └── shell.py
├── tests
└── tox.ini

```
## File Responsibilities

Each subapp in `apps/` (e.g. `hello_world`, `voting`) follows this common structure:

- **models.py** – Defines database models using SQLModel.
- **schemas.py** – Defines request and response validation schemas (Pydantic models). Same as Django REST Framework serializers.
- **selectors.py** – Read-only data access patterns (e.g. list filters, aggregations).
- **services.py** – Business logic layer, combines repositories/selectors to implement use cases.
- **repository.py** (optional) – Low-level database queries. Used by Selectors & Services.
- **apis/`<version>`/views.py** – HTTP route handlers for versioned APIs, similar to Django views.

This modular structure ensures separation of concerns, testability, and scalability.


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
# at src/backend/
make migrations msg="add SomeModel"
```

To upgrade/downgrade
```bash
# at src/backend/
make upgrade_all
```

## 🐚 Interactive Shell

```bash
# at src/backend/
make shell
```

Preloaded
- session: SQLModel sync session

- async_session: async session factory

- arun(coro): run async functions

- Your models (e.g., SomeModel, etc.)

## 🧪 Testing

To be added

---

Feel free to fork this and adapt it for your team or project.
