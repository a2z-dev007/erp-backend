from rest_framework import serializers

from erp.extensions.construction.requests.models import MaterialRequest


class MaterialRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialRequest
        fields = (
            "id",
            "site_id",
            "code",
            "status",
            "priority",
            "needed_on",
            "created_at",
            "updated_at",
        )
