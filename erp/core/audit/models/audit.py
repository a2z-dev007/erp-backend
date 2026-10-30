from django.conf import settings
from django.db import models

from erp.common.models import TimestampedModel, UUIDModel


class AuditEvent(UUIDModel, TimestampedModel):
    firm = models.ForeignKey(
        "core_organization.Firm",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="audit_events",
    )
    action = models.CharField(max_length=64)
    entity_type = models.CharField(max_length=64)
    entity_id = models.UUIDField()
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="audit_events",
    )
    summary = models.CharField(max_length=512, blank=True)
    payload = models.JSONField(default=dict, blank=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return f"{self.action} {self.entity_type}"
