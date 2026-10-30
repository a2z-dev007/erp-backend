from rest_framework import serializers

from erp.extensions.construction.evidence.models import FieldEvidence


class FieldEvidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldEvidence
        fields = (
            "id",
            "site_id",
            "title",
            "photo_key",
            "latitude",
            "longitude",
            "captured_at",
            "created_at",
            "updated_at",
        )
