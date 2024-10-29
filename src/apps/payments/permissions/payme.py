from base64 import b64decode
from django.conf import settings
from rest_framework.permissions import BasePermission



class PaymePermission(BasePermission):
    """
    Custom permission class for Payme merchant API authentication
    """
    def has_permission(self, request, view):
        auth_header = request.META.get('HTTP_AUTHORIZATION', '')
        if not auth_header.startswith('Basic '):
            return False

        try:
            auth_decoded = b64decode(auth_header[6:]).decode('utf-8')
            username, password = auth_decoded.split(':')
            return username == settings.PAYME_USERNAME and password == settings.PAYME_PASSWORD
        except:
            return False

