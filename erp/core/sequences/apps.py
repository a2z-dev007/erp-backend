from django.apps import AppConfig


class SequencesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "erp.core.sequences"
    label = "core_sequences"
    verbose_name = "Core — Sequences"
