from django.db import models

from erp.common.models import ScopedModel


class Document(ScopedModel):
    title = models.CharField(max_length=255)
    object_key = models.CharField(max_length=512)
    content_type = models.CharField(max_length=128, default="application/octet-stream")
    size_bytes = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ("title",)

    def __str__(self) -> str:
        return self.title
