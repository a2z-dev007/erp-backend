from rest_framework.routers import DefaultRouter

from erp.extensions.construction.variations.api.views import (
    ProjectProgressRecordViewSet,
    VariationOrderViewSet,
)

router = DefaultRouter()
router.register("construction/variation-orders", VariationOrderViewSet, basename="variation-order")
router.register("construction/progress-records", ProjectProgressRecordViewSet, basename="progress-record")

urlpatterns = router.urls
