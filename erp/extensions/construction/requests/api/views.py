from rest_framework.permissions import IsAuthenticated

from erp.common.api.viewsets import ERPReadOnlyViewSet
from erp.extensions.construction.requests.api.serializers import MaterialRequestSerializer
from erp.extensions.construction.requests.models import MaterialRequest


class MaterialRequestViewSet(ERPReadOnlyViewSet):
    serializer_class = MaterialRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = MaterialRequest.objects.select_related("site")
        site_id = self.request.query_params.get("site_id")
        if site_id:
            qs = qs.filter(site_id=site_id)
        return qs
