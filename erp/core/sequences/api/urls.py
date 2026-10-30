from rest_framework.routers import DefaultRouter

from erp.core.sequences.api.views import NumberSequenceViewSet

router = DefaultRouter()
router.register("sequences", NumberSequenceViewSet, basename="number-sequence")

urlpatterns = router.urls
