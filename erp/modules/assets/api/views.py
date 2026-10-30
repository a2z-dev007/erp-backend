from rest_framework import serializers

from erp.common.api.module_api import readonly_viewset
from erp.modules.assets.models import FixedAsset


class FixedAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = FixedAsset
        fields = "__all__"


FixedAssetViewSet = readonly_viewset(FixedAsset, FixedAssetSerializer, select_related=("firm",))
