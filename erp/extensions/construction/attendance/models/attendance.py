from django.db import models

from erp.common.models import TimestampedModel, UUIDModel


class SiteAttendance(UUIDModel, TimestampedModel):
    class Status(models.TextChoices):
        PRESENT = "present", "Present"
        ABSENT = "absent", "Absent"

    site = models.ForeignKey(
        "core_organization.Site",
        on_delete=models.RESTRICT,
        related_name="attendance_records",
    )
    employee = models.ForeignKey(
        "mod_hr.Employee",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="attendance_records",
    )
    attendance_date = models.DateField()
    status = models.CharField(max_length=16, choices=Status.choices, default=Status.PRESENT)

    class Meta:
        unique_together = ("site", "employee", "attendance_date")
        ordering = ("-attendance_date",)
