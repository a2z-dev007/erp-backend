from django.apps import AppConfig


class HrConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "erp.modules.hr"
    label = "mod_hr"
    verbose_name = "Human Resources"
