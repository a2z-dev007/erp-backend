"""Seed master-prompt entities (≥SEED_COUNT rows each)."""

from __future__ import annotations

from datetime import date, timedelta
from decimal import Decimal

from django.utils import timezone

from erp.core.approvals.models import WorkflowDefinition
from erp.core.organization.models import Branch, Department
from erp.extensions.construction.attendance.models import SiteAttendance
from erp.extensions.construction.boq.models import Boq, BoqLine
from erp.extensions.construction.client_billing.models import ClientBill, RetentionRecord
from erp.extensions.construction.contractors.models import SubcontractorBill, WorkOrder
from erp.extensions.construction.equipment.models import EquipmentAsset
from erp.extensions.construction.measurement.models import MeasurementBook, WorkPackage
from erp.extensions.construction.quality.models import QualityInspection
from erp.extensions.construction.requests.models import MaterialRequest, MaterialRequestLine
from erp.extensions.construction.variations.models import ProjectProgressRecord, VariationOrder
from erp.modules.assets.models import FixedAsset
from erp.modules.crm.models import Customer
from erp.modules.finance.models import GLEntry, LedgerAccount, Payment, TaxCategory, Voucher
from erp.modules.hr.models import Employee
from erp.modules.inventory.models import Item, StockLedgerEntry
from erp.modules.procurement.models import GoodsReceiptNote, PurchaseInvoice, PurchaseOrder, Vendor
from erp.modules.sales.models import ClientContract, SalesInvoice, SalesOrder

SEED_COUNT = 10


