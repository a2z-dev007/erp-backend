from django.db import models

from erp.common.models import ScopedModel


class ContractorParty(ScopedModel):
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=128, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    pan = models.CharField(max_length=16, blank=True)

    class Meta:
        unique_together = ("firm", "code")
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name
