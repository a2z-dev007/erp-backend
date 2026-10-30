# Backend module gap audit

**Sources:** [MODULE_REGISTRY.md](./MODULE_REGISTRY.md), [erp-learning/public/data/meta/modules.json](../../erp-learning/public/data/meta/modules.json), [docs/04-erp-core](../docs/04-erp-core/), [docs/06-industry-extensions/construction](../docs/06-industry-extensions/construction/), [ERP master prompt](../../ERP_Learning_and_Commercial_Platform_Design_Master_Prompt.md) (catalog sections — not all 40+ construction topics are separate Django apps in MVP).

**Last updated:** 2026-10-29

---

## Summary

| Layer | Catalog / docs expectation | Backend Django apps | Demo model + list API + `seed_all` (≥10 rows) |
|-------|---------------------------|---------------------|-----------------------------------------------|
| L1 Core | 9 platform apps | 9 under `erp/core/` | Yes (identity org fully CRUD; others read list) |
| L2 Business | inventory, procurement, finance, CRM | 4 under `erp/modules/` | Yes (+ vendors, stock balances) |
| L3 Construction (learning catalog) | 8 extension modules | 8 under `erp/extensions/construction/` | Yes |
| L3 Construction (extra PRDs) | equipment, attendance, QA, reports, … | Not separate apps yet | No — documented only in product `docs/` |

**Run demo data:** `python manage.py seed_all`  
**Enable modules:** `ERP_MODULES=inventory,procurement,finance,crm,construction` (default in `.env.example`).

---

## L1 — Core (`erp/core/`)

| Module | App label | List API prefix | Seed |
|--------|-----------|-----------------|------|
| User management | `core_identity` | `auth/*`, `users/` | 10 users |
| Access control | `core_access` | `access/permissions/`, `access/roles/` | RBAC + 10 roles |
| Organization | `core_organization` | `organisation/*` | 10 firms + tree |
| Approvals | `core_approvals` | `approvals/requests/` | 10 |
| Audit | `core_audit` | `audit/events/` | 10 |
| Documents | `core_documents` | `documents/` | 10 |
| Sequences | `core_sequences` | `sequences/` | 10 |
| Imports | `core_imports` | `imports/batches/` | 10 |
| Notifications | `core_notifications` | `notifications/` | 10 |

**Not separate backend apps (by design):** customer/employee/master-data/reporting PRDs — covered later or via L2/L3.

---

## L2 — Business (`erp/modules/`)

| Module | App label | List API | Seed |
|--------|-----------|----------|------|
| Inventory | `mod_inventory` | `inventory/items/`, `inventory/stock/` | 10 items + 10 balances |
| Procurement | `mod_procurement` | `procurement/vendors/`, `procurement/purchase-orders/` | 10 each |
| Finance | `mod_finance` | `finance/vouchers/` | 10 |
| CRM | `mod_crm` | `crm/leads/` | 10 |

---

## L3 — Construction (`erp/extensions/construction/`)

| Learning catalog ID | App label | List API | Seed |
|--------------------|-----------|----------|------|
| `ext_construction_requests` | `ext_construction_requests` | `construction/material-requests/` | 10 |
| `ext_construction_contractors` | `ext_construction_contractors` | `construction/contractors/`, `construction/work-orders/` | 10 each |
| `ext_construction_evidence` | `ext_construction_evidence` | `construction/evidence/` | 10 |
| `ext_construction_boq` | `ext_construction_boq` | `construction/boqs/` | 10 |
| `ext_construction_measurement` | `ext_construction_measurement` | `construction/measurement-books/` | 10 |
| `ext_construction_client_billing` | `ext_construction_client_billing` | `construction/client-bills/` | 10 |
| `ext_construction_costing` | `ext_construction_costing` | `construction/project-budgets/` | 10 |
| Material consumption (catalog ref) | `ext_construction_consumption` | `construction/material-consumptions/` | 10 |

**Product PRDs not yet as Django apps:** site-management (sites in org), construction-procurement (L2 procurement), equipment, attendance, quality-and-safety, construction-reports, BOQ line detail, RA bill lines, etc. — implement in future slices per [module-build-order](../../docs/10-implementation-planning/module-build-order.md).

---

## Master prompt §5–§6 (40 common + 44 construction topics)

The master prompt is a **learning catalog**, not a 1:1 app list. Mapped to this backend:

- **Common ERP (1–40):** Foundation covered by L1 + L2; manufacturing, POS, HR payroll, multi-currency, etc. are **out of MVP** (see [scope-and-non-goals](../../docs/00-product-foundation/scope-and-non-goals.md)).
- **Construction (1–44):** MVP slices map to L3 apps above; labour/payroll, bank guarantees, DLP, real estate sales, etc. remain **PRD-only** until scoped.

---

## Next implementation priorities

1. Full CRUD + RBAC permissions per module (not only read-only demo APIs).
2. Line models (MR lines, BOQ lines, voucher lines, GL).
3. Workflow posting (GRN, issue, approvals inbox).
4. Optional L3 apps from deferred PRDs when client prioritizes.
