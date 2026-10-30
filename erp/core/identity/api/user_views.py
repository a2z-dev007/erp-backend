from rest_framework.permissions import IsAuthenticated

from erp.common.api.viewsets import ERPReadOnlyViewSet
from erp.core.identity.api.serializers import UserListSerializer
from erp.core.identity.models import User


class UserViewSet(ERPReadOnlyViewSet):
    queryset = User.objects.filter(is_active=True).order_by("email")
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]
