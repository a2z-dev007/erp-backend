from rest_framework import serializers

from erp.core.organization.models import CostCode, Firm, Project, Site, Store


class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = (
            "id",
            "code",
            "name",
            "pan",
            "gstin",
            "fy_start_month",
            "status",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")


class ProjectSerializer(serializers.ModelSerializer):
    firm_id = serializers.PrimaryKeyRelatedField(source="firm", queryset=Firm.objects.all())

    class Meta:
        model = Project
        fields = (
            "id",
            "firm_id",
            "code",
            "name",
            "client_name",
            "contract_value_inr",
            "manager",
            "starts_on",
            "ends_on",
            "status",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")


class SiteSerializer(serializers.ModelSerializer):
    project_id = serializers.PrimaryKeyRelatedField(source="project", queryset=Project.objects.all())
    firm_id = serializers.UUIDField(source="project.firm_id", read_only=True)

    class Meta:
        model = Site
        fields = (
            "id",
            "firm_id",
            "project_id",
            "code",
            "name",
            "status",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")


class StoreSerializer(serializers.ModelSerializer):
    site_id = serializers.PrimaryKeyRelatedField(source="site", queryset=Site.objects.all())
    project_id = serializers.UUIDField(source="site.project_id", read_only=True)

    class Meta:
        model = Store
        fields = (
            "id",
            "project_id",
            "site_id",
            "code",
            "name",
            "status",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")


class CostCodeSerializer(serializers.ModelSerializer):
    project_id = serializers.PrimaryKeyRelatedField(source="project", queryset=Project.objects.all())

    class Meta:
        model = CostCode
        fields = (
            "id",
            "project_id",
            "code",
            "name",
            "status",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")
