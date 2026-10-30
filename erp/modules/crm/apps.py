from django.apps import AppConfig


class CrmConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "erp.modules.crm"
    label = "mod_crm"
    verbose_name = "CRM"
