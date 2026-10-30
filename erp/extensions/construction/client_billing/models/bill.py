from django.db import models

from erp.common.models import TimestampedModel, UUIDModel


class ClientBill(UUIDModel, TimestampedModel):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        SUBMITTED = "submitted", "Submitted"
        PAID = "paid", "Paid"

    project = models.ForeignKey(
        "core_organization.Project",
        on_delete=models.RESTRICT,
        related_name="client_bills",
    )
    code = models.CharField(max_length=32)
    bill_date = models.DateField()
    gross_inr = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    retention_inr = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        unique_together = ("project", "code")
        ordering = ("-bill_date",)

    def __str__(self) -> str:
        return self.code
