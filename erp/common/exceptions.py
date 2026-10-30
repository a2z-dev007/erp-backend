from rest_framework.exceptions import APIException


class ERPValidationError(APIException):
    status_code = 400
    default_code = "validation_error"
    default_detail = "Invalid input."
