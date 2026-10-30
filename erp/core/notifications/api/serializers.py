from rest_framework import serializers

from erp.core.notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = (
            "id",
            "user_id",
            "title",
            "message",
            "channel",
            "is_read",
            "created_at",
            "updated_at",
        )
