from rest_framework import serializers

from erp.core.documents.models import Document


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = (
            "id",
            "firm_id",
            "title",
            "object_key",
            "content_type",
            "size_bytes",
            "created_at",
            "updated_at",
        )
