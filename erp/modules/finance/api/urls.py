from rest_framework.routers import DefaultRouter

from erp.modules.finance.api.ledger_views import (
    GLEntryViewSet,
    LedgerAccountViewSet,
    PaymentViewSet,
    TaxCategoryViewSet,
)
from erp.modules.finance.api.views import VoucherViewSet

router = DefaultRouter()
router.register("finance/vouchers", VoucherViewSet, basename="finance-voucher")
router.register("finance/ledger-accounts", LedgerAccountViewSet, basename="ledger-account")
router.register("finance/gl-entries", GLEntryViewSet, basename="gl-entry")
router.register("finance/payments", PaymentViewSet, basename="payment")
router.register("finance/tax-categories", TaxCategoryViewSet, basename="tax-category")

urlpatterns = router.urls
