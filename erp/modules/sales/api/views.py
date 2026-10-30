from rest_framework import serializers

from erp.common.api.module_api import readonly_viewset
from erp.modules.sales.models import ClientContract, SalesInvoice, SalesOrder


class SalesOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrder
        fields = "__all__"


class SalesInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesInvoice
        fields = "__all__"


class ClientContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientContract
        fields = "__all__"


SalesOrderViewSet = readonly_viewset(SalesOrder, SalesOrderSerializer, select_related=("firm", "customer"))
SalesInvoiceViewSet = readonly_viewset(
    SalesInvoice, SalesInvoiceSerializer, select_related=("firm", "customer")
)
ClientContractViewSet = readonly_viewset(
    ClientContract, ClientContractSerializer, select_related=("firm", "project")
)
