from django.apps import AppConfig


class ProcurementConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "erp.modules.procurement"
    label = "mod_procurement"
    verbose_name = "Procurement"
