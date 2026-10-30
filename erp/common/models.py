import uuid

from django.db import models


class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ScopedModel(UUIDModel, TimestampedModel):
    """Records scoped to a firm (multi-firm within one deployment)."""

    firm = models.ForeignKey(
        "core_organization.Firm",
        on_delete=models.RESTRICT,
        related_name="%(class)s_set",
    )

    class Meta:
        abstract = True
