# Backend implementation record

Single source for **what exists in `backend/` today** and how it was set up. Update the [Changelog](#changelog) when you ship new module slices.

**Last updated:** 2026-10-29

---

## 1. Scope of this backend

| In scope (foundation) | Not implemented yet |
|----------------------|---------------------|
| Django 5 + DRF modular monolith | Full L2/L3 business workflows |
| Session-cookie auth for browser clients | Next.js HTTP adapter wired to Django |
| Organisation master data CRUD | Approvals inbox, documents/MinIO, imports, notifications |
| RBAC seed + permission checks on org APIs | Inventory, procurement, finance APIs |
| OpenAPI (drf-spectacular), health, envelope JSON | Production `settings/production.py` |
| Docker Compose: Postgres, Redis, MinIO | Celery jobs beyond scaffold |
| Pytest smoke tests (auth + organisation) | End-to-end frontend integration |

**Deployment model (from product docs):** one deployment per client, dedicated database; multi-**firm** inside a deployment — not multi-tenant SaaS v1.

**Stack:** Python 3.12+ (3.14 tested), PostgreSQL (or SQLite for quick local), Redis, MinIO.

---

## 2. Repository layout (production-style `erp` package)

Previous flat `apps/` and `shared/` trees were reorganized into:

```text
backend/
├── config/                 # Django project: settings, urls, celery, wsgi
├── erp/
│   ├── common/             # Cross-cutting code (NOT a Django app)
│   ├── core/               # L1 — always installed
│   ├── modules/            # L2 — toggled via ERP_MODULES
│   └── extensions/
│       └── construction/   # L3 — construction pack
├── tests/
├── docs/                   # This handbook
├── docker-compose.yml
├── requirements.txt
├── pyproject.toml
├── manage.py
└── .env.example
```

**Django convention:** Python import path is dotted (`erp.core.identity`); **app label** stays short (`core_identity`) so table names and migrations remain stable (`core_identity_user`, etc.).

Details: [erp/README.md](../erp/README.md), [docs/01-architecture/django-application-structure.md](../../docs/01-architecture/django-application-structure.md).

---

## 3. Configuration

| Item | Location / notes |
|------|------------------|
| Settings split | `config/settings/base.py`, `local.py`, `test.py` |
| Env loading | `django-environ`, read from `backend/.env` |
| `AUTH_USER_MODEL` | `core_identity.User` |
| `INSTALLED_APPS` | `CORE_APPS` + optional apps from `ERP_MODULES` |
| `ERP_MODULES` default | `inventory,procurement,finance,construction` |
| Time zone | `Asia/Kolkata` |
| API prefix | `/api/v1/` |
| OpenAPI | `/api/v1/schema/`, Swagger UI `/api/v1/docs/` |
| Celery | `config/celery.py`, broker `REDIS_URL` |

**Test settings:** `config/settings/test.py` forces in-memory SQLite so pytest does not require Postgres from `.env`.

---

## 4. Shared platform layer (`erp/common`)

Not registered as a Django app. Provides:

| Component | Path | Role |
|-----------|------|------|
| Base models | `erp/common/models.py` | `UUIDModel`, `TimestampedModel`, `ScopedModel` |
| Request ID | `erp/common/middleware.py` | `RequestIDMiddleware` → `meta.request_id` on responses |
| Pagination | `erp/common/pagination.py` | `ERPPageNumberPagination` (envelope-aware) |
| API envelope | `erp/common/api/responses.py` | Success: `{ data, meta }`; errors: `{ error, meta }` |
| Exception handler | `erp/common/api/exceptions.py` | DRF → ERP error shape |
| Health | `erp/common/api/views.py` | `GET /api/v1/health/` |

**REST framework defaults** (`config/settings/base.py`):

- Authentication: `SessionAuthentication`
- Default permission: `IsAuthenticated`
- Custom exception handler and pagination as above
- JSON renderer only (API)

**CORS / CSRF:** configured for `localhost:3000` with credentials for future Next.js integration.

---

## 5. Registered Django applications (15)

| Layer | Python path | App label | Migrations | API routes |
|-------|-------------|-----------|------------|------------|
| L1 | `erp.core.identity` | `core_identity` | Yes | **Implemented** |
| L1 | `erp.core.access` | `core_access` | Yes | Wired (no public routes yet) |
| L1 | `erp.core.organization` | `core_organization` | Yes | **Implemented** |
| L1 | `erp.core.approvals` | `core_approvals` | No | Placeholder (`urls` empty) |
| L1 | `erp.core.audit` | `core_audit` | No | Placeholder |
| L1 | `erp.core.documents` | `core_documents` | No | Placeholder |
| L1 | `erp.core.sequences` | `core_sequences` | No | Placeholder |
| L1 | `erp.core.imports` | `core_imports` | No | Placeholder |
| L1 | `erp.core.notifications` | `core_notifications` | No | Placeholder |
| L2 | `erp.modules.inventory` | `mod_inventory` | No | Placeholder |
| L2 | `erp.modules.procurement` | `mod_procurement` | No | Placeholder |
| L2 | `erp.modules.finance` | `mod_finance` | No | Placeholder |
| L3 | `erp.extensions.construction.requests` | `ext_construction_requests` | No | Placeholder |
| L3 | `erp.extensions.construction.contractors` | `ext_construction_contractors` | No | Placeholder |
| L3 | `erp.extensions.construction.evidence` | `ext_construction_evidence` | No | Placeholder |

Per-app internal skeleton (all apps): `models/`, `services/`, `selectors/`, `api/` (`serializers`, `views`, `urls`), `apps.py`, `admin.py` where relevant.

**URL wiring:** `config/urls.py` includes every app’s `api.urls` under `/api/v1/` (placeholders export empty `urlpatterns`).

---

## 6. Implemented domain and APIs

### 6.1 Identity (`erp.core.identity`)

- **Model:** `User` — UUID PK, email login, `full_name`, `user_type` (internal / contractor / client), optional `contractor_party_id`, staff/active flags.
- **Admin:** registered.
- **Endpoints:**

| Method | Path | Notes |
|--------|------|--------|
| POST | `/api/v1/auth/login/` | Session login (email + password) |
| POST | `/api/v1/auth/logout/` | Session logout |
| GET | `/api/v1/users/me/` | Current user profile |

Product PRD: [docs/04-erp-core/user-management/PRD.md](../../docs/04-erp-core/user-management/PRD.md)

### 6.2 Access control (`erp.core.access`)

- **Models:** `Permission`, `Role`, `RolePermission`, `UserRoleAssignment` (`scope_json` for firm/project scoping).
- **Permission class:** `HasERPPermission` — views set `required_permission` (e.g. `organisation.firm.view`).
- **Service:** `user_has_permission(user, code)` considers role assignments and scope.
- **Management command:** `python manage.py seed_rbac` — seeds organisation permissions and roles: Owner, ProjectManager, SiteSupervisor, StoreKeeper.

Product PRD: [docs/04-erp-core/access-control/PRD.md](../../docs/04-erp-core/access-control/PRD.md)

### 6.3 Organisation (`erp.core.organization`)

- **Models:** `Firm`, `Project`, `Site`, `Store`, `CostCode` — hierarchy Firm → Project → Site → Store; cost codes scoped to firm; UUID + timestamps.
- **Selectors:** scoped listing/filtering by user’s `scope_json`.
- **ViewSets:** DRF routers under `/api/v1/organisation/`:

| Resource | Path prefix |
|----------|-------------|
| Firms | `firms/` |
| Projects | `projects/` |
| Sites | `sites/` |
| Stores | `stores/` |
| Cost codes | `cost-codes/` |

- **Management command:** `python manage.py seed_demo` — demo superuser and sample org tree.

Product PRD: [docs/04-erp-core/organization-settings/PRD.md](../../docs/04-erp-core/organization-settings/PRD.md)

**Demo credentials:** `owner@demo.local` / `demo1234` (after `seed_rbac` + `seed_demo`).

---

## 7. Infrastructure (Docker Compose)

| Service | Port | Purpose |
|---------|------|---------|
| PostgreSQL 16 | 5432 | Primary DB (`erp` / `erp` / `erp_dev`) |
| Redis 7 | 6379 | Celery broker (future) |
| MinIO | 9000, console 9001 | Object storage (future documents module) |

---

## 8. Tests

Run:

```bash
cd backend
DJANGO_SETTINGS_MODULE=config.settings.test pytest
```

| File | Coverage |
|------|----------|
| `tests/test_auth.py` | Login + `/users/me/` |
| `tests/test_organization_api.py` | Permission denied without role; firm list with Owner role |
| `tests/conftest.py` | `seeded_rbac` fixture |

**Status:** 4 tests passing (as of 2026-10-29).

---

## 9. Documentation and learning assets elsewhere in the repo

| Path | Role |
|------|------|
| `docs/` | Product PRDs, architecture, QA, delivery (~104 markdown files) |
| `docs/MASTER_ERP_PRD.md` | Product entry point |
| `docs/DOCUMENTATION_INDEX.md` | Index of all product docs |
| `docs/PROGRESS.md` | High-level doc + backend milestone note |
| `erp-learning/` | Vite + React lab (JSON fixtures, ERD, module catalog) |
| `frontend/` | Next.js PWA (still on json-server; Django not wired) |

---

## 10. Recommended build order (from planning docs)

See [docs/10-implementation-planning/module-build-order.md](../../docs/10-implementation-planning/module-build-order.md):

1. identity + access → organization (**done**)
2. audit + sequences + approvals
3. inventory → construction requests; procurement; contractors
4. finance; documents + evidence; imports; notifications; dashboard API

Track status in [MODULE_REGISTRY.md](./MODULE_REGISTRY.md).

---

## 11. Known gaps and follow-ups

- Placeholder apps have `apps.py` and empty API urls but no models/migrations yet.
- No `config/settings/production.py` hardened profile.
- API JSON is **snake_case**; frontend Zod schemas may use camelCase — adapter needed.
- Payroll and multi-tenant SaaS v1 explicitly out of product scope.
- Open product questions: `docs/00-product-foundation/assumptions-and-open-questions.md` (OQ-001–012).

---

## Changelog

| Date | Summary |
|------|---------|
| 2026-10-29 | Initial Django backend: config, Docker, 15 apps, common envelope layer, identity/auth, access/RBAC seed, organisation CRUD, OpenAPI, pytest smoke tests |
| 2026-10-29 | Reorganized to `erp/core`, `erp/modules`, `erp/extensions`, `erp/common`; updated imports and `INSTALLED_APPS`; tests still pass |
| 2026-10-29 | Added `backend/docs/` handbook (this file, module registry, per-module note stubs) |
| 2026-10-29 | Module demo models + list APIs; `python manage.py seed_all` (10+ rows per module) |
| 2026-10-29 | Added CRM, vendors/stock/work-orders, 5 construction apps (BOQ, MB, client bills, budgets, consumption); [MODULE_GAP_AUDIT.md](./MODULE_GAP_AUDIT.md) |
