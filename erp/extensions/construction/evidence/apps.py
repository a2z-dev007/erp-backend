from django.apps import AppConfig


class ConstructionEvidenceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "erp.extensions.construction.evidence"
    label = "ext_construction_evidence"
    verbose_name = "Construction — Evidence"
