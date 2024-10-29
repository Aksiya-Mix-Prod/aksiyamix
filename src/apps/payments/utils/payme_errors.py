from rest_framework import status
from rest_framework.response import Response


class PaymeErrorResponse:
    """
    Helper class to format the responses from Payme
    """
    ERRORS = {
        'transaction_not_found': {"code": -31003, "message": {"uz": "Transaction not found", "ru": "Транзакция не найдена", "en": "Transaction not found"}},
        'invalid_amount': {"code": -31001, "message": {"uz": "Invalid amount", "ru": "Неверная сумма", "en": "Invalid amount"}},
        'unable_to_perform': {"code": -31008, "message": {"uz": "Unable to perform operation", "ru": "Невозможно выполнить операцию", "en": "Unable to perform operation"}},
        'order_not_found': {"code": -31050, "message": {"uz": "Order not found", "ru": "Заказ не найден", "en": "Order not found"}},
        'order_already_paid': {"code": -31051, "message": {"uz": "Order already paid", "ru": "Заказ уже оплачен", "en": "Order already paid"}},
        'incorrect_amount': {"code": -31052, "message": {"uz": "Incorrect amount", "ru": "Неверная сумма", "en": "Incorrect amount"}},
    }

    def get_error_response(self, error_code, request_id):
        """Helper method to format the error responses."""
        return Response({
            "error": self.ERRORS.get(error_code, self.ERRORS['unable_to_perform']),
            "request_id": request_id
        }, status=status.HTTP_200_OK)

    def get_success_response(self, result, request_id):
        """Helper method to format the success responses."""
        return Response({
            "success": result,
            "request_id": request_id
        }, status=status.HTTP_200_OK)