from django.core.cache import cache

from rest_framework.response import Response

from apps.base.views import CustomGenericAPIView, CustomCreateAPIView
from apps.users.serializers import ForgotPasswordSerializer, NewPasswordSerializer
from apps.users.utils import EskizUz


class ForgotPasswordAPIView(CustomCreateAPIView):
    """
    This view is send link to phone number.
    """
    permission_classes = ()
    authentication_classes = ()

    serializer_class = ForgotPasswordSerializer


class NewPasswordAPIView(CustomGenericAPIView):
    """
    This view is set new password to user.
    """
    queryset = []

    permission_classes = ()
    authentication_classes = ()

    serializer_class = NewPasswordSerializer

    def get(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        token_in_cache = cache.get(EskizUz.FORGOT_PASSWORD_KEY.format(token=token))
        if not token_in_cache:
            return Response({'error': 'request not found'}, status=404)
        return Response(status=200)

    def post(self, request, *args, **kwargs):
        token = request.query_params.get('token')
        serializer = self.get_serializer(data=request.data, 
                                         context={'token':token,})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=200)