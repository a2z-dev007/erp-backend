from rest_framework import serializers

from erp.modules.inventory.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = (
            "id",
            "firm_id",
            "code",
            "name",
            "uom",
            "category",
            "reorder_level",
            "created_at",
            "updated_at",
        )
