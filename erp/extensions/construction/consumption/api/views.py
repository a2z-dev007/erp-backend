from erp.common.api.module_api import readonly_viewset
from erp.extensions.construction.consumption.api.serializers import MaterialConsumptionSerializer
from erp.extensions.construction.consumption.models import MaterialConsumption

MaterialConsumptionViewSet = readonly_viewset(
    MaterialConsumption,
    MaterialConsumptionSerializer,
    select_related=("site", "item"),
)
