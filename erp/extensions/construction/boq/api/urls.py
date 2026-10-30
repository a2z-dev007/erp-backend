from rest_framework.routers import DefaultRouter

from erp.extensions.construction.boq.api.line_views import BoqLineViewSet
from erp.extensions.construction.boq.api.views import BoqViewSet

router = DefaultRouter()
router.register("construction/boqs", BoqViewSet, basename="construction-boq")
router.register("construction/boq-lines", BoqLineViewSet, basename="construction-boq-line")

urlpatterns = router.urls
