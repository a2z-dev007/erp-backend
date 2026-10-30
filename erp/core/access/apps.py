from django.apps import AppConfig


class AccessConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "erp.core.access"
    label = "core_access"
    verbose_name = "Core — Access Control"
