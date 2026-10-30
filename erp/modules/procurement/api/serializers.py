from rest_framework import serializers

from erp.modules.procurement.models import PurchaseOrder


class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = (
            "id",
            "firm_id",
            "project_id",
            "code",
            "vendor_name",
            "status",
            "total_inr",
            "created_at",
            "updated_at",
        )
