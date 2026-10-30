from django.core.management import call_command
from django.core.management.base import BaseCommand

from erp.common.seed.runner import run_seed_all
from erp.core.access.models import Permission


class Command(BaseCommand):
    help = "Seed RBAC (if needed), organisation graph, and 10+ demo rows per module API"

    def add_arguments(self, parser):
        parser.add_argument(
            "--skip-rbac",
            action="store_true",
            help="Do not run seed_rbac before seeding data",
        )

    def handle(self, *args, **options):
        call_command("migrate", verbosity=0)
        if not options["skip_rbac"] and not Permission.objects.exists():
            call_command("seed_rbac")

        counts = run_seed_all()
        summary = ", ".join(f"{k}={v}" for k, v in sorted(counts.items()))
        self.stdout.write(self.style.SUCCESS(f"seed_all complete: {summary}"))
        self.stdout.write("Login: owner@demo.local / demo1234 (also user01@demo.local … user09@demo.local)")
