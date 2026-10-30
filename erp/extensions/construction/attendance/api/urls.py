from rest_framework.routers import DefaultRouter

from erp.extensions.construction.attendance.api.views import SiteAttendanceViewSet

router = DefaultRouter()
router.register("construction/site-attendance", SiteAttendanceViewSet, basename="site-attendance")

urlpatterns = router.urls
