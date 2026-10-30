from django.db import models

from erp.common.models import ScopedModel, TimestampedModel, UUIDModel


class TaxCategory(ScopedModel):
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=128)
    rate_percent = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    class Meta:
        unique_together = ("firm", "code")
        ordering = ("code",)


class LedgerAccount(ScopedModel):
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=255)
    account_type = models.CharField(max_length=32, default="expense")

    class Meta:
        unique_together = ("firm", "code")
        ordering = ("code",)


class Payment(ScopedModel):
    class Direction(models.TextChoices):
        IN = "in", "Incoming"
        OUT = "out", "Outgoing"

    code = models.CharField(max_length=32)
    payment_date = models.DateField()
    amount_inr = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    direction = models.CharField(max_length=8, choices=Direction.choices, default=Direction.OUT)

    class Meta:
        unique_together = ("firm", "code")
        ordering = ("-payment_date",)


class GLEntry(UUIDModel, TimestampedModel):
    firm = models.ForeignKey(
        "core_organization.Firm",
        on_delete=models.RESTRICT,
        related_name="gl_entries",
    )
    account = models.ForeignKey(LedgerAccount, on_delete=models.RESTRICT, related_name="gl_entries")
    voucher = models.ForeignKey(
        "mod_finance.Voucher",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="gl_entries",
    )
    entry_date = models.DateField()
    debit_inr = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    credit_inr = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    narration = models.CharField(max_length=512, blank=True)

    class Meta:
        ordering = ("-entry_date",)
