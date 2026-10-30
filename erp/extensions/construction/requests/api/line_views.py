from rest_framework import serializers

from erp.common.api.module_api import readonly_viewset
from erp.extensions.construction.requests.models import MaterialRequestLine


class MaterialRequestLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialRequestLine
        fields = "__all__"


MaterialRequestLineViewSet = readonly_viewset(
    MaterialRequestLine,
    MaterialRequestLineSerializer,
    select_related=("material_request", "item"),
)
