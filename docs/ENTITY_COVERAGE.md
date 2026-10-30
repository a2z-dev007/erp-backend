# Master prompt entity coverage (§11, lines 589–636)

**Tenant:** intentionally omitted (single deployment; use **Firm** as company).

| Entity (master prompt) | Prince model | API list | Seed ≥10 |
|------------------------|--------------|----------|----------|
| Company | `Firm` | `organisation/firms/` | Yes |
| Branch | `Branch` | `organisation/branches/` | Yes |
| Department | `Department` | `organisation/departments/` | Yes |
| User | `User` | `users/` | Yes |
| Role | `Role` | `access/roles/` | Yes |
| Customer | `Customer` | `crm/customers/` | Yes |
| Supplier | `Vendor` | `procurement/vendors/` | Yes |
| Employee | `Employee` | `hr/employees/` | Yes |
| Item | `Item` | `inventory/items/` | Yes |
| Warehouse | `Store` | `organisation/stores/` | Yes (via org seed) |
| Project | `Project` | `organisation/projects/` | Yes |
| Contract | `ClientContract` | `sales/contracts/` | Yes |
| Budget | `ProjectBudget` | `construction/project-budgets/` | Yes |
| Sales Order | `SalesOrder` | `sales/orders/` | Yes |
| Purchase Order | `PurchaseOrder` | `procurement/purchase-orders/` | Yes |
| Goods Receipt | `GoodsReceiptNote` | `procurement/grns/` | Yes |
| Sales Invoice | `SalesInvoice` | `sales/invoices/` | Yes |
| Purchase Invoice | `PurchaseInvoice` | `procurement/purchase-invoices/` | Yes |
| Payment | `Payment` | `finance/payments/` | Yes |
| Journal Entry | `Voucher` | `finance/vouchers/` | Yes |
| General Ledger Entry | `GLEntry` | `finance/gl-entries/` | Yes |
| Stock Ledger Entry | `StockLedgerEntry` | `inventory/stock-ledger/` | Yes |
| Cost Center | `CostCode` | `organisation/cost-codes/` | Yes |
| Tax Category | `TaxCategory` | `finance/tax-categories/` | Yes |
| Fixed Asset | `FixedAsset` | `assets/fixed-assets/` | Yes |
| Workflow | `WorkflowDefinition` | `approvals/workflows/` | Yes |
| Audit Log | `AuditEvent` | `audit/events/` | Yes |

### Construction-specific (§11 continuation)

| Entity | Model | API |
|--------|-------|-----|
| Site | `Site` | `organisation/sites/` |
| BOQ | `Boq` | `construction/boqs/` |
| BOQ Item | `BoqLine` | `construction/boq-lines/` |
| Cost Code | `CostCode` | `organisation/cost-codes/` |
| Project Budget | `ProjectBudget` | `construction/project-budgets/` |
| Work Package | `WorkPackage` | `construction/work-packages/` |
| Measurement Record | `MeasurementBook` | `construction/measurement-books/` |
| Subcontractor WO | `WorkOrder` | `construction/work-orders/` |
| Subcontractor Bill | `SubcontractorBill` | `construction/subcontractor-bills/` |
| Material Requisition | `MaterialRequest` | `construction/material-requests/` |
| Site Consumption | `MaterialConsumption` | `construction/material-consumptions/` |
| Retention | `RetentionRecord` | `construction/retention-records/` |
| Progress | `ProjectProgressRecord` | `construction/progress-records/` |
| Variation Order | `VariationOrder` | `construction/variation-orders/` |
| Equipment | `EquipmentAsset` | `construction/equipment/` |
| Site attendance | `SiteAttendance` | `construction/site-attendance/` |
| QA inspection | `QualityInspection` | `construction/quality-inspections/` |

**Not in scope:** Payroll / wages (`Employee` master only). **Implementation level:** scaffold (read list + seed); posting, approvals, and line-level business rules are next phases.
