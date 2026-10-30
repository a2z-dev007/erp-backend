from django.conf import settings
from django.db import models

from erp.common.models import ScopedModel


class ApprovalRequest(ScopedModel):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        APPROVED = "approved", "Approved"
        REJECTED = "rejected", "Rejected"

    reference_type = models.CharField(max_length=64)
    reference_id = models.UUIDField()
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    requester = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="approval_requests",
    )

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.title
