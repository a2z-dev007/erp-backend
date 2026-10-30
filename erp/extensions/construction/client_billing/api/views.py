from erp.common.api.module_api import readonly_viewset
from erp.extensions.construction.client_billing.api.serializers import ClientBillSerializer
from erp.extensions.construction.client_billing.models import ClientBill

ClientBillViewSet = readonly_viewset(
    ClientBill,
    ClientBillSerializer,
    select_related=("project",),
)
