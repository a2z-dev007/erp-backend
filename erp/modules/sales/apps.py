from django.apps import AppConfig


class SalesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "erp.modules.sales"
    label = "mod_sales"
    verbose_name = "Sales"
