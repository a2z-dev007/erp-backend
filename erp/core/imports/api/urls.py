from rest_framework.routers import DefaultRouter

from erp.core.imports.api.views import ImportBatchViewSet

router = DefaultRouter()
router.register("imports/batches", ImportBatchViewSet, basename="import-batch")

urlpatterns = router.urls
