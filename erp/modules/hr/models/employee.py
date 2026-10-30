from django.db import models

from erp.common.models import ScopedModel


class Employee(ScopedModel):
    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"

    department = models.ForeignKey(
        "core_organization.Department",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="employees",
    )
    code = models.CharField(max_length=32)
    full_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=128, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)

    class Meta:
        unique_together = ("firm", "code")
        ordering = ("full_name",)
