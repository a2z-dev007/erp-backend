from rest_framework import serializers

from erp.common.api.module_api import readonly_viewset
from erp.modules.finance.models import GLEntry, LedgerAccount, Payment, TaxCategory


class TaxCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TaxCategory
        fields = "__all__"


class LedgerAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = LedgerAccount
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class GLEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = GLEntry
        fields = "__all__"


TaxCategoryViewSet = readonly_viewset(TaxCategory, TaxCategorySerializer, select_related=("firm",))
LedgerAccountViewSet = readonly_viewset(LedgerAccount, LedgerAccountSerializer, select_related=("firm",))
PaymentViewSet = readonly_viewset(Payment, PaymentSerializer, select_related=("firm",))
GLEntryViewSet = readonly_viewset(GLEntry, GLEntrySerializer, select_related=("firm", "account", "voucher"))
