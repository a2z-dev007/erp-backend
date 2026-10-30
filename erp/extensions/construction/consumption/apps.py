from django.apps import AppConfig


class ConstructionConsumptionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "erp.extensions.construction.consumption"
    label = "ext_construction_consumption"
    verbose_name = "Construction — Material Consumption"
