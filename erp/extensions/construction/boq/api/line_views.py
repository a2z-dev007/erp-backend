from rest_framework import serializers

from erp.common.api.module_api import readonly_viewset
from erp.extensions.construction.boq.models import BoqLine


class BoqLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoqLine
        fields = "__all__"


BoqLineViewSet = readonly_viewset(BoqLine, BoqLineSerializer, select_related=("boq",))
