from rest_framework.routers import DefaultRouter

from erp.core.approvals.api.views import ApprovalRequestViewSet
from erp.core.approvals.api.workflow_views import WorkflowDefinitionViewSet

router = DefaultRouter()
router.register("approvals/workflows", WorkflowDefinitionViewSet, basename="workflow-definition")
router.register("approvals/requests", ApprovalRequestViewSet, basename="approval-request")

urlpatterns = router.urls
