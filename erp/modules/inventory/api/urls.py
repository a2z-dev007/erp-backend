from rest_framework.routers import DefaultRouter

from erp.modules.inventory.api.ledger_views import StockLedgerEntryViewSet
from erp.modules.inventory.api.stock_views import StockBalanceViewSet
from erp.modules.inventory.api.views import ItemViewSet

router = DefaultRouter()
router.register("inventory/items", ItemViewSet, basename="inventory-item")
router.register("inventory/stock", StockBalanceViewSet, basename="inventory-stock")
router.register("inventory/stock-ledger", StockLedgerEntryViewSet, basename="stock-ledger-entry")

urlpatterns = router.urls
