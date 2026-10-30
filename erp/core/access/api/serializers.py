from rest_framework import serializers

from erp.core.access.models import Permission, Role


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ("id", "code", "description", "created_at", "updated_at")


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ("id", "code", "name", "created_at", "updated_at")
