from rest_framework import serializers

from erp.extensions.construction.consumption.models import MaterialConsumption


class MaterialConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialConsumption
        fields = "__all__"
