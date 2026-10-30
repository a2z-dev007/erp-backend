from rest_framework.views import exception_handler

from erp.common.api.responses import error_envelope


def erp_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is None:
        return error_envelope(
            "internal_error",
            "An unexpected error occurred.",
            status=500,
        )

    code = "validation_error"
    if response.status_code == 401:
        code = "authentication_required"
    elif response.status_code == 403:
        code = "permission_denied"
    elif response.status_code == 404:
        code = "not_found"
    elif response.status_code == 409:
        code = "invalid_state"

    fields = {}
    message = str(exc)
    if isinstance(response.data, dict):
        if "detail" in response.data:
            message = str(response.data["detail"])
        else:
            fields = response.data
            message = "Invalid input."

    response.data = {
        "error": {"code": code, "message": message, "fields": fields},
        "meta": {"request_id": getattr(context["request"], "request_id", "")},
    }
    return response
