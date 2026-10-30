# Prince ERP — API reference (by module)

**Base URL (local):** `http://127.0.0.1:8000/api/v1/`  
**Interactive docs:** [Swagger UI](/api/v1/docs/) · **OpenAPI JSON:** `/api/v1/schema/`  
**Last updated:** 2026-10-29

---

## Conventions

| Topic | Detail |
|--------|--------|
| **Auth** | Session cookie (browser) or `Authorization: Token <key>` from login |
| **Login** | `POST /api/v1/auth/login/` → `{ "data": { "token", "email", ... } }` |
| **Success shape** | `{ "data": ..., "meta": { "request_id", ... } }` |
| **Errors** | `{ "error": { "code", "message", "fields" }, "meta": { "request_id" } }` |
| **Pagination** | List endpoints use `?page=` and `?page_size=`; paginated `data` includes `results`, `meta.page`, `meta.total` |
| **Filters** | Many lists support `?firm_id=`, `?project_id=`, `?site_id=` where applicable |
| **JSON** | **snake_case** field names |
| **CRUD vs read** | **Organisation** (firms, projects, sites, stores, cost codes) = full CRUD + RBAC. Most other modules = **GET list + GET detail** (scaffold phase) |

**Demo data:** `python manage.py seed_all` (runs migrate + seeds 10+ rows per resource).  
**Demo user:** `owner@demo.local` / `demo1234`

**Enable modules in `.env`:**

```env
ERP_MODULES=inventory,procurement,finance,crm,sales,hr,assets,construction
```

---

