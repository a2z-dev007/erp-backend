from django.db import models

from erp.common.models import TimestampedModel, UUIDModel


class MaterialRequestLine(UUIDModel, TimestampedModel):
    material_request = models.ForeignKey(
        "ext_construction_requests.MaterialRequest",
        on_delete=models.CASCADE,
        related_name="lines",
    )
    item = models.ForeignKey(
        "mod_inventory.Item",
        on_delete=models.RESTRICT,
        related_name="material_request_lines",
    )
    qty = models.DecimalField(max_digits=14, decimal_places=3)

    class Meta:
        ordering = ("created_at",)
