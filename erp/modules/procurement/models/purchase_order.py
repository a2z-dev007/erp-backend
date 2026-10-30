from django.db import models

from erp.common.models import ScopedModel


class PurchaseOrder(ScopedModel):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        APPROVED = "approved", "Approved"
        CLOSED = "closed", "Closed"

    project = models.ForeignKey(
        "core_organization.Project",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="purchase_orders",
    )
    code = models.CharField(max_length=32)
    vendor_name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    total_inr = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    class Meta:
        unique_together = ("firm", "code")
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.code
