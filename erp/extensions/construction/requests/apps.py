from django.apps import AppConfig


class ConstructionRequestsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "erp.extensions.construction.requests"
    label = "ext_construction_requests"
    verbose_name = "Construction — Requests"
