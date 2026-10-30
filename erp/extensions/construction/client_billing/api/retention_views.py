from rest_framework import serializers

from erp.common.api.module_api import readonly_viewset
from erp.extensions.construction.client_billing.models import RetentionRecord


class RetentionRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetentionRecord
        fields = "__all__"


RetentionRecordViewSet = readonly_viewset(
    RetentionRecord,
    RetentionRecordSerializer,
    select_related=("client_bill",),
)
