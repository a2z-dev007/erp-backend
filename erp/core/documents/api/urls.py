from rest_framework.routers import DefaultRouter

from erp.core.documents.api.views import DocumentViewSet

router = DefaultRouter()
router.register("documents", DocumentViewSet, basename="document")

urlpatterns = router.urls
