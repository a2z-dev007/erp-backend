from rest_framework import serializers

from erp.common.api.module_api import readonly_viewset
from erp.extensions.construction.measurement.models import WorkPackage


class WorkPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPackage
        fields = "__all__"


WorkPackageViewSet = readonly_viewset(WorkPackage, WorkPackageSerializer, select_related=("project",))
