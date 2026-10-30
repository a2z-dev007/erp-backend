from rest_framework import serializers

from erp.common.api.module_api import readonly_viewset
from erp.modules.inventory.models import StockLedgerEntry


class StockLedgerEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = StockLedgerEntry
        fields = "__all__"


StockLedgerEntryViewSet = readonly_viewset(
    StockLedgerEntry,
    StockLedgerEntrySerializer,
    select_related=("store", "item"),
)
