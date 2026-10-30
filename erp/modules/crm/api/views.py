from erp.common.api.module_api import readonly_viewset
from erp.modules.crm.api.serializers import LeadSerializer
from erp.modules.crm.models import Lead

LeadViewSet = readonly_viewset(Lead, LeadSerializer, select_related=("firm",))
