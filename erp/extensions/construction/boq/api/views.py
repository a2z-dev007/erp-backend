from erp.common.api.module_api import readonly_viewset
from erp.extensions.construction.boq.api.serializers import BoqSerializer
from erp.extensions.construction.boq.models import Boq

BoqViewSet = readonly_viewset(Boq, BoqSerializer, select_related=("project",))
