from django.apps import AppConfig


class OrganizationConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "erp.core.organization"
    label = "core_organization"
    verbose_name = "Core — Organization"
