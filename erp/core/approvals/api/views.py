from rest_framework.permissions import IsAuthenticated

from erp.common.api.viewsets import ERPReadOnlyViewSet
from erp.core.approvals.api.serializers import ApprovalRequestSerializer
from erp.core.approvals.models import ApprovalRequest


class ApprovalRequestViewSet(ERPReadOnlyViewSet):
    serializer_class = ApprovalRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = ApprovalRequest.objects.select_related("firm", "requester")
        firm_id = self.request.query_params.get("firm_id")
        if firm_id:
            qs = qs.filter(firm_id=firm_id)
        return qs
