from rest_framework.routers import DefaultRouter

from erp.modules.assets.api.views import FixedAssetViewSet

router = DefaultRouter()
router.register("assets/fixed-assets", FixedAssetViewSet, basename="fixed-asset")

urlpatterns = router.urls
