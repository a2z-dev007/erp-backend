from rest_framework import serializers

from erp.core.sequences.models import NumberSequence


class NumberSequenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NumberSequence
        fields = (
            "id",
            "firm_id",
            "code",
            "prefix",
            "current_value",
            "created_at",
            "updated_at",
        )
