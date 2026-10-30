from rest_framework.routers import DefaultRouter

from erp.extensions.construction.quality.api.views import QualityInspectionViewSet

router = DefaultRouter()
router.register("construction/quality-inspections", QualityInspectionViewSet, basename="quality-inspection")

urlpatterns = router.urls
