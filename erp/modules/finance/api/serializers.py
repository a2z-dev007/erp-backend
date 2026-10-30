from rest_framework import serializers

from erp.modules.finance.models import Voucher


class VoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voucher
        fields = (
            "id",
            "firm_id",
            "voucher_number",
            "voucher_date",
            "voucher_type",
            "status",
            "amount_inr",
            "narration",
            "created_at",
            "updated_at",
        )
