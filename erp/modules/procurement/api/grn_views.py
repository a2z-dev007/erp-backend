from rest_framework import serializers

from erp.common.api.module_api import readonly_viewset
from erp.modules.procurement.models import GoodsReceiptNote, PurchaseInvoice


class GoodsReceiptNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsReceiptNote
        fields = "__all__"


class PurchaseInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseInvoice
        fields = "__all__"


GoodsReceiptNoteViewSet = readonly_viewset(
    GoodsReceiptNote, GoodsReceiptNoteSerializer, select_related=("firm", "purchase_order")
)
PurchaseInvoiceViewSet = readonly_viewset(
    PurchaseInvoice, PurchaseInvoiceSerializer, select_related=("firm", "vendor")
)
