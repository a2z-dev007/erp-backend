from rest_framework.routers import DefaultRouter

from erp.modules.procurement.api.grn_views import GoodsReceiptNoteViewSet, PurchaseInvoiceViewSet
from erp.modules.procurement.api.vendor_views import VendorViewSet
from erp.modules.procurement.api.views import PurchaseOrderViewSet

router = DefaultRouter()
router.register("procurement/vendors", VendorViewSet, basename="vendor")
router.register("procurement/purchase-orders", PurchaseOrderViewSet, basename="purchase-order")
router.register("procurement/grns", GoodsReceiptNoteViewSet, basename="grn")
router.register("procurement/purchase-invoices", PurchaseInvoiceViewSet, basename="purchase-invoice")

urlpatterns = router.urls
