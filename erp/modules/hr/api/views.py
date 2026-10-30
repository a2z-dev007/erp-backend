from rest_framework import serializers

from erp.common.api.module_api import readonly_viewset
from erp.modules.hr.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


EmployeeViewSet = readonly_viewset(Employee, EmployeeSerializer, select_related=("firm", "department"))
