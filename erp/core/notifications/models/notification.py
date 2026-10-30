from django.conf import settings
from django.db import models

from erp.common.models import TimestampedModel, UUIDModel


class Notification(UUIDModel, TimestampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="notifications",
    )
    title = models.CharField(max_length=255)
    message = models.TextField(blank=True)
    channel = models.CharField(max_length=32, default="in_app")
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.title
