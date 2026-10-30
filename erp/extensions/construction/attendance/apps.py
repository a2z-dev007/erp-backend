from django.apps import AppConfig


class ConstructionAttendanceConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "erp.extensions.construction.attendance"
    label = "ext_construction_attendance"
    verbose_name = "Construction — Site Attendance"
