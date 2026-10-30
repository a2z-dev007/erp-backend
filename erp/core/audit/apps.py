from django.apps import AppConfig


class AuditConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "erp.core.audit"
    label = "core_audit"
    verbose_name = "Core — Audit"
