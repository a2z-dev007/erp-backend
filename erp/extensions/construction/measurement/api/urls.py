from rest_framework.routers import DefaultRouter

from erp.extensions.construction.measurement.api.views import MeasurementBookViewSet
from erp.extensions.construction.measurement.api.work_package_views import WorkPackageViewSet

router = DefaultRouter()
router.register("construction/measurement-books", MeasurementBookViewSet, basename="measurement-book")
router.register("construction/work-packages", WorkPackageViewSet, basename="work-package")

urlpatterns = router.urls
