from django.db import models

from erp.common.models import TimestampedModel, UUIDModel


class MeasurementBook(UUIDModel, TimestampedModel):
    project = models.ForeignKey(
        "core_organization.Project",
        on_delete=models.RESTRICT,
        related_name="measurement_books",
    )
    code = models.CharField(max_length=32)
    title = models.CharField(max_length=255)
    measured_on = models.DateField()
    certified_qty = models.DecimalField(max_digits=14, decimal_places=3, default=0)

    class Meta:
        unique_together = ("project", "code")
        ordering = ("-measured_on",)

    def __str__(self) -> str:
        return self.code
