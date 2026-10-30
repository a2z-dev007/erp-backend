from rest_framework.permissions import IsAuthenticated

from erp.common.api.viewsets import ERPReadOnlyViewSet
from erp.core.sequences.api.serializers import NumberSequenceSerializer
from erp.core.sequences.models import NumberSequence


class NumberSequenceViewSet(ERPReadOnlyViewSet):
    serializer_class = NumberSequenceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = NumberSequence.objects.select_related("firm")
        firm_id = self.request.query_params.get("firm_id")
        if firm_id:
            qs = qs.filter(firm_id=firm_id)
        return qs
