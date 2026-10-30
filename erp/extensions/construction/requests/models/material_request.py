from django.db import models

from erp.common.models import TimestampedModel, UUIDModel


class MaterialRequest(UUIDModel, TimestampedModel):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        SUBMITTED = "submitted", "Submitted"
        APPROVED = "approved", "Approved"
        FULFILLED = "fulfilled", "Fulfilled"

    class Priority(models.TextChoices):
        LOW = "low", "Low"
        NORMAL = "normal", "Normal"
        HIGH = "high", "High"

    site = models.ForeignKey(
        "core_organization.Site",
        on_delete=models.RESTRICT,
        related_name="material_requests",
    )
    code = models.CharField(max_length=32)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.DRAFT)
    priority = models.CharField(max_length=16, choices=Priority.choices, default=Priority.NORMAL)
    needed_on = models.DateField(null=True, blank=True)

    class Meta:
        unique_together = ("site", "code")
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.code
