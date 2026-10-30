from rest_framework import viewsets

from erp.common.api.responses import envelope_body


class EnvelopeMixin:
    """Wrap successful non-paginated DRF payloads in { data, meta }."""

    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)
        if hasattr(response, "data") and isinstance(response.data, dict):
            if "data" not in response.data and "error" not in response.data:
                if getattr(response, "exception", None) is None and response.status_code < 400:
                    response.data = envelope_body(response.data)
        return response


class ERPReadOnlyViewSet(EnvelopeMixin, viewsets.ReadOnlyModelViewSet):
    """Authenticated list/retrieve for seeded demo resources."""

    pass
