from django.apps import AppConfig


class ConstructionCostingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "erp.extensions.construction.costing"
    label = "ext_construction_costing"
    verbose_name = "Construction — Project Costing"
