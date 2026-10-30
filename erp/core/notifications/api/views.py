from rest_framework.permissions import IsAuthenticated

from erp.common.api.viewsets import ERPReadOnlyViewSet
from erp.core.notifications.api.serializers import NotificationSerializer
from erp.core.notifications.models import Notification


class NotificationViewSet(ERPReadOnlyViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user).select_related("user")
