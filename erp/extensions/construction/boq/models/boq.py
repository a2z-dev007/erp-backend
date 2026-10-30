from django.db import models

from erp.common.models import TimestampedModel, UUIDModel


class Boq(UUIDModel, TimestampedModel):
    project = models.ForeignKey(
        "core_organization.Project",
        on_delete=models.RESTRICT,
        related_name="boqs",
    )
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=255)
    revision_no = models.PositiveSmallIntegerField(default=1)
    total_inr = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    class Meta:
        unique_together = ("project", "code", "revision_no")
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return f"{self.code} r{self.revision_no}"
