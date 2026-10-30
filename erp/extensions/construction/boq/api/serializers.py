from rest_framework import serializers

from erp.extensions.construction.boq.models import Boq


class BoqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boq
        fields = "__all__"
