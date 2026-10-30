from django.db import models

from erp.common.models import ScopedModel


class FixedAsset(ScopedModel):
    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        DISPOSED = "disposed", "Disposed"

    code = models.CharField(max_length=32)
    name = models.CharField(max_length=255)
    purchase_date = models.DateField(null=True, blank=True)
    value_inr = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)

    class Meta:
        unique_together = ("firm", "code")
        ordering = ("code",)
