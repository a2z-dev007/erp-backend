"""Idempotent demo seed: at least SEED_COUNT rows per module API resource."""

from __future__ import annotations

import uuid
from datetime import date, datetime, timedelta
from decimal import Decimal

from django.utils import timezone

from erp.core.access.models import Role, UserRoleAssignment
from erp.core.approvals.models import ApprovalRequest
from erp.core.audit.models import AuditEvent
from erp.core.documents.models import Document
from erp.core.identity.models import User
from erp.core.imports.models import ImportBatch
from erp.core.notifications.models import Notification
from erp.core.organization.models import CostCode, Firm, Project, Site, Store
from erp.core.sequences.models import NumberSequence
from erp.extensions.construction.boq.models import Boq
from erp.extensions.construction.client_billing.models import ClientBill
from erp.extensions.construction.consumption.models import MaterialConsumption
from erp.extensions.construction.contractors.models import ContractorParty, WorkOrder
from erp.extensions.construction.costing.models import ProjectBudget
from erp.extensions.construction.evidence.models import FieldEvidence
from erp.extensions.construction.measurement.models import MeasurementBook
from erp.extensions.construction.requests.models import MaterialRequest
from erp.modules.crm.models import Lead
from erp.modules.finance.models import Voucher
from erp.modules.inventory.models import Item, StockBalance
from erp.common.seed.entity_seed import seed_master_entities
from erp.modules.procurement.models import PurchaseOrder, Vendor

SEED_COUNT = 10

ITEM_NAMES = [
    ("CEM-OPC", "OPC 53 Grade Cement", "BAG", "Civil"),
    ("STL-TMT", "TMT Steel 12mm", "MT", "Steel"),
    ("SND-RC", "River Sand", "CUM", "Civil"),
    ("AGG-20", "20mm Aggregate", "CUM", "Civil"),
    ("BRK-FLY", "Fly Ash Bricks", "NOS", "Masonry"),
    ("PPE-HEL", "Safety Helmet", "NOS", "PPE"),
    ("PNT-EXT", "Exterior Emulsion", "LTR", "Finishing"),
    ("CBL-4C", "4 Core Cable", "MTR", "Electrical"),
    ("PIP-PVC", "PVC Pipe 110mm", "MTR", "Plumbing"),
    ("FMX-TIL", "Floor Tile 600x600", "SQM", "Finishing"),
]

VENDORS = [
    "Shree Cement Distributors",
    "Tata Steel Trade",
    "Local Sand Suppliers",
    "BuildMart Aggregates",
    "Green Brick Co",
    "SafeWorks PPE",
    "Asian Paints Dealer",
    "ElectroHub",
    "FlowPlumb Traders",
    "TileCraft",
]


