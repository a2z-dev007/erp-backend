from rest_framework import serializers

from erp.core.imports.models import ImportBatch


class ImportBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportBatch
        fields = (
            "id",
            "firm_id",
            "module_key",
            "file_name",
            "status",
            "total_rows",
            "error_rows",
            "created_at",
            "updated_at",
        )
