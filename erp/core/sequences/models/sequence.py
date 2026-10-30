from django.db import models

from erp.common.models import ScopedModel


class NumberSequence(ScopedModel):
    code = models.CharField(max_length=32)
    prefix = models.CharField(max_length=16, blank=True)
    current_value = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ("firm", "code")
        ordering = ("code",)

    def __str__(self) -> str:
        return f"{self.code} ({self.firm_id})"
