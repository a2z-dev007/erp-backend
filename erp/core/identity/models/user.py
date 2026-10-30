import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from erp.core.identity.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    class UserType(models.TextChoices):
        INTERNAL = "internal", "Internal"
        CONTRACTOR = "contractor", "Contractor"
        CLIENT = "client", "Client"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255, blank=True)
    user_type = models.CharField(
        max_length=20,
        choices=UserType.choices,
        default=UserType.INTERNAL,
    )
    contractor_party_id = models.UUIDField(null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: list[str] = []

    objects = UserManager()

    def __str__(self) -> str:
        return self.email
