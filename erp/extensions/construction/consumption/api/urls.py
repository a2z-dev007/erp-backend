from rest_framework.routers import DefaultRouter

from erp.extensions.construction.consumption.api.views import MaterialConsumptionViewSet

router = DefaultRouter()
router.register(
    "construction/material-consumptions",
    MaterialConsumptionViewSet,
    basename="material-consumption",
)

urlpatterns = router.urls
