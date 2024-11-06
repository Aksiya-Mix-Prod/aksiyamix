from rest_framework.exceptions import APIException


class BasePaymeException(APIException):

    status_code = 200
    error_code = None
    message = None

    def __init__(self, error_message: str = None):
        detail: dict = {
            "error": {
                "code": self.error_code,
                "message": self.message,
                "data": error_message
            }
        }
        self.detail = detail


class PermissionDenied(BasePaymeException):
    """
    PermissionDenied APIException \
        That is raised when the client is not allowed to server.
    """
    status_code = 200
    error_code = -32504
    message = "Permission denied"


class MethodNotFound(BasePaymeException):
    """
    MethodNotFound APIException \
        That is raised when the method does not exist.
    """
    status_code = 405
    error_code = -32601
    message = 'Method not found'


class TooManyRequests(BasePaymeException):
    """
    TooManyRequests APIException \
        That is raised when the request exceeds the limit.
    """
    status_code = 200
    error_code = -31099
    message = {
        "uz": "Buyurtma tolovni amalga oshirish jarayonida",
        "ru": "Транзакция в очереди",
        "en": "Order payment status is queued"
    }


class PaymeTimeoutException(Exception):
    """
    Payme timeout exception that means that payme is working slowly.
    """