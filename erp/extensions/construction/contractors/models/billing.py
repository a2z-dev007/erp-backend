from django.db import models

from erp.common.models import ScopedModel


class SubcontractorBill(ScopedModel):
    work_order = models.ForeignKey(
        "ext_construction_contractors.WorkOrder",
        on_delete=models.RESTRICT,
        related_name="bills",
    )
    code = models.CharField(max_length=32)
    bill_date = models.DateField()
    gross_inr = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    retention_inr = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    class Meta:
        unique_together = ("firm", "code")
        ordering = ("-bill_date",)
