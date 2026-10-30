# Module: `core_access` (`erp.core.access`)

**Status:** ✅ Foundation done (models + RBAC seed + permission class)  
**Product PRD:** [access-control](../../../docs/04-erp-core/access-control/PRD.md)  
**Last updated:** 2026-10-29

---

## Purpose

ERP permissions, roles, and scoped user–role assignments. Enforces `required_permission` on views via `HasERPPermission`.

---

## Models

| Model | Table | Notes |
|-------|-------|-------|
| `Permission` | `core_access_permission` | Stable string `code` |
| `Role` | `core_access_role` | `code`, `name` |
| `RolePermission` | `core_access_rolepermission` | M2M through table |
| `UserRoleAssignment` | `core_access_userroleassignment` | `scope_json` (e.g. `firm_ids`) |

**Migrations:** `0001_initial.py`, `0002_initial.py`

---

## Permissions (seeded)

Organisation suite only today — see `seed_rbac`:

- `organisation.firm.view|manage`
- `organisation.project.view|manage`
- `organisation.site.view|manage`
- `organisation.store.view|manage`
- `organisation.cost_code.view|manage`

**Roles:** Owner, ProjectManager, SiteSupervisor, StoreKeeper

---

## API

_No public REST routes yet._ `api/urls.py` is included but empty. Assignment/admin APIs pending.

---

## Services & selectors

- **`services/access.py`:** `user_has_permission(user, code)` with scope evaluation
- **`api/permissions.py`:** `HasERPPermission`

---

## Integrations

- **Used by:** `core_organization` viewsets set `required_permission`

---

## Tests

| File | Scenarios |
|------|-----------|
| `tests/test_organization_api.py` | 403 without permission; success with Owner |

---

## Open items

- [ ] REST APIs for roles, assignments, permission catalog
- [ ] Expand permission codes per module as L2/L3 ship
- [ ] Document `scope_json` schema in domain model doc