def seed_master_entities(
    *,
    hq_firm,
    hq_project,
    hq_site,
    hq_store,
    items: list[Item],
    today: date,
) -> dict[str, int]:
    counts: dict[str, int] = {}

    branch = None
    dept = None
    for i in range(1, SEED_COUNT + 1):
        branch, _ = Branch.objects.update_or_create(
            firm=hq_firm,
            code=f"BR-{i:02d}",
            defaults={"name": f"Branch {i}", "city": "Bengaluru"},
        )
        dept, _ = Department.objects.update_or_create(
            firm=hq_firm,
            code=f"DEPT-{i:02d}",
            defaults={"name": f"Department {i}", "branch": branch},
        )
    counts["branches"] = SEED_COUNT
    counts["departments"] = SEED_COUNT

    customers: list[Customer] = []
    for i in range(1, SEED_COUNT + 1):
        c, _ = Customer.objects.update_or_create(
            firm=hq_firm,
            code=f"CUST-{i:03d}",
            defaults={"name": f"Customer {i}", "gstin": f"29CUST{i:05d}F1Z5", "billing_city": "Mumbai"},
        )
        customers.append(c)
    counts["customers"] = SEED_COUNT

    for i in range(1, SEED_COUNT + 1):
        Employee.objects.update_or_create(
            firm=hq_firm,
            code=f"EMP-{i:03d}",
            defaults={
                "full_name": f"Employee {i}",
                "job_title": "Site Engineer",
                "department": dept,
            },
        )
    counts["employees"] = SEED_COUNT

    for i in range(1, SEED_COUNT + 1):
        SalesOrder.objects.update_or_create(
            firm=hq_firm,
            code=f"SO-{i:04d}",
            defaults={"customer": customers[i - 1], "total_inr": Decimal(100_000 + i * 10_000), "status": "confirmed"},
        )
        SalesInvoice.objects.update_or_create(
            firm=hq_firm,
            code=f"SINV-{i:04d}",
            defaults={
                "customer": customers[i - 1],
                "invoice_date": today - timedelta(days=i),
                "total_inr": Decimal(100_000 + i * 10_000),
                "status": "posted",
            },
        )
        ClientContract.objects.update_or_create(
            firm=hq_firm,
            code=f"CC-{i:03d}",
            defaults={
                "project": hq_project,
                "name": f"Client contract {i}",
                "contract_value_inr": Decimal(5_000_000 + i * 500_000),
            },
        )
    counts["sales_orders"] = SEED_COUNT
    counts["sales_invoices"] = SEED_COUNT
    counts["client_contracts"] = SEED_COUNT

    vendors = list(Vendor.objects.filter(firm=hq_firm).order_by("code")[:SEED_COUNT])
    pos = list(PurchaseOrder.objects.filter(firm=hq_firm).order_by("code")[:SEED_COUNT])
    for i in range(1, SEED_COUNT + 1):
        GoodsReceiptNote.objects.update_or_create(
            firm=hq_firm,
            code=f"GRN-{i:04d}",
            defaults={
                "purchase_order": pos[i - 1] if i - 1 < len(pos) else None,
                "received_on": today - timedelta(days=i),
                "status": "posted",
            },
        )
        PurchaseInvoice.objects.update_or_create(
            firm=hq_firm,
            code=f"PINV-{i:04d}",
            defaults={
                "vendor": vendors[i - 1] if i - 1 < len(vendors) else None,
                "invoice_date": today - timedelta(days=i),
                "amount_inr": Decimal(75_000 + i * 5_000),
                "status": "posted",
            },
        )
    counts["grns"] = SEED_COUNT
    counts["purchase_invoices"] = SEED_COUNT

    accounts: list[LedgerAccount] = []
    for i in range(1, SEED_COUNT + 1):
        TaxCategory.objects.update_or_create(
            firm=hq_firm,
            code=f"GST-{i:02d}",
            defaults={"name": f"GST slab {i}", "rate_percent": Decimal(18 if i % 2 else 5)},
        )
        acc, _ = LedgerAccount.objects.update_or_create(
            firm=hq_firm,
            code=f"ACC-{i:03d}",
            defaults={"name": f"Ledger account {i}", "account_type": "expense"},
        )
        accounts.append(acc)
        Payment.objects.update_or_create(
            firm=hq_firm,
            code=f"PAY-{i:04d}",
            defaults={
                "payment_date": today - timedelta(days=i),
                "amount_inr": Decimal(20_000 + i * 2_000),
                "direction": "out" if i % 2 else "in",
            },
        )
        WorkflowDefinition.objects.update_or_create(
            firm=hq_firm,
            code=f"WF-{i:02d}",
            defaults={"name": f"Workflow {i}", "module_key": "procurement"},
        )
        FixedAsset.objects.update_or_create(
            firm=hq_firm,
            code=f"FA-{i:03d}",
            defaults={
                "name": f"Fixed asset {i}",
                "purchase_date": today - timedelta(days=365 + i),
                "value_inr": Decimal(500_000 + i * 50_000),
            },
        )
        EquipmentAsset.objects.update_or_create(
            firm=hq_firm,
            code=f"EQ-{i:03d}",
            defaults={"name": f"Excavator {i}", "equipment_type": "plant"},
        )
    counts["tax_categories"] = SEED_COUNT
    counts["ledger_accounts"] = SEED_COUNT
    counts["payments"] = SEED_COUNT
    counts["workflows"] = SEED_COUNT
    counts["fixed_assets"] = SEED_COUNT
    counts["equipment"] = SEED_COUNT

    vouchers = list(Voucher.objects.filter(firm=hq_firm).order_by("voucher_number")[:SEED_COUNT])
    for i, acc in enumerate(accounts, start=1):
        GLEntry.objects.update_or_create(
            firm=hq_firm,
            account=acc,
            entry_date=today - timedelta(days=i),
            debit_inr=Decimal(1000 * i),
            defaults={
                "voucher": vouchers[i - 1] if i - 1 < len(vouchers) else None,
                "credit_inr": Decimal(0),
                "narration": f"Seed GL {i}",
            },
        )
    counts["gl_entries"] = len(accounts)

    if hq_store and items:
        now = timezone.now()
        for i, item in enumerate(items, start=1):
            StockLedgerEntry.objects.update_or_create(
                store=hq_store,
                item=item,
                document_type="opening",
                document_id=item.id,
                defaults={"qty_delta": Decimal(10 * i), "occurred_at": now - timedelta(hours=i)},
            )
        counts["stock_ledger_entries"] = len(items)

    boqs = list(Boq.objects.filter(project=hq_project).order_by("code")[:SEED_COUNT])
    for i, boq in enumerate(boqs, start=1):
        BoqLine.objects.update_or_create(
            boq=boq,
            line_no=i,
            defaults={"description": f"BOQ line {i}", "qty": Decimal(i * 10), "rate_inr": Decimal(500 + i * 50)},
        )
    counts["boq_lines"] = len(boqs)

    for i in range(1, SEED_COUNT + 1):
        WorkPackage.objects.update_or_create(
            project=hq_project,
            code=f"WP-{i:02d}",
            defaults={"name": f"Work package {i}"},
        )
        VariationOrder.objects.update_or_create(
            project=hq_project,
            code=f"VO-{i:03d}",
            defaults={"title": f"Variation {i}", "amount_inr": Decimal(150_000 + i * 10_000)},
        )
        ProjectProgressRecord.objects.update_or_create(
            project=hq_project,
            code=f"PRG-{i:03d}",
            defaults={"progress_pct": Decimal(min(100, i * 9)), "recorded_on": today - timedelta(days=i)},
        )
    counts["work_packages"] = SEED_COUNT
    counts["variation_orders"] = SEED_COUNT
    counts["progress_records"] = SEED_COUNT

    wo = WorkOrder.objects.filter(firm=hq_firm).order_by("code").first()
    if wo:
        for i in range(1, SEED_COUNT + 1):
            SubcontractorBill.objects.update_or_create(
                firm=hq_firm,
                code=f"SB-{i:04d}",
                defaults={
                    "work_order": wo,
                    "bill_date": today - timedelta(days=i),
                    "gross_inr": Decimal(200_000 + i * 15_000),
                    "retention_inr": Decimal(10_000 + i),
                },
            )
        counts["subcontractor_bills"] = SEED_COUNT

    bills = list(ClientBill.objects.filter(project=hq_project).order_by("code")[:SEED_COUNT])
    for i, bill in enumerate(bills, start=1):
        RetentionRecord.objects.update_or_create(
            client_bill=bill,
            defaults={
                "amount_inr": Decimal(25_000 + i * 1_000),
                "release_due_on": today + timedelta(days=90 + i),
                "released": i % 5 == 0,
            },
        )
    counts["retention_records"] = len(bills)

    mrs = list(MaterialRequest.objects.filter(site=hq_site).order_by("code")[:SEED_COUNT])
    for i, mr in enumerate(mrs):
        if i < len(items):
            MaterialRequestLine.objects.update_or_create(
                material_request=mr,
                item=items[i],
                defaults={"qty": Decimal(5 + i)},
            )
    counts["material_request_lines"] = min(len(mrs), len(items))

    employees = list(Employee.objects.filter(firm=hq_firm).order_by("code")[:SEED_COUNT])
    for i, emp in enumerate(employees, start=1):
        SiteAttendance.objects.update_or_create(
            site=hq_site,
            employee=emp,
            attendance_date=today - timedelta(days=i),
            defaults={"status": "present"},
        )
        QualityInspection.objects.update_or_create(
            site=hq_site,
            code=f"QI-{i:03d}",
            defaults={"inspected_on": today - timedelta(days=i), "result": "pass" if i % 4 else "fail"},
        )
    counts["site_attendance"] = len(employees)
    counts["quality_inspections"] = SEED_COUNT

    return counts
