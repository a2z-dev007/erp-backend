from django.db import models

from erp.common.models import TimestampedModel, UUIDModel


class StockBalance(UUIDModel, TimestampedModel):
    store = models.ForeignKey(
        "core_organization.Store",
        on_delete=models.CASCADE,
        related_name="stock_balances",
    )
    item = models.ForeignKey(
        "mod_inventory.Item",
        on_delete=models.CASCADE,
        related_name="stock_balances",
    )
    on_hand = models.DecimalField(max_digits=14, decimal_places=3, default=0)
    reserved = models.DecimalField(max_digits=14, decimal_places=3, default=0)

    class Meta:
        unique_together = ("store", "item")
        ordering = ("store_id", "item_id")

    def __str__(self) -> str:
        return f"{self.item_id} @ {self.store_id}"
