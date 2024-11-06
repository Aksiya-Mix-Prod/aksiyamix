import base64
import binascii
from django.conf import settings
from rest_framework.permissions import BasePermission
from apps.payments.exceptions import PermissionDenied



class PaymeAuthPermission(BasePermission):

    def has_permission(self, request, view):
        is_payme = False
        password = request.META.get('HTTP_AUTHORIZATION')
        if not isinstance(password, str):
            error_message = "Request from an unauthorized source!"
            raise PermissionDenied(error_message=error_message)

        password = password.split()[-1]

        try:
            password = base64.b64decode(password).decode('utf-8')
        except (binascii.Error, UnicodeDecodeError) as error:
            error_message = "Error when authorize request to merchant!"

            raise PermissionDenied(error_message=error_message) from error

        merchant_key = password.split(':')[-1]

        if merchant_key == settings.PAYME_PASSWORD:
            is_payme = True

        if merchant_key != settings.PAYME_PASSWORD:
            pass

        print(merchant_key)
        print(settings.PAYME_PASSWORD)
        print(is_payme)
        if is_payme is False:
            raise PermissionDenied(
                error_message="Unavailable data for unauthorized users!"
            )

        return True
