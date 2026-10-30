from django.apps import AppConfig


class FinanceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "erp.modules.finance"
    label = "mod_finance"
    verbose_name = "Finance"
