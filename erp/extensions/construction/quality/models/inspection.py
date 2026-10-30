from django.db import models

from erp.common.models import TimestampedModel, UUIDModel


class QualityInspection(UUIDModel, TimestampedModel):
    site = models.ForeignKey(
        "core_organization.Site",
        on_delete=models.RESTRICT,
        related_name="quality_inspections",
    )
    code = models.CharField(max_length=32)
    inspected_on = models.DateField()
    result = models.CharField(max_length=32, default="pass")

    class Meta:
        unique_together = ("site", "code")
        ordering = ("-inspected_on",)
