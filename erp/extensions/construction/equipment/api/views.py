from rest_framework import serializers

from erp.common.api.module_api import readonly_viewset
from erp.extensions.construction.equipment.models import EquipmentAsset


class EquipmentAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipmentAsset
        fields = "__all__"


EquipmentAssetViewSet = readonly_viewset(
    EquipmentAsset, EquipmentAssetSerializer, select_related=("firm",)
)
