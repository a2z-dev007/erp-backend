from django.db import models

from erp.common.models import ScopedModel


class Lead(ScopedModel):
    class Status(models.TextChoices):
        NEW = "new", "New"
        QUALIFIED = "qualified", "Qualified"
        WON = "won", "Won"
        LOST = "lost", "Lost"

    code = models.CharField(max_length=32)
    company_name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=128, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.NEW)
    source = models.CharField(max_length=64, blank=True)

    class Meta:
        unique_together = ("firm", "code")
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.company_name
