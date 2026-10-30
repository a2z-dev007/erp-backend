from rest_framework.routers import DefaultRouter

from erp.modules.hr.api.views import EmployeeViewSet

router = DefaultRouter()
router.register("hr/employees", EmployeeViewSet, basename="employee")

urlpatterns = router.urls
