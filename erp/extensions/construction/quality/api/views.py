from rest_framework import serializers

from erp.common.api.module_api import readonly_viewset
from erp.extensions.construction.quality.models import QualityInspection


class QualityInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualityInspection
        fields = "__all__"


QualityInspectionViewSet = readonly_viewset(
    QualityInspection, QualityInspectionSerializer, select_related=("site",)
)
