from erp.common.api.module_api import readonly_viewset
from erp.extensions.construction.measurement.api.serializers import MeasurementBookSerializer
from erp.extensions.construction.measurement.models import MeasurementBook

MeasurementBookViewSet = readonly_viewset(
    MeasurementBook,
    MeasurementBookSerializer,
    select_related=("project",),
)
