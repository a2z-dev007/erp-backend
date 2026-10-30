from django.db import models

from erp.common.models import TimestampedModel, UUIDModel


class StockLedgerEntry(UUIDModel, TimestampedModel):
    store = models.ForeignKey(
        "core_organization.Store",
        on_delete=models.RESTRICT,
        related_name="stock_ledger_entries",
    )
    item = models.ForeignKey(
        "mod_inventory.Item",
        on_delete=models.RESTRICT,
        related_name="stock_ledger_entries",
    )
    qty_delta = models.DecimalField(max_digits=14, decimal_places=3)
    document_type = models.CharField(max_length=32)
    document_id = models.UUIDField(null=True, blank=True)
    occurred_at = models.DateTimeField()

    class Meta:
        ordering = ("-occurred_at",)
