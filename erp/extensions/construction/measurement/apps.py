from django.apps import AppConfig


class ConstructionMeasurementConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "erp.extensions.construction.measurement"
    label = "ext_construction_measurement"
    verbose_name = "Construction — Measurement"
