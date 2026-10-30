from rest_framework import serializers

from erp.extensions.construction.contractors.models import ContractorParty


class ContractorPartySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractorParty
        fields = (
            "id",
            "firm_id",
            "code",
            "name",
            "contact_person",
            "phone",
            "pan",
            "created_at",
            "updated_at",
        )
