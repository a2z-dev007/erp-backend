from erp.common.api.module_api import readonly_viewset
from erp.extensions.construction.costing.api.serializers import ProjectBudgetSerializer
from erp.extensions.construction.costing.models import ProjectBudget

ProjectBudgetViewSet = readonly_viewset(
    ProjectBudget,
    ProjectBudgetSerializer,
    select_related=("project",),
)
