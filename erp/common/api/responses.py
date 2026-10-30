from typing import Any

from rest_framework.response import Response

from erp.common.api.context import request_id_ctx


def envelope_body(data: Any = None, meta: dict | None = None) -> dict[str, Any]:
    return {
        "data": data,
        "meta": {"request_id": request_id_ctx.get(), **(meta or {})},
    }


def envelope(data: Any = None, meta: dict | None = None, status: int = 200) -> Response:
    return Response(envelope_body(data, meta=meta), status=status)


def error_envelope(
    code: str,
    message: str,
    fields: dict | None = None,
    status: int = 400,
) -> Response:
    body = {
        "error": {
            "code": code,
            "message": message,
            "fields": fields or {},
        },
        "meta": {"request_id": request_id_ctx.get()},
    }
    return Response(body, status=status)
