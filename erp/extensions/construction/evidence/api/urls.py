from rest_framework.routers import DefaultRouter

from erp.extensions.construction.evidence.api.views import FieldEvidenceViewSet

router = DefaultRouter()
router.register("construction/evidence", FieldEvidenceViewSet, basename="field-evidence")

urlpatterns = router.urls
