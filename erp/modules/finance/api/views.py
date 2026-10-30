from rest_framework.permissions import IsAuthenticated

from erp.common.api.viewsets import ERPReadOnlyViewSet
from erp.modules.finance.api.serializers import VoucherSerializer
from erp.modules.finance.models import Voucher


class VoucherViewSet(ERPReadOnlyViewSet):
    serializer_class = VoucherSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = Voucher.objects.select_related("firm")
        firm_id = self.request.query_params.get("firm_id")
        if firm_id:
            qs = qs.filter(firm_id=firm_id)
        return qs
