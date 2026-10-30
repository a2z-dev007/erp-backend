from rest_framework.routers import DefaultRouter

from erp.extensions.construction.requests.api.line_views import MaterialRequestLineViewSet
from erp.extensions.construction.requests.api.views import MaterialRequestViewSet

router = DefaultRouter()
router.register("construction/material-requests", MaterialRequestViewSet, basename="material-request")
router.register("construction/material-request-lines", MaterialRequestLineViewSet, basename="material-request-line")

urlpatterns = router.urls
