from rest_framework import serializers

from erp.core.audit.models import AuditEvent


class AuditEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditEvent
        fields = (
            "id",
            "firm_id",
            "action",
            "entity_type",
            "entity_id",
            "actor_id",
            "summary",
            "payload",
            "created_at",
            "updated_at",
        )
