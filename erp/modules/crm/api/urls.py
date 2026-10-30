from rest_framework.routers import DefaultRouter

from erp.modules.crm.api.customer_views import CustomerViewSet
from erp.modules.crm.api.views import LeadViewSet

router = DefaultRouter()
router.register("crm/customers", CustomerViewSet, basename="crm-customer")
router.register("crm/leads", LeadViewSet, basename="crm-lead")

urlpatterns = router.urls
