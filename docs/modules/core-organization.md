# Module: `core_organization` (`erp.core.organization`)

**Status:** ✅ Foundation done  
**Product PRD:** [organization-settings](../../../docs/04-erp-core/organization-settings/PRD.md)  
**Last updated:** 2026-10-29

---

## Purpose

Firm → project → site → store hierarchy and firm-scoped cost codes. Primary scope anchor for RBAC.

---

## Models

| Model | Table | Notes |
|-------|-------|-------|
| `Firm` | `core_organization_firm` | `code` unique; PAN/GSTIN; `fy_start_month` |
| `Project` | `core_organization_project` | FK firm; unique `(firm, code)`; optional `manager` user |
| `Site` | `core_organization_site` | FK project; unique `(project, code)` |
| `Store` | `core_organization_store` | FK site |
| `CostCode` | `core_organization_costcode` | FK firm; unique `(firm, code)` |

**Migrations:** `0001_initial.py`

---

## Permissions

All organisation endpoints use `HasERPPermission` with `organisation.*` codes from `seed_rbac`.

---

## API

Base path: `/api/v1/organisation/`

| Resource | Router prefix | ViewSet |
|----------|---------------|---------|
| Firms | `firms/` | `FirmViewSet` |
| Projects | `projects/` | `ProjectViewSet` |
| Sites | `sites/` | `SiteViewSet` |
| Stores | `stores/` | `StoreViewSet` |
| Cost codes | `cost-codes/` | `CostCodeViewSet` |

List responses use ERP envelope + pagination.

---

## Services & selectors

- **`selectors/organization.py`:** Scoped querysets from user role assignments
- **Views:** CRUD via DRF viewsets

---

## Management commands

| Command | Purpose |
|---------|---------|
| `seed_demo` | Demo superuser + sample firm/project/site/store |

---

## Tests

| File | Scenarios |
|------|-----------|
| `tests/test_organization_api.py` | Permission gate; firm list with Owner |

---

## Open items

- [ ] Soft-delete / inactive filtering rules vs PRD
- [ ] Validation for GSTIN/PAN formats
- [ ] Bulk import of org tree (may tie to `core_imports`)
