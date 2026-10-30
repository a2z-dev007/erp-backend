from rest_framework.routers import DefaultRouter

from erp.extensions.construction.equipment.api.views import EquipmentAssetViewSet

router = DefaultRouter()
router.register("construction/equipment", EquipmentAssetViewSet, basename="equipment-asset")

urlpatterns = router.urls
