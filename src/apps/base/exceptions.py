from rest_framework.exceptions import APIException, _get_error_details

from django.forms.utils import ErrorDict, ErrorList
from django.core.exceptions import ValidationError


class CustomAPIExceptionError(APIException):
    default_detail = 'Error'
    default_code = 400

    def __init__(self, code: int = None, detail: str | dict | list | tuple = None) -> None:
        if detail is None:
            detail = self.default_detail
        if code is None:
            code = self.default_code

        if isinstance(detail, tuple):
            detail = list(detail)
        elif not isinstance(detail, dict) and not isinstance(detail, list):
            detail = [detail]

        self.detail = _get_error_details(detail, code)


class CustomExceptionError(ValidationError):
    def __init__(self, code: int = None, detail: str | dict = None) -> None:
        """
        Универсальное исключение для работы с моделями, формами и админкой Django.
        detail может быть строкой (общая ошибка) или словарем (ошибки по полям).
        """
        if isinstance(detail, str):
            detail = {'__all__': [detail]}  # Общая ошибка
        elif isinstance(detail, dict):
            # Убедимся, что значения словаря — это списки ошибок
            detail = {
                key: value if isinstance(value, list) else [value]
                for key, value in detail.items()
            }
        else:
            raise ValueError("Detail must be a string or a dictionary.")

        error_dict = ErrorDict({
            key: ErrorList(value)
            for key, value in detail.items()
        })
        super().__init__(error_dict)

    def __str__(self):
        return f"CustomExceptionError: {self.message_dict}"