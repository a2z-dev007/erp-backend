from rest_framework import serializers

from erp.common.api.module_api import readonly_viewset
from erp.core.organization.models import Branch, Department


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


BranchViewSet = readonly_viewset(Branch, BranchSerializer, select_related=("firm",))
DepartmentViewSet = readonly_viewset(
    Department,
    DepartmentSerializer,
    select_related=("firm", "branch"),
)
