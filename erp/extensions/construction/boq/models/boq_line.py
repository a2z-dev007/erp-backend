from django.db import models

from erp.common.models import TimestampedModel, UUIDModel


class BoqLine(UUIDModel, TimestampedModel):
    boq = models.ForeignKey("ext_construction_boq.Boq", on_delete=models.CASCADE, related_name="lines")
    line_no = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=512)
    qty = models.DecimalField(max_digits=14, decimal_places=3, default=0)
    rate_inr = models.DecimalField(max_digits=14, decimal_places=2, default=0)

    class Meta:
        unique_together = ("boq", "line_no")
        ordering = ("line_no",)
