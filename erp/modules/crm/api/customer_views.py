from rest_framework import serializers

from erp.common.api.module_api import readonly_viewset
from erp.modules.crm.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


CustomerViewSet = readonly_viewset(Customer, CustomerSerializer, select_related=("firm",))
