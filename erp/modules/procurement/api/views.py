from rest_framework.permissions import IsAuthenticated

from erp.common.api.viewsets import ERPReadOnlyViewSet
from erp.modules.procurement.api.serializers import PurchaseOrderSerializer
from erp.modules.procurement.models import PurchaseOrder


class PurchaseOrderViewSet(ERPReadOnlyViewSet):
    serializer_class = PurchaseOrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = PurchaseOrder.objects.select_related("firm", "project")
        firm_id = self.request.query_params.get("firm_id")
        if firm_id:
            qs = qs.filter(firm_id=firm_id)
        return qs
