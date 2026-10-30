from django.db import connection
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from erp.common.api.responses import envelope, error_envelope


class HealthView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, request):
        try:
            connection.ensure_connection()
            connection.cursor().execute("SELECT 1")
        except Exception as exc:
            return error_envelope(
                "internal_error",
                f"Database unavailable: {exc}",
                status=503,
            )
        return envelope({"status": "ok", "database": "connected"})
