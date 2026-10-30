from rest_framework.permissions import IsAuthenticated

from erp.common.api.viewsets import ERPReadOnlyViewSet
from erp.extensions.construction.contractors.api.serializers import ContractorPartySerializer
from erp.extensions.construction.contractors.models import ContractorParty


class ContractorPartyViewSet(ERPReadOnlyViewSet):
    serializer_class = ContractorPartySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = ContractorParty.objects.select_related("firm")
        firm_id = self.request.query_params.get("firm_id")
        if firm_id:
            qs = qs.filter(firm_id=firm_id)
        return qs
