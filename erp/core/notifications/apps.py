from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "erp.core.notifications"
    label = "core_notifications"
    verbose_name = "Core — Notifications"
