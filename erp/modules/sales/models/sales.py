from django.db import models

from erp.common.models import ScopedModel


class SalesOrder(ScopedModel):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        CONFIRMED = "confirmed", "Confirmed"
        CLOSED = "closed", "Closed"

    customer = models.ForeignKey(
        "mod_crm.Customer",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sales_orders",
    )
    code = models.CharField(max_length=32)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    total_inr = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    class Meta:
        unique_together = ("firm", "code")
        ordering = ("-created_at",)


class SalesInvoice(ScopedModel):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        POSTED = "posted", "Posted"
        PAID = "paid", "Paid"

    customer = models.ForeignKey(
        "mod_crm.Customer",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="sales_invoices",
    )
    code = models.CharField(max_length=32)
    invoice_date = models.DateField()
    total_inr = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        unique_together = ("firm", "code")
        ordering = ("-invoice_date",)


class ClientContract(ScopedModel):
    project = models.ForeignKey(
        "core_organization.Project",
        on_delete=models.RESTRICT,
        related_name="client_contracts",
    )
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=255)
    contract_value_inr = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    class Meta:
        unique_together = ("firm", "code")
        ordering = ("code",)
