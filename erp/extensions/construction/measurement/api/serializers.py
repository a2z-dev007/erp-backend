from rest_framework import serializers

from erp.extensions.construction.measurement.models import MeasurementBook


class MeasurementBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementBook
        fields = "__all__"
