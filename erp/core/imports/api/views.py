from rest_framework.permissions import IsAuthenticated

from erp.common.api.viewsets import ERPReadOnlyViewSet
from erp.core.imports.api.serializers import ImportBatchSerializer
from erp.core.imports.models import ImportBatch


class ImportBatchViewSet(ERPReadOnlyViewSet):
    serializer_class = ImportBatchSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = ImportBatch.objects.select_related("firm")
        firm_id = self.request.query_params.get("firm_id")
        if firm_id:
            qs = qs.filter(firm_id=firm_id)
        return qs
