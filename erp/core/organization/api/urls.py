from rest_framework.routers import DefaultRouter

from erp.core.organization.api.org_unit_views import BranchViewSet, DepartmentViewSet
from erp.core.organization.api.views import (
    CostCodeViewSet,
    FirmViewSet,
    ProjectViewSet,
    SiteViewSet,
    StoreViewSet,
)

router = DefaultRouter()
router.register("branches", BranchViewSet, basename="branch")
router.register("departments", DepartmentViewSet, basename="department")
router.register("firms", FirmViewSet, basename="firm")
router.register("projects", ProjectViewSet, basename="project")
router.register("sites", SiteViewSet, basename="site")
router.register("stores", StoreViewSet, basename="store")
router.register("cost-codes", CostCodeViewSet, basename="cost-code")

urlpatterns = router.urls
