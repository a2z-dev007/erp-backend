from django.db import models

from erp.common.models import TimestampedModel, UUIDModel


class FieldEvidence(UUIDModel, TimestampedModel):
    site = models.ForeignKey(
        "core_organization.Site",
        on_delete=models.RESTRICT,
        related_name="field_evidence",
    )
    title = models.CharField(max_length=255)
    photo_key = models.CharField(max_length=512, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    captured_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.title
