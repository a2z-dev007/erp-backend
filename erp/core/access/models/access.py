from django.conf import settings
from django.db import models

from erp.common.models import TimestampedModel, UUIDModel


class Permission(UUIDModel, TimestampedModel):
    code = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        ordering = ("code",)

    def __str__(self) -> str:
        return self.code


class Role(UUIDModel, TimestampedModel):
    code = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=128)
    permissions = models.ManyToManyField(
        Permission,
        through="RolePermission",
        related_name="roles",
    )

    class Meta:
        ordering = ("code",)

    def __str__(self) -> str:
        return self.name


class RolePermission(UUIDModel):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("role", "permission")


class UserRoleAssignment(UUIDModel, TimestampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="role_assignments",
    )
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name="assignments")
    scope_json = models.JSONField(default=dict, blank=True)

    class Meta:
        unique_together = ("user", "role")
