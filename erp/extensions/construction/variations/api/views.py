from rest_framework import serializers

from erp.common.api.module_api import readonly_viewset
from erp.extensions.construction.variations.models import ProjectProgressRecord, VariationOrder


class VariationOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariationOrder
        fields = "__all__"


class ProjectProgressRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectProgressRecord
        fields = "__all__"


VariationOrderViewSet = readonly_viewset(
    VariationOrder, VariationOrderSerializer, select_related=("project",)
)
ProjectProgressRecordViewSet = readonly_viewset(
    ProjectProgressRecord, ProjectProgressRecordSerializer, select_related=("project",)
)
