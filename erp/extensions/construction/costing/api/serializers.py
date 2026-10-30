from rest_framework import serializers

from erp.extensions.construction.costing.models import ProjectBudget


class ProjectBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectBudget
        fields = "__all__"
