"""Minimal read-only list API used by demo / scaffold modules."""

from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from erp.common.api.viewsets import ERPReadOnlyViewSet


def readonly_viewset(model, serializer_cls=None, select_related=None):
    if serializer_cls is None:

        class _AutoSerializer(serializers.ModelSerializer):
            class Meta:
                model = model
                fields = "__all__"

        serializer_cls = _AutoSerializer

    rel = select_related or ()

    class _ViewSet(ERPReadOnlyViewSet):
        serializer_class = serializer_cls
        permission_classes = [IsAuthenticated]

        def get_queryset(self):
            qs = model.objects.all()
            if rel:
                qs = qs.select_related(*rel)
            firm_id = self.request.query_params.get("firm_id")
            if firm_id and hasattr(model, "firm_id"):
                qs = qs.filter(firm_id=firm_id)
            project_id = self.request.query_params.get("project_id")
            if project_id and hasattr(model, "project_id"):
                qs = qs.filter(project_id=project_id)
            site_id = self.request.query_params.get("site_id")
            if site_id and hasattr(model, "site_id"):
                qs = qs.filter(site_id=site_id)
            return qs

    return _ViewSet
