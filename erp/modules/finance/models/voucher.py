from django.db import models

from erp.common.models import ScopedModel


class Voucher(ScopedModel):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        POSTED = "posted", "Posted"

    voucher_number = models.CharField(max_length=32)
    voucher_date = models.DateField()
    voucher_type = models.CharField(max_length=32, default="payment")
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    amount_inr = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    narration = models.CharField(max_length=512, blank=True)

    class Meta:
        unique_together = ("firm", "voucher_number")
        ordering = ("-voucher_date",)

    def __str__(self) -> str:
        return self.voucher_number
