from django.db import models

from erp.common.models import ScopedModel


class ImportBatch(ScopedModel):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        RUNNING = "running", "Running"
        COMPLETED = "completed", "Completed"
        FAILED = "failed", "Failed"

    module_key = models.CharField(max_length=64)
    file_name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    total_rows = models.PositiveIntegerField(default=0)
    error_rows = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return self.file_name
