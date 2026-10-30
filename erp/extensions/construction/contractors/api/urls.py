from rest_framework.routers import DefaultRouter

from erp.extensions.construction.contractors.api.billing_views import SubcontractorBillViewSet
from erp.extensions.construction.contractors.api.views import ContractorPartyViewSet
from erp.extensions.construction.contractors.api.work_order_views import WorkOrderViewSet

router = DefaultRouter()
router.register("construction/contractors", ContractorPartyViewSet, basename="contractor-party")
router.register("construction/work-orders", WorkOrderViewSet, basename="work-order")
router.register("construction/subcontractor-bills", SubcontractorBillViewSet, basename="subcontractor-bill")

urlpatterns = router.urls
