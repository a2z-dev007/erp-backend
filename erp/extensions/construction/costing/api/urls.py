from rest_framework.routers import DefaultRouter

from erp.extensions.construction.costing.api.views import ProjectBudgetViewSet

router = DefaultRouter()
router.register("construction/project-budgets", ProjectBudgetViewSet, basename="project-budget")

urlpatterns = router.urls
