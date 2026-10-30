from django.apps import AppConfig


class ConstructionQualityConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "erp.extensions.construction.quality"
    label = "ext_construction_quality"
    verbose_name = "Construction — Quality & Safety"
