from rest_framework import serializers

from erp.core.approvals.models import ApprovalRequest


class ApprovalRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApprovalRequest
        fields = (
            "id",
            "firm_id",
            "reference_type",
            "reference_id",
            "title",
            "status",
            "requester_id",
            "created_at",
            "updated_at",
        )
