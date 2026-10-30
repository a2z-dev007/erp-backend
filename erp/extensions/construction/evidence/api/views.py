from rest_framework.permissions import IsAuthenticated

from erp.common.api.viewsets import ERPReadOnlyViewSet
from erp.extensions.construction.evidence.api.serializers import FieldEvidenceSerializer
from erp.extensions.construction.evidence.models import FieldEvidence


class FieldEvidenceViewSet(ERPReadOnlyViewSet):
    serializer_class = FieldEvidenceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = FieldEvidence.objects.select_related("site")
        site_id = self.request.query_params.get("site_id")
        if site_id:
            qs = qs.filter(site_id=site_id)
        return qs
