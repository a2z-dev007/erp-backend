from django.apps import AppConfig


class ApprovalsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "erp.core.approvals"
    label = "core_approvals"
    verbose_name = "Core — Approvals"
