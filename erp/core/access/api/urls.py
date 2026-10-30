from rest_framework.routers import DefaultRouter

from erp.core.access.api.views import PermissionViewSet, RoleViewSet

router = DefaultRouter()
router.register("access/permissions", PermissionViewSet, basename="permission")
router.register("access/roles", RoleViewSet, basename="role")

urlpatterns = router.urls
