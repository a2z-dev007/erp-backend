from django.apps import AppConfig


class InventoryConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "erp.modules.inventory"
    label = "mod_inventory"
    verbose_name = "Inventory"
