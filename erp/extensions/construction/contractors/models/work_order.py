from django.db import models

from erp.common.models import ScopedModel


class WorkOrder(ScopedModel):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        ACTIVE = "active", "Active"
        CLOSED = "closed", "Closed"

    contractor = models.ForeignKey(
        "ext_construction_contractors.ContractorParty",
        on_delete=models.RESTRICT,
        related_name="work_orders",
    )
    project = models.ForeignKey(
        "core_organization.Project",
        on_delete=models.RESTRICT,
        related_name="work_orders",
    )
    code = models.CharField(max_length=32)
    title = models.CharField(max_length=255)
    contract_value_inr = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        unique_together = ("firm", "code")
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.code
