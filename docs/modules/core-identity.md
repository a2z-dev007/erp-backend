# Module: `core_identity` (`erp.core.identity`)

**Status:** ✅ Foundation done  
**Product PRD:** [user-management](../../../docs/04-erp-core/user-management/PRD.md)  
**Last updated:** 2026-10-29

---

## Purpose

Custom user model and session-based authentication endpoints for browser clients.

---

## Models

| Model | Table | Notes |
|-------|-------|-------|
| `User` | `core_identity_user` | UUID PK; email as `USERNAME_FIELD`; `user_type`; optional `contractor_party_id` |

**Migrations:** `0001_initial.py`

---

## Permissions

Uses Django session auth + global `IsAuthenticated`. No module-specific ERP permission codes on auth endpoints yet.

---

## API

| Method | Path | Permission | Description |
|--------|------|------------|-------------|
| POST | `/api/v1/auth/login/` | AllowAny | Email/password → session |
| POST | `/api/v1/auth/logout/` | Authenticated | Clear session |
| GET | `/api/v1/users/me/` | Authenticated | Current user payload |

---

## Services & selectors

_Login/logout in `api/views.py`. Extend with services when adding registration, password reset, or user admin APIs._

---

## Integrations

- **Depends on:** Django auth session framework
- **Used by:** All authenticated APIs; `organization.Project.manager` FK

---

## Tests

| File | Scenarios |
|------|-----------|
| `tests/test_auth.py` | Login + me |

---

## Deviations from PRD

| Section | Change | Reason |
|---------|--------|--------|
| _TBD_ | User CRUD / invite flows not built | Foundation phase |

---

## Open items

- [ ] User management APIs (list, create, deactivate) per PRD
- [ ] Role assignment APIs (may live in `core_access`)
- [ ] Contractor/client user linking to parties
