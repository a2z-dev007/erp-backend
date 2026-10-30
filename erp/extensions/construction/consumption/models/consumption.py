from django.db import models

from erp.common.models import TimestampedModel, UUIDModel


class MaterialConsumption(UUIDModel, TimestampedModel):
    site = models.ForeignKey(
        "core_organization.Site",
        on_delete=models.RESTRICT,
        related_name="material_consumptions",
    )
    item = models.ForeignKey(
        "mod_inventory.Item",
        on_delete=models.RESTRICT,
        related_name="consumptions",
    )
    code = models.CharField(max_length=32)
    qty = models.DecimalField(max_digits=14, decimal_places=3)
    consumed_on = models.DateField()

    class Meta:
        unique_together = ("site", "code")
        ordering = ("-consumed_on",)

    def __str__(self) -> str:
        return self.code
