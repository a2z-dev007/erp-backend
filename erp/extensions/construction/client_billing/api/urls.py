from rest_framework.routers import DefaultRouter

from erp.extensions.construction.client_billing.api.retention_views import RetentionRecordViewSet
from erp.extensions.construction.client_billing.api.views import ClientBillViewSet

router = DefaultRouter()
router.register("construction/client-bills", ClientBillViewSet, basename="client-bill")
router.register("construction/retention-records", RetentionRecordViewSet, basename="retention-record")

urlpatterns = router.urls
