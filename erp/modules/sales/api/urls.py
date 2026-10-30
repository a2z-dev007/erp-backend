from rest_framework.routers import DefaultRouter

from erp.modules.sales.api.views import (
    ClientContractViewSet,
    SalesInvoiceViewSet,
    SalesOrderViewSet,
)

router = DefaultRouter()
router.register("sales/orders", SalesOrderViewSet, basename="sales-order")
router.register("sales/invoices", SalesInvoiceViewSet, basename="sales-invoice")
router.register("sales/contracts", ClientContractViewSet, basename="client-contract")

urlpatterns = router.urls