def run_seed_all() -> dict[str, int]:
    """Seed organisation graph and module demo rows. Returns counts per area."""
    counts: dict[str, int] = {}

    owner, _ = User.objects.update_or_create(
        email="owner@demo.local",
        defaults={
            "full_name": "Demo Owner",
            "user_type": User.UserType.INTERNAL,
            "is_staff": True,
            "is_superuser": True,
            "is_active": True,
        },
    )
    if owner.password == "" or not owner.check_password("demo1234"):
        owner.set_password("demo1234")
        owner.save(update_fields=["password"])

    firms: list[Firm] = []
    projects: list[Project] = []
    sites: list[Site] = []

    for i in range(1, SEED_COUNT + 1):
        code = f"FIRM-{i:02d}"
        firm, _ = Firm.objects.update_or_create(
            code=code,
            defaults={
                "name": f"Demo Construction Co {i}",
                "pan": f"ABCDE{i:04d}F",
                "gstin": f"29ABCDE{i:04d}F1Z5",
                "status": Firm.Status.ACTIVE,
            },
        )
        firms.append(firm)

        project, _ = Project.objects.update_or_create(
            firm=firm,
            code=f"PRJ-{i:02d}",
            defaults={
                "name": f"Demo Project {i}",
                "client_name": f"Client {i} Developers",
                "contract_value_inr": Decimal(10_000_000 + i * 1_250_000),
                "manager": owner,
                "status": Project.Status.ACTIVE,
            },
        )
        projects.append(project)

        site, _ = Site.objects.update_or_create(
            project=project,
            code=f"SITE-{i:02d}",
            defaults={"name": f"Site {i}", "status": Site.Status.ACTIVE},
        )
        sites.append(site)

        Store.objects.update_or_create(
            site=site,
            code=f"STR-{i:02d}",
            defaults={"name": f"Main Store {i}", "status": Store.Status.ACTIVE},
        )

    hq_firm = firms[0]
    hq_project = projects[0]
    hq_site = sites[0]

    for i in range(1, SEED_COUNT + 1):
        CostCode.objects.update_or_create(
            project=hq_project,
            code=f"CC-{i:02d}",
            defaults={"name": f"Cost head {i}", "status": CostCode.Status.ACTIVE},
        )

    counts["firms"] = len(firms)
    counts["projects"] = len(projects)
    counts["sites"] = len(sites)

    owner_role = Role.objects.filter(code="Owner").first()
    if owner_role:
        UserRoleAssignment.objects.update_or_create(
            user=owner,
            role=owner_role,
            defaults={"scope_json": {"firm_ids": [str(f.id) for f in firms]}},
        )

    users: list[User] = [owner]
    for i in range(1, SEED_COUNT):
        email = f"user{i:02d}@demo.local"
        user, created = User.objects.update_or_create(
            email=email,
            defaults={
                "full_name": f"Demo User {i:02d}",
                "user_type": User.UserType.INTERNAL,
                "is_active": True,
            },
        )
        if created:
            user.set_password("demo1234")
            user.save(update_fields=["password"])
        users.append(user)
        if owner_role:
            UserRoleAssignment.objects.update_or_create(
                user=user,
                role=owner_role,
                defaults={"scope_json": {"firm_ids": [str(hq_firm.id)]}},
            )
    counts["users"] = len(users)

    for i in range(1, 7):
        Role.objects.update_or_create(
            code=f"DemoRole{i:02d}",
            defaults={"name": f"Demo Role {i:02d}"},
        )

    for i in range(1, SEED_COUNT + 1):
        ApprovalRequest.objects.update_or_create(
            firm=hq_firm,
            title=f"Approval request {i:02d}",
            defaults={
                "reference_type": "purchase_order",
                "reference_id": uuid.uuid4(),
                "status": ApprovalRequest.Status.PENDING if i % 3 else ApprovalRequest.Status.APPROVED,
                "requester": users[i % len(users)],
            },
        )
    counts["approval_requests"] = SEED_COUNT

    for i in range(1, SEED_COUNT + 1):
        AuditEvent.objects.update_or_create(
            entity_type="firm",
            entity_id=hq_firm.id,
            action=f"seed.action_{i}",
            defaults={
                "firm": hq_firm,
                "actor": owner,
                "summary": f"Seeded audit event {i}",
                "payload": {"index": i},
            },
        )
    counts["audit_events"] = SEED_COUNT

    for i in range(1, SEED_COUNT + 1):
        Document.objects.update_or_create(
            firm=hq_firm,
            object_key=f"demo/docs/file-{i:02d}.pdf",
            defaults={
                "title": f"Demo document {i:02d}",
                "content_type": "application/pdf",
                "size_bytes": 1024 * i,
            },
        )
    counts["documents"] = SEED_COUNT

    for i in range(1, SEED_COUNT + 1):
        NumberSequence.objects.update_or_create(
            firm=hq_firm,
            code=f"DOC-{i:02d}",
            defaults={"prefix": f"D{i}", "current_value": i * 100},
        )
    counts["sequences"] = SEED_COUNT

    for i in range(1, SEED_COUNT + 1):
        ImportBatch.objects.update_or_create(
            firm=hq_firm,
            file_name=f"import_batch_{i:02d}.csv",
            defaults={
                "module_key": "inventory",
                "status": ImportBatch.Status.COMPLETED,
                "total_rows": 100 + i,
                "error_rows": i % 2,
            },
        )
    counts["import_batches"] = SEED_COUNT

    for i in range(1, SEED_COUNT + 1):
        Notification.objects.update_or_create(
            user=owner,
            title=f"Notification {i:02d}",
            defaults={
                "message": f"Demo notification body {i}",
                "channel": "in_app",
                "is_read": i % 4 == 0,
            },
        )
    counts["notifications"] = SEED_COUNT

    for idx, (code, name, uom, cat) in enumerate(ITEM_NAMES, start=1):
        Item.objects.update_or_create(
            firm=hq_firm,
            code=code,
            defaults={
                "name": name,
                "uom": uom,
                "category": cat,
                "reorder_level": Decimal(idx * 5),
            },
        )
    counts["inventory_items"] = len(ITEM_NAMES)

    for i in range(1, SEED_COUNT + 1):
        PurchaseOrder.objects.update_or_create(
            firm=hq_firm,
            code=f"PO-{i:04d}",
            defaults={
                "project": hq_project,
                "vendor_name": VENDORS[i - 1],
                "status": PurchaseOrder.Status.APPROVED if i % 2 else PurchaseOrder.Status.DRAFT,
                "total_inr": Decimal(50_000 + i * 12_500),
            },
        )
    counts["purchase_orders"] = SEED_COUNT

    today = date.today()
    for i in range(1, SEED_COUNT + 1):
        Voucher.objects.update_or_create(
            firm=hq_firm,
            voucher_number=f"JV-{i:04d}",
            defaults={
                "voucher_date": today - timedelta(days=i),
                "voucher_type": "journal" if i % 2 else "payment",
                "status": Voucher.Status.POSTED if i % 3 else Voucher.Status.DRAFT,
                "amount_inr": Decimal(25_000 + i * 3_000),
                "narration": f"Seeded voucher {i}",
            },
        )
    counts["vouchers"] = SEED_COUNT

    for i in range(1, SEED_COUNT + 1):
        MaterialRequest.objects.update_or_create(
            site=hq_site,
            code=f"MR-{i:04d}",
            defaults={
                "status": MaterialRequest.Status.SUBMITTED,
                "priority": MaterialRequest.Priority.HIGH if i % 5 == 0 else MaterialRequest.Priority.NORMAL,
                "needed_on": today + timedelta(days=i),
            },
        )
    counts["material_requests"] = SEED_COUNT

    for i in range(1, SEED_COUNT + 1):
        ContractorParty.objects.update_or_create(
            firm=hq_firm,
            code=f"SUB-{i:02d}",
            defaults={
                "name": f"Subcontractor {i} Pvt Ltd",
                "contact_person": f"Contact {i}",
                "phone": f"98765{43210 + i}",
                "pan": f"SUBC{i:05d}F",
            },
        )
    counts["contractors"] = SEED_COUNT

    base_time = timezone.now() - timedelta(hours=SEED_COUNT)
    for i in range(1, SEED_COUNT + 1):
        FieldEvidence.objects.update_or_create(
            site=hq_site,
            title=f"Site photo {i:02d}",
            defaults={
                "photo_key": f"demo/evidence/photo-{i:02d}.jpg",
                "latitude": Decimal("12.971600") + Decimal(i) / Decimal(10000),
                "longitude": Decimal("77.594600") + Decimal(i) / Decimal(10000),
                "captured_at": base_time + timedelta(hours=i),
            },
        )
    counts["field_evidence"] = SEED_COUNT

    for i in range(1, SEED_COUNT + 1):
        Lead.objects.update_or_create(
            firm=hq_firm,
            code=f"LEAD-{i:03d}",
            defaults={
                "company_name": f"Prospect Builder {i}",
                "contact_name": f"Prospect Contact {i}",
                "status": Lead.Status.QUALIFIED if i % 2 else Lead.Status.NEW,
                "source": "site_visit" if i % 3 else "referral",
            },
        )
    counts["crm_leads"] = SEED_COUNT

    for i in range(1, SEED_COUNT + 1):
        Vendor.objects.update_or_create(
            firm=hq_firm,
            code=f"VND-{i:02d}",
            defaults={
                "name": VENDORS[i - 1],
                "gstin": f"29VEND{i:05d}F1Z5",
                "contact_phone": f"98000{10000 + i}",
            },
        )
    counts["vendors"] = SEED_COUNT

    hq_store = Store.objects.filter(site=hq_site).first()
    items = list(Item.objects.filter(firm=hq_firm).order_by("code")[:SEED_COUNT])
    if hq_store and items:
        for i, item in enumerate(items, start=1):
            StockBalance.objects.update_or_create(
                store=hq_store,
                item=item,
                defaults={
                    "on_hand": Decimal(50 * i),
                    "reserved": Decimal(i),
                },
            )
        counts["stock_balances"] = len(items)

    contractor = ContractorParty.objects.filter(firm=hq_firm).order_by("code").first()
    if contractor:
        for i in range(1, SEED_COUNT + 1):
            WorkOrder.objects.update_or_create(
                firm=hq_firm,
                code=f"WO-{i:04d}",
                defaults={
                    "contractor": contractor,
                    "project": hq_project,
                    "title": f"Subcontract package {i}",
                    "contract_value_inr": Decimal(500_000 + i * 75_000),
                    "status": WorkOrder.Status.ACTIVE,
                },
            )
        counts["work_orders"] = SEED_COUNT

    for i in range(1, SEED_COUNT + 1):
        Boq.objects.update_or_create(
            project=hq_project,
            code=f"BOQ-{i:02d}",
            revision_no=1,
            defaults={
                "name": f"BOQ package {i}",
                "total_inr": Decimal(1_000_000 + i * 250_000),
            },
        )
    counts["boqs"] = SEED_COUNT

    for i in range(1, SEED_COUNT + 1):
        MeasurementBook.objects.update_or_create(
            project=hq_project,
            code=f"MB-{i:04d}",
            defaults={
                "title": f"Measurement sheet {i}",
                "measured_on": today - timedelta(days=i),
                "certified_qty": Decimal(10 * i),
            },
        )
    counts["measurement_books"] = SEED_COUNT

    for i in range(1, SEED_COUNT + 1):
        ClientBill.objects.update_or_create(
            project=hq_project,
            code=f"RA-{i:04d}",
            defaults={
                "bill_date": today - timedelta(days=i),
                "gross_inr": Decimal(800_000 + i * 50_000),
                "retention_inr": Decimal(40_000 + i * 2_500),
                "status": ClientBill.Status.SUBMITTED,
            },
        )
    counts["client_bills"] = SEED_COUNT

    for i in range(1, SEED_COUNT + 1):
        ProjectBudget.objects.update_or_create(
            project=hq_project,
            code=f"BUD-{i:02d}",
            defaults={
                "name": f"Budget head {i}",
                "budget_inr": Decimal(2_000_000 + i * 100_000),
                "actual_inr": Decimal(1_500_000 + i * 80_000),
            },
        )
    counts["project_budgets"] = SEED_COUNT

    if items:
        for i, item in enumerate(items, start=1):
            MaterialConsumption.objects.update_or_create(
                site=hq_site,
                code=f"CON-{i:04d}",
                defaults={
                    "item": item,
                    "qty": Decimal(5 * i),
                    "consumed_on": today - timedelta(days=i),
                },
            )
        counts["material_consumptions"] = len(items)

    counts.update(
        seed_master_entities(
            hq_firm=hq_firm,
            hq_project=hq_project,
            hq_site=hq_site,
            hq_store=hq_store,
            items=items,
            today=today,
        )
    )

    return counts
