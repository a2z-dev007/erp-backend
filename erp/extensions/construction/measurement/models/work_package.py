from django.db import models

from erp.common.models import TimestampedModel, UUIDModel


class WorkPackage(UUIDModel, TimestampedModel):
    project = models.ForeignKey(
        "core_organization.Project",
        on_delete=models.RESTRICT,
        related_name="work_packages",
    )
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = ("project", "code")
        ordering = ("code",)
