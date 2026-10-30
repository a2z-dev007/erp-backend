from rest_framework import mixins, viewsets

from erp.core.access.api.permissions import HasERPPermission
from erp.core.organization.api.serializers import (
    CostCodeSerializer,
    FirmSerializer,
    ProjectSerializer,
    SiteSerializer,
    StoreSerializer,
)
from erp.core.organization.models import CostCode, Firm, Project, Site, Store
from erp.core.organization.selectors.organization import (
    cost_codes_for_user,
    firms_for_user,
    projects_for_user,
    sites_for_user,
    stores_for_user,
)
from erp.common.api.viewsets import EnvelopeMixin


class FirmViewSet(EnvelopeMixin, viewsets.ModelViewSet):
    serializer_class = FirmSerializer
    permission_classes = [HasERPPermission]
    required_permission = "organisation.firm.view"

    def get_queryset(self):
        return firms_for_user(self.request.user, q=self.request.query_params.get("q"))

    def get_permissions(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            self.required_permission = "organisation.firm.manage"
        else:
            self.required_permission = "organisation.firm.view"
        return super().get_permissions()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class ProjectViewSet(EnvelopeMixin, viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    permission_classes = [HasERPPermission]

    def get_queryset(self):
        return projects_for_user(
            self.request.user,
            firm_id=self.request.query_params.get("firm_id"),
            q=self.request.query_params.get("q"),
        )

    def get_permissions(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            self.required_permission = "organisation.project.manage"
        else:
            self.required_permission = "organisation.project.view"
        return super().get_permissions()

class SiteViewSet(EnvelopeMixin, viewsets.ModelViewSet):
    serializer_class = SiteSerializer
    permission_classes = [HasERPPermission]

    def get_queryset(self):
        return sites_for_user(
            self.request.user,
            project_id=self.request.query_params.get("project_id"),
            q=self.request.query_params.get("q"),
        )

    def get_permissions(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            self.required_permission = "organisation.site.manage"
        else:
            self.required_permission = "organisation.site.view"
        return super().get_permissions()


class StoreViewSet(EnvelopeMixin, viewsets.ModelViewSet):
    serializer_class = StoreSerializer
    permission_classes = [HasERPPermission]

    def get_queryset(self):
        return stores_for_user(
            self.request.user,
            site_id=self.request.query_params.get("site_id"),
            q=self.request.query_params.get("q"),
        )

    def get_permissions(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            self.required_permission = "organisation.store.manage"
        else:
            self.required_permission = "organisation.store.view"
        return super().get_permissions()


class CostCodeViewSet(EnvelopeMixin, viewsets.ModelViewSet):
    serializer_class = CostCodeSerializer
    permission_classes = [HasERPPermission]

    def get_queryset(self):
        return cost_codes_for_user(
            self.request.user,
            project_id=self.request.query_params.get("project_id"),
            q=self.request.query_params.get("q"),
        )

    def get_permissions(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            self.required_permission = "organisation.cost_code.manage"
        else:
            self.required_permission = "organisation.cost_code.view"
        return super().get_permissions()
