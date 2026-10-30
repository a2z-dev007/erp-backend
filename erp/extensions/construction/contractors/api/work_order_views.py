from rest_framework import serializers

from erp.common.api.module_api import readonly_viewset
from erp.extensions.construction.contractors.models import WorkOrder


class WorkOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkOrder
        fields = "__all__"


WorkOrderViewSet = readonly_viewset(
    WorkOrder,
    WorkOrderSerializer,
    select_related=("firm", "contractor", "project"),
)
