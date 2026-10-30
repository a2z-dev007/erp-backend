from django.conf import settings
from django.db import models

from erp.common.models import TimestampedModel, UUIDModel


class Branch(UUIDModel, TimestampedModel):
    firm = models.ForeignKey("core_organization.Firm", on_delete=models.RESTRICT, related_name="branches")
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=128, blank=True)

    class Meta:
        unique_together = ("firm", "code")
        ordering = ("code",)

    def __str__(self) -> str:
        return self.name


class Department(UUIDModel, TimestampedModel):
    firm = models.ForeignKey("core_organization.Firm", on_delete=models.RESTRICT, related_name="departments")
    branch = models.ForeignKey(
        Branch,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="departments",
    )
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = ("firm", "code")
        ordering = ("code",)

    def __str__(self) -> str:
        return self.name


class Firm(UUIDModel, TimestampedModel):
    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"

    code = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=255)
    pan = models.CharField(max_length=16, blank=True)
    gstin = models.CharField(max_length=20, blank=True)
    fy_start_month = models.PositiveSmallIntegerField(default=4)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)

    def __str__(self) -> str:
        return self.name


class Project(UUIDModel, TimestampedModel):
    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"

    firm = models.ForeignKey(Firm, on_delete=models.RESTRICT, related_name="projects")
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=255)
    client_name = models.CharField(max_length=255, blank=True)
    contract_value_inr = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="managed_projects",
    )
    starts_on = models.DateField(null=True, blank=True)
    ends_on = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)

    class Meta:
        unique_together = ("firm", "code")

    def __str__(self) -> str:
        return self.name


class Site(UUIDModel, TimestampedModel):
    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"

    project = models.ForeignKey(Project, on_delete=models.RESTRICT, related_name="sites")
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)

    class Meta:
        unique_together = ("project", "code")

    @property
    def firm_id(self):
        return self.project.firm_id

    def __str__(self) -> str:
        return self.name


class Store(UUIDModel, TimestampedModel):
    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"

    site = models.ForeignKey(Site, on_delete=models.RESTRICT, related_name="stores")
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)

    class Meta:
        unique_together = ("site", "code")

    def __str__(self) -> str:
        return self.name


class CostCode(UUIDModel, TimestampedModel):
    class Status(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"

    project = models.ForeignKey(Project, on_delete=models.RESTRICT, related_name="cost_codes")
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)

    class Meta:
        unique_together = ("project", "code")

    def __str__(self) -> str:
        return self.code
