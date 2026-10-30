from django.db import models

from erp.common.models import TimestampedModel, UUIDModel


class RetentionRecord(UUIDModel, TimestampedModel):
    client_bill = models.ForeignKey(
        "ext_construction_client_billing.ClientBill",
        on_delete=models.CASCADE,
        related_name="retention_records",
    )
    amount_inr = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    release_due_on = models.DateField(null=True, blank=True)
    released = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created_at",)
