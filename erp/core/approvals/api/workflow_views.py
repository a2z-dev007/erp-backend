from rest_framework import serializers

from erp.common.api.module_api import readonly_viewset
from erp.core.approvals.models import WorkflowDefinition


class WorkflowDefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkflowDefinition
        fields = "__all__"


WorkflowDefinitionViewSet = readonly_viewset(
    WorkflowDefinition,
    WorkflowDefinitionSerializer,
    select_related=("firm",),
)
