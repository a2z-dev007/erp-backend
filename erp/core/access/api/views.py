from rest_framework.permissions import IsAuthenticated

from erp.common.api.viewsets import ERPReadOnlyViewSet
from erp.core.access.api.serializers import PermissionSerializer, RoleSerializer
from erp.core.access.models import Permission, Role


class PermissionViewSet(ERPReadOnlyViewSet):
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [IsAuthenticated]


class RoleViewSet(ERPReadOnlyViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [IsAuthenticated]
