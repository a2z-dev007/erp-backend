from django.db import models

from erp.common.models import ScopedModel


class EquipmentAsset(ScopedModel):
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=255)
    equipment_type = models.CharField(max_length=64, blank=True)

    class Meta:
        unique_together = ("firm", "code")
        ordering = ("name",)
