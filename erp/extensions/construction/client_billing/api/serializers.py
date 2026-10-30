from rest_framework import serializers

from erp.extensions.construction.client_billing.models import ClientBill


class ClientBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientBill
        fields = "__all__"
