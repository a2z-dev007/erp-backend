from django.db import models

from erp.common.models import ScopedModel


class Customer(ScopedModel):
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=255)
    gstin = models.CharField(max_length=20, blank=True)
    billing_city = models.CharField(max_length=128, blank=True)

    class Meta:
        unique_together = ("firm", "code")
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name
