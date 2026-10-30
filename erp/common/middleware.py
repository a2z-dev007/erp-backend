import uuid

from erp.common.api.context import request_id_ctx


class RequestIDMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())
        request.request_id = request_id
        token = request_id_ctx.set(request_id)
        try:
            response = self.get_response(request)
        finally:
            request_id_ctx.reset(token)
        response["X-Request-ID"] = request_id
        return response
