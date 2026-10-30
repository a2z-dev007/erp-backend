from rest_framework import serializers

from erp.core.identity.models import User


class UserMeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "full_name",
            "user_type",
            "contractor_party_id",
            "is_active",
        )


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "full_name",
            "user_type",
            "is_active",
            "date_joined",
        )


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)


class LoginResponseSerializer(serializers.Serializer):
    """Returned in envelope `data` after successful login."""

    token = serializers.CharField()
    id = serializers.UUIDField()
    email = serializers.EmailField()
    full_name = serializers.CharField()
    user_type = serializers.CharField()
    contractor_party_id = serializers.UUIDField(allow_null=True)
    is_active = serializers.BooleanField()
