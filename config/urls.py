from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from erp.common.api.views import HealthView

api_v1_patterns = [
    path("health/", HealthView.as_view(), name="health"),
    path("", include("erp.core.identity.api.urls")),
    path("organisation/", include("erp.core.organization.api.urls")),
    path("", include("erp.core.access.api.urls")),
    path("", include("erp.core.approvals.api.urls")),
    path("", include("erp.core.audit.api.urls")),
    path("", include("erp.core.documents.api.urls")),
    path("", include("erp.core.sequences.api.urls")),
    path("", include("erp.core.imports.api.urls")),
    path("", include("erp.core.notifications.api.urls")),
    path("", include("erp.modules.inventory.api.urls")),
    path("", include("erp.modules.procurement.api.urls")),
    path("", include("erp.modules.finance.api.urls")),
    path("", include("erp.modules.crm.api.urls")),
    path("", include("erp.modules.sales.api.urls")),
    path("", include("erp.modules.hr.api.urls")),
    path("", include("erp.modules.assets.api.urls")),
    path("", include("erp.extensions.construction.requests.api.urls")),
    path("", include("erp.extensions.construction.contractors.api.urls")),
    path("", include("erp.extensions.construction.evidence.api.urls")),
    path("", include("erp.extensions.construction.boq.api.urls")),
    path("", include("erp.extensions.construction.measurement.api.urls")),
    path("", include("erp.extensions.construction.client_billing.api.urls")),
    path("", include("erp.extensions.construction.costing.api.urls")),
    path("", include("erp.extensions.construction.consumption.api.urls")),
    path("", include("erp.extensions.construction.equipment.api.urls")),
    path("", include("erp.extensions.construction.attendance.api.urls")),
    path("", include("erp.extensions.construction.quality.api.urls")),
    path("", include("erp.extensions.construction.variations.api.urls")),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/v1/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/v1/", include(api_v1_patterns)),
]
