from django.db import models

from erp.common.models import ScopedModel


class GoodsReceiptNote(ScopedModel):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        POSTED = "posted", "Posted"

    purchase_order = models.ForeignKey(
        "mod_procurement.PurchaseOrder",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="grns",
    )
    code = models.CharField(max_length=32)
    received_on = models.DateField()
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        unique_together = ("firm", "code")
        ordering = ("-received_on",)


class PurchaseInvoice(ScopedModel):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        POSTED = "posted", "Posted"

    vendor = models.ForeignKey(
        "mod_procurement.Vendor",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="purchase_invoices",
    )
    code = models.CharField(max_length=32)
    invoice_date = models.DateField()
    amount_inr = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        unique_together = ("firm", "code")
        ordering = ("-invoice_date",)
