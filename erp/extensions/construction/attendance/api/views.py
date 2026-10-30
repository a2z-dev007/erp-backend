from rest_framework import serializers

from erp.common.api.module_api import readonly_viewset
from erp.extensions.construction.attendance.models import SiteAttendance


class SiteAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteAttendance
        fields = "__all__"


SiteAttendanceViewSet = readonly_viewset(
    SiteAttendance, SiteAttendanceSerializer, select_related=("site", "employee")
)
