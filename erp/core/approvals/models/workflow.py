from django.db import models

from erp.common.models import ScopedModel


class WorkflowDefinition(ScopedModel):
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=128)
    module_key = models.CharField(max_length=64)

    class Meta:
        unique_together = ("firm", "code")
        ordering = ("code",)
