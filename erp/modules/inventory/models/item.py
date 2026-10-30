from django.db import models

from erp.common.models import ScopedModel


class Item(ScopedModel):
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=255)
    uom = models.CharField(max_length=16, default="NOS")
    category = models.CharField(max_length=64, blank=True)
    reorder_level = models.DecimalField(max_digits=14, decimal_places=3, default=0)

    class Meta:
        unique_together = ("firm", "code")
        ordering = ("code",)

    def __str__(self) -> str:
        return self.name
