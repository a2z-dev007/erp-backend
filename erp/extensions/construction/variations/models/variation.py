from django.db import models

from erp.common.models import TimestampedModel, UUIDModel


class VariationOrder(UUIDModel, TimestampedModel):
    project = models.ForeignKey(
        "core_organization.Project",
        on_delete=models.RESTRICT,
        related_name="variation_orders",
    )
    code = models.CharField(max_length=32)
    title = models.CharField(max_length=255)
    amount_inr = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    class Meta:
        unique_together = ("project", "code")
        ordering = ("-created_at",)


class ProjectProgressRecord(UUIDModel, TimestampedModel):
    project = models.ForeignKey(
        "core_organization.Project",
        on_delete=models.RESTRICT,
        related_name="progress_records",
    )
    code = models.CharField(max_length=32)
    progress_pct = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    recorded_on = models.DateField()

    class Meta:
        unique_together = ("project", "code")
        ordering = ("-recorded_on",)
