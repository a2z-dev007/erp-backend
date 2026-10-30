from django.db import models

from erp.common.models import TimestampedModel, UUIDModel


class ProjectBudget(UUIDModel, TimestampedModel):
    project = models.ForeignKey(
        "core_organization.Project",
        on_delete=models.RESTRICT,
        related_name="budgets",
    )
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=255)
    budget_inr = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    actual_inr = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    class Meta:
        unique_together = ("project", "code")
        ordering = ("code",)

    def __str__(self) -> str:
        return self.code
