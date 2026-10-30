# Prince ERP — Django Backend

Modular monolith API (Django 5 + DRF) for the construction ERP. Architecture: [docs/01-architecture/django-application-structure.md](../docs/01-architecture/django-application-structure.md).

**Implementation handbook (update as you build modules):** [docs/README.md](docs/README.md)  
**API by module:** [docs/API_REFERENCE.md](docs/API_REFERENCE.md) · **AI / project context:** [../CONTEXT.md](../CONTEXT.md)

## Prerequisites

- Python 3.12+ (3.14 tested)
- Docker Desktop (recommended for PostgreSQL, Redis, MinIO)

## Quick start

### 1. Environment

```bash
cd backend
cp .env.example .env
```

Edit `.env` if needed. **Default is SQLite** (`USE_SQLITE=true`, `db.sqlite3`) — no Docker required for migrate/seed/runserver.

For PostgreSQL: `docker compose up -d`, then set `USE_SQLITE=false` and `DATABASE_URL=postgres://erp:erp@localhost:5432/erp_dev`.

### 2. Start infrastructure

```bash
docker compose up -d
```

Services: Postgres `:5432`, Redis `:6379`, MinIO `:9000` (console `:9001`).

### 3. Python environment

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 4. Database and seed data

```bash
export DJANGO_SETTINGS_MODULE=config.settings.local
python manage.py migrate
python manage.py seed_all
```

`seed_all` runs `seed_rbac` when needed, then loads **10+ rows per module** (firms, items, POs, vouchers, construction data, etc.).

**Demo login:** `owner@demo.local` / `demo1234` (also `user01@demo.local` … `user09@demo.local`, same password).

Legacy minimal org seed: `python manage.py seed_demo` (optional; superseded by `seed_all`).

### 5. Run API

```bash
python manage.py runserver
```

| URL | Purpose |
|-----|---------|
| http://127.0.0.1:8000/api/v1/health/ | Health check |
| http://127.0.0.1:8000/api/v1/docs/ | Swagger UI |
| http://127.0.0.1:8000/admin/ | Django admin |

### 6. Example: login + list firms

```bash
curl -c cookies.txt -H "Content-Type: application/json" \
  -d '{"email":"owner@demo.local","password":"demo1234"}' \
  http://127.0.0.1:8000/api/v1/auth/login/

curl -b cookies.txt http://127.0.0.1:8000/api/v1/organisation/firms/
```

Login returns a **`token`** in `data` (DRF token auth). Use it in Swagger **Authorize** or:

```bash
curl -H "Authorization: Token YOUR_TOKEN_HERE" http://127.0.0.1:8000/api/v1/users/me/
```

## Package layout (`erp/`)

| Path | Layer | Django label | Status |
|------|-------|--------------|--------|
| `erp/core/identity` | L1 | `core_identity` | Auth, custom User |
| `erp/core/access` | L1 | `core_access` | Roles, `seed_rbac` |
| `erp/core/organization` | L1 | `core_organization` | Org CRUD APIs |
| `erp/core/*` (approvals, audit, …) | L1 | `core_*` | Placeholder |
| `erp/modules/*` | L2 | `mod_*` | Placeholder |
| `erp/extensions/construction/*` | L3 | `ext_construction_*` | Placeholder |
| `erp/common/` | — | (not an app) | Envelope, pagination, base models |

Details: [erp/README.md](erp/README.md)

Enable/disable L2/L3 via `.env`:

```env
ERP_MODULES=inventory,procurement,finance,construction
```

## Tests

Tests always use **in-memory SQLite** (`config.settings.test`) — not Postgres and not your local `db.sqlite3`.

```bash
pytest
```

If your `.env` still has Postgres, pytest is unaffected. To run migrate/seed against a file DB locally, use default `local` settings (SQLite `db.sqlite3`).

## Celery (optional)

```bash
celery -A config.celery worker -l info
```

Requires Redis from `docker compose`.

## Connect Next.js frontend

Set in the frontend app (when adapter is ready):

```env
NEXT_PUBLIC_DATA_SOURCE=http
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000/api/v1
```

API uses **snake_case** JSON; map to frontend Zod **camelCase** in the HTTP adapter.

## Project structure

```text
backend/
├── config/                settings, urls, celery
├── erp/
│   ├── common/            shared utilities (not a Django app)
│   ├── core/              L1 Django apps
│   ├── modules/           L2 Django apps
│   └── extensions/        L3 Django apps (construction/…)
└── tests/
```
