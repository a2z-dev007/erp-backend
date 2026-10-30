from rest_framework import serializers

from erp.common.api.module_api import readonly_viewset
from erp.modules.inventory.models import StockBalance


class StockBalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockBalance
        fields = "__all__"


StockBalanceViewSet = readonly_viewset(
    StockBalance,
    StockBalanceSerializer,
    select_related=("store", "item"),
)