## Platform

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/health/` | No | DB connectivity check |

---

## L1 — Identity & access

### `core_identity` — User management

| Method | Path | Auth | Notes |
|--------|------|------|--------|
| POST | `/auth/login/` | No | Body: `{ "email", "password" }` → user + **token** |
| POST | `/auth/logout/` | Yes | Clears session; deletes token |
| GET | `/users/me/` | Yes | Current user profile |
| GET | `/users/` | Yes | List users |
| GET | `/users/{id}/` | Yes | User detail |

### `core_access` — Roles & permissions

| Method | Path | Auth |
|--------|------|------|
| GET | `/access/permissions/` | Yes |
| GET | `/access/permissions/{id}/` | Yes |
| GET | `/access/roles/` | Yes |
| GET | `/access/roles/{id}/` | Yes |

---

## L1 — Organisation (`core_organization`)

Base path: **`/organisation/`**  
Permissions: `organisation.*.view` / `organisation.*.manage` (see `seed_rbac`).

| Resource | List | Create | Update | Delete |
|----------|------|--------|--------|--------|
| Branches | GET `branches/` | — | — | — |
| Departments | GET `departments/` | — | — | — |
| Firms | GET `firms/` | POST | PUT/PATCH | DELETE |
| Projects | GET `projects/` | POST | PUT/PATCH | DELETE |
| Sites | GET `sites/` | POST | PUT/PATCH | DELETE |
| Stores | GET `stores/` | POST | PUT/PATCH | DELETE |
| Cost codes | GET `cost-codes/` | POST | PUT/PATCH | DELETE |

Query examples: `?firm_id=`, `?project_id=`, `?site_id=`, `?q=` (search on supported resources).

> **Note:** Branch and department are **read-only list** in API today; firms/projects/sites/stores/cost codes support full CRUD.

---

## L1 — Core platform services

### `core_approvals`

| Method | Path |
|--------|------|
| GET | `/approvals/workflows/` |
| GET | `/approvals/workflows/{id}/` |
| GET | `/approvals/requests/` |
| GET | `/approvals/requests/{id}/` |

### `core_audit`

| Method | Path |
|--------|------|
| GET | `/audit/events/` |
| GET | `/audit/events/{id}/` |

### `core_documents`

| Method | Path |
|--------|------|
| GET | `/documents/` |
| GET | `/documents/{id}/` |

### `core_sequences`

| Method | Path |
|--------|------|
| GET | `/sequences/` |
| GET | `/sequences/{id}/` |

### `core_imports`

| Method | Path |
|--------|------|
| GET | `/imports/batches/` |
| GET | `/imports/batches/{id}/` |

### `core_notifications`

| Method | Path |
|--------|------|
| GET | `/notifications/` |
| GET | `/notifications/{id}/` |

Scoped to **current user** for list.

---

## L2 — CRM (`mod_crm`)

| Method | Path | Model |
|--------|------|--------|
| GET | `/crm/customers/` | Customer |
| GET | `/crm/customers/{id}/` | |
| GET | `/crm/leads/` | Lead |
| GET | `/crm/leads/{id}/` | |

---

## L2 — Sales (`mod_sales`)

| Method | Path | Model |
|--------|------|--------|
| GET | `/sales/orders/` | SalesOrder |
| GET | `/sales/orders/{id}/` | |
| GET | `/sales/invoices/` | SalesInvoice |
| GET | `/sales/invoices/{id}/` | |
| GET | `/sales/contracts/` | ClientContract |
| GET | `/sales/contracts/{id}/` | |

---

## L2 — HR (`mod_hr`)

| Method | Path | Model |
|--------|------|--------|
| GET | `/hr/employees/` | Employee |
| GET | `/hr/employees/{id}/` | |

Payroll / wages **not** in scope.

---

## L2 — Fixed assets (`mod_assets`)

| Method | Path | Model |
|--------|------|--------|
| GET | `/assets/fixed-assets/` | FixedAsset |
| GET | `/assets/fixed-assets/{id}/` | |

---

## L2 — Inventory (`mod_inventory`)

| Method | Path | Model |
|--------|------|--------|
| GET | `/inventory/items/` | Item |
| GET | `/inventory/items/{id}/` | |
| GET | `/inventory/stock/` | StockBalance |
| GET | `/inventory/stock/{id}/` | |
| GET | `/inventory/stock-ledger/` | StockLedgerEntry |
| GET | `/inventory/stock-ledger/{id}/` | |

---

## L2 — Procurement (`mod_procurement`)

| Method | Path | Model |
|--------|------|--------|
| GET | `/procurement/vendors/` | Vendor (supplier) |
| GET | `/procurement/vendors/{id}/` | |
| GET | `/procurement/purchase-orders/` | PurchaseOrder |
| GET | `/procurement/purchase-orders/{id}/` | |
| GET | `/procurement/grns/` | GoodsReceiptNote |
| GET | `/procurement/grns/{id}/` | |
| GET | `/procurement/purchase-invoices/` | PurchaseInvoice |
| GET | `/procurement/purchase-invoices/{id}/` | |

---

## L2 — Finance (`mod_finance`)

| Method | Path | Model |
|--------|------|--------|
| GET | `/finance/vouchers/` | Voucher (journal header) |
| GET | `/finance/vouchers/{id}/` | |
| GET | `/finance/ledger-accounts/` | LedgerAccount |
| GET | `/finance/ledger-accounts/{id}/` | |
| GET | `/finance/gl-entries/` | GLEntry |
| GET | `/finance/gl-entries/{id}/` | |
| GET | `/finance/payments/` | Payment |
| GET | `/finance/payments/{id}/` | |
| GET | `/finance/tax-categories/` | TaxCategory |
| GET | `/finance/tax-categories/{id}/` | |

---

## L3 — Construction extension

All paths prefixed with **`/construction/`**. Requires `construction` in `ERP_MODULES`.

### Material requests (`ext_construction_requests`)

| Method | Path | Model |
|--------|------|--------|
| GET | `/construction/material-requests/` | MaterialRequest |
| GET | `/construction/material-request-lines/` | MaterialRequestLine |

### Subcontractors (`ext_construction_contractors`)

| Method | Path | Model |
|--------|------|--------|
| GET | `/construction/contractors/` | ContractorParty |
| GET | `/construction/work-orders/` | WorkOrder |
| GET | `/construction/subcontractor-bills/` | SubcontractorBill |

### GPS evidence (`ext_construction_evidence`)

| Method | Path | Model |
|--------|------|--------|
| GET | `/construction/evidence/` | FieldEvidence |

### BOQ (`ext_construction_boq`)

| Method | Path | Model |
|--------|------|--------|
| GET | `/construction/boqs/` | Boq |
| GET | `/construction/boq-lines/` | BoqLine |

### Measurement (`ext_construction_measurement`)

| Method | Path | Model |
|--------|------|--------|
| GET | `/construction/measurement-books/` | MeasurementBook |
| GET | `/construction/work-packages/` | WorkPackage |

### Client billing (`ext_construction_client_billing`)

| Method | Path | Model |
|--------|------|--------|
| GET | `/construction/client-bills/` | ClientBill |
| GET | `/construction/retention-records/` | RetentionRecord |

### Project costing (`ext_construction_costing`)

| Method | Path | Model |
|--------|------|--------|
| GET | `/construction/project-budgets/` | ProjectBudget |

### Material consumption (`ext_construction_consumption`)

| Method | Path | Model |
|--------|------|--------|
| GET | `/construction/material-consumptions/` | MaterialConsumption |

### Equipment (`ext_construction_equipment`)

| Method | Path | Model |
|--------|------|--------|
| GET | `/construction/equipment/` | EquipmentAsset |

### Site attendance (`ext_construction_attendance`)

| Method | Path | Model |
|--------|------|--------|
| GET | `/construction/site-attendance/` | SiteAttendance |

### Quality & safety (`ext_construction_quality`)

| Method | Path | Model |
|--------|------|--------|
| GET | `/construction/quality-inspections/` | QualityInspection |

### Variations & progress (`ext_construction_variations`)

| Method | Path | Model |
|--------|------|--------|
| GET | `/construction/variation-orders/` | VariationOrder |
| GET | `/construction/progress-records/` | ProjectProgressRecord |

---

## Quick test (curl)

```bash
# Login
curl -s -c /tmp/erp.cookies -H "Content-Type: application/json" \
  -d '{"email":"owner@demo.local","password":"demo1234"}' \
  http://127.0.0.1:8000/api/v1/auth/login/

# Use token from response.data.token
export TOKEN="paste-token-here"
curl -s -H "Authorization: Token $TOKEN" http://127.0.0.1:8000/api/v1/organisation/firms/
```

---

## Related docs

- [ENTITY_COVERAGE.md](./ENTITY_COVERAGE.md) — master prompt entities → models  
- [MODULE_REGISTRY.md](./MODULE_REGISTRY.md) — implementation status  
- Product PRDs: [docs/MASTER_ERP_PRD.md](../../docs/MASTER_ERP_PRD.md)
