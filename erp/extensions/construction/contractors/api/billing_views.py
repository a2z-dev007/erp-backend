from rest_framework import serializers

from erp.common.api.module_api import readonly_viewset
from erp.extensions.construction.contractors.models import SubcontractorBill


class SubcontractorBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubcontractorBill
        fields = "__all__"


SubcontractorBillViewSet = readonly_viewset(
    SubcontractorBill,
    SubcontractorBillSerializer,
    select_related=("firm", "work_order"),
)
