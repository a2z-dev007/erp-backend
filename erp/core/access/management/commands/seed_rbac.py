from django.core.management.base import BaseCommand

from erp.core.access.models import Permission, Role, RolePermission


PERMISSIONS = [
    ("organisation.firm.view", "View firms"),
    ("organisation.firm.manage", "Manage firms"),
    ("organisation.project.view", "View projects"),
    ("organisation.project.manage", "Manage projects"),
    ("organisation.site.view", "View sites"),
    ("organisation.site.manage", "Manage sites"),
    ("organisation.store.view", "View stores"),
    ("organisation.store.manage", "Manage stores"),
    ("organisation.cost_code.view", "View cost codes"),
    ("organisation.cost_code.manage", "Manage cost codes"),
]

ROLES = {
    "Owner": [p[0] for p in PERMISSIONS],
    "ProjectManager": [
        "organisation.firm.view",
        "organisation.project.view",
        "organisation.project.manage",
        "organisation.site.view",
        "organisation.site.manage",
        "organisation.store.view",
        "organisation.cost_code.view",
        "organisation.cost_code.manage",
    ],
    "SiteSupervisor": [
        "organisation.firm.view",
        "organisation.project.view",
        "organisation.site.view",
        "organisation.store.view",
    ],
    "StoreKeeper": [
        "organisation.firm.view",
        "organisation.project.view",
        "organisation.site.view",
        "organisation.store.view",
        "organisation.store.manage",
    ],
}


class Command(BaseCommand):
    help = "Seed ERP permissions and roles"

    def handle(self, *args, **options):
        perm_map = {}
        for code, desc in PERMISSIONS:
            perm, _ = Permission.objects.update_or_create(
                code=code,
                defaults={"description": desc},
            )
            perm_map[code] = perm

        for role_code, perm_codes in ROLES.items():
            role, _ = Role.objects.update_or_create(
                code=role_code,
                defaults={"name": role_code},
            )
            RolePermission.objects.filter(role=role).delete()
            for pc in perm_codes:
                RolePermission.objects.create(role=role, permission=perm_map[pc])

        self.stdout.write(self.style.SUCCESS(f"Seeded {len(perm_map)} permissions and {len(ROLES)} roles"))
