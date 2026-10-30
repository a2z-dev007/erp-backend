from rest_framework.permissions import IsAuthenticated

from erp.common.api.viewsets import ERPReadOnlyViewSet
from erp.core.audit.api.serializers import AuditEventSerializer
from erp.core.audit.models import AuditEvent


class AuditEventViewSet(ERPReadOnlyViewSet):
    serializer_class = AuditEventSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = AuditEvent.objects.select_related("firm", "actor")
        firm_id = self.request.query_params.get("firm_id")
        if firm_id:
            qs = qs.filter(firm_id=firm_id)
        return qs
