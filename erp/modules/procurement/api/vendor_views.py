from rest_framework import serializers

from erp.common.api.module_api import readonly_viewset
from erp.modules.procurement.models import Vendor


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = "__all__"


VendorViewSet = readonly_viewset(Vendor, VendorSerializer, select_related=("firm",))
