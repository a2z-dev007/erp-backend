from django.apps import AppConfig


class ConstructionClientBillingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "erp.extensions.construction.client_billing"
    label = "ext_construction_client_billing"
    verbose_name = "Construction — Client Billing"
