from rest_framework.permissions import IsAuthenticated

from erp.common.api.viewsets import ERPReadOnlyViewSet
from erp.modules.inventory.api.serializers import ItemSerializer
from erp.modules.inventory.models import Item


class ItemViewSet(ERPReadOnlyViewSet):
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = Item.objects.select_related("firm")
        firm_id = self.request.query_params.get("firm_id")
        if firm_id:
            qs = qs.filter(firm_id=firm_id)
        return qs
