from rest_framework.permissions import IsAuthenticated

from erp.common.api.viewsets import ERPReadOnlyViewSet
from erp.core.documents.api.serializers import DocumentSerializer
from erp.core.documents.models import Document


class DocumentViewSet(ERPReadOnlyViewSet):
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = Document.objects.select_related("firm")
        firm_id = self.request.query_params.get("firm_id")
        if firm_id:
            qs = qs.filter(firm_id=firm_id)
        return qs
