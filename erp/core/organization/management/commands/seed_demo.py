from django.core.management.base import BaseCommand

from erp.core.access.models import Role, UserRoleAssignment
from erp.core.identity.models import User
from erp.core.organization.models import CostCode, Firm, Project, Site, Store


class Command(BaseCommand):
    help = "Seed demo org data and owner user (owner@demo.local / demo1234)"

    def handle(self, *args, **options):
        firm, _ = Firm.objects.update_or_create(
            code="FIRM-HQ",
            defaults={
                "name": "Malhar Constructions Pvt Ltd",
                "pan": "AABCM1234F",
                "gstin": "29AABCM1234F1Z5",
                "status": "active",
            },
        )
        user, created = User.objects.update_or_create(
            email="owner@demo.local",
            defaults={
                "full_name": "Demo Owner",
                "user_type": User.UserType.INTERNAL,
                "is_staff": True,
                "is_superuser": True,
            },
        )
        if created:
            user.set_password("demo1234")
            user.save()

        owner_role = Role.objects.filter(code="Owner").first()
        if owner_role:
            UserRoleAssignment.objects.update_or_create(
                user=user,
                role=owner_role,
                defaults={"scope_json": {"firm_ids": [str(firm.id)]}},
            )

        project, _ = Project.objects.update_or_create(
            firm=firm,
            code="PRJ-BLR-04",
            defaults={
                "name": "Whitefield Tower Superstructure",
                "client_name": "Raya Infra Developers",
                "contract_value_inr": 186500000,
                "manager": user,
                "status": "active",
            },
        )
        site, _ = Site.objects.update_or_create(
            project=project,
            code="WF-POD",
            defaults={"name": "Whitefield Podium Site", "status": "active"},
        )
        Store.objects.update_or_create(
            site=site,
            code="STR-WF-01",
            defaults={"name": "Whitefield Main Store", "status": "active"},
        )
        CostCode.objects.update_or_create(
            project=project,
            code="STR-RC",
            defaults={"name": "Structural RCC", "status": "active"},
        )

        self.stdout.write(self.style.SUCCESS("Demo data seeded. Login: owner@demo.local / demo1234"))
