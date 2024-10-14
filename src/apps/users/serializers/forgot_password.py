from django.core.cache import cache
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers

from apps.base.serializers import CustomSerializer
from apps.base.exceptions import CustomExceptionError
from apps.authentication.utils import generate_jwt_tokens
from apps.users.utils import EskizUz
from apps.authentication.services import check_username_type


class ForgotPasswordSerializer(serializers.CustomSerializer):
    username = serializers.CharField()
    link = serializers.CharField(read_only=True)

    def validate_username(self, username):
        #======== checking username type ========
        username_type = check_username_type(username)

        #======== checking user exists ========
        if username_type == 'phone_number':
            user = get_user_model().objects.filter(phone_number=username)
        else:
            user = get_user_model().objects.filter(email=username)
        if not user.exists():
            raise CustomExceptionError(code=404, detail="User with this phone number does not exist.")
        
        return username
    
    @classmethod
    def check_limit(cls, request):
        """
        Checking limit for ip address
        """
        ip_address = request.META.get('REMOTE_ADDR')

        limit = cache.get(ip_address, 0)
        if limit >= 3:
            raise CustomExceptionError(code=403, detail='Try after one hour')
        else:
            cache.set(ip_address, limit + 1, 60 * 60)

    def save(self, *args, **kwargs):
        """
        Send forgot password link to phone number or email user. 
        """
        username_type = check_username_type(username=self.validated_data['username'])

        # self.check_limit(self.context['request'])
        if username_type == 'phone_number':
            user = get_object_or_404(get_user_model(), phone_number=self.validated_data['username'])
        else:
            user = get_object_or_404(get_user_model(), email=self.validated_data['username'])

        token_generator = PasswordResetTokenGenerator()
        token = token_generator.make_token(user)

        reset_url = self.context['request'].build_absolute_uri(f'confirm/?token={token}')

        EskizUz.send_sms(
            send_type='FORGOT_PASSWORD', 
            username=self.validated_data['username'],
            token=token,
            link=reset_url,
            )
        
        self.validated_data['link'] = reset_url


class NewPasswordSerializer(serializers.CustomSerializer):
    password = serializers.CharField(validators=[validate_password], write_only=True)
    
    refresh = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)

    def save(self, **kwargs):
        attrs = self.validated_data
        context = self.context

        token  = context['token']
        username = cache.get(EskizUz.FORGOT_PASSWORD_KEY.format(token=token))
        
        if not username:
            raise CustomExceptionError(code=404, detail='not found')
        
        username_type = check_username_type(username)
        
        if username_type == 'phone_number':
            user = get_object_or_404(get_user_model(), phone_number=username)
        else:
            user = get_object_or_404(get_user_model(), email=username)
        user.set_password(attrs['password'])
        user.save()

        cache.delete(EskizUz.FORGOT_PASSWORD_KEY.format(token=token))

        tokens = generate_jwt_tokens(user)

        self.validated_data['refresh'] = tokens['refresh']
        self.validated_data['access'] = tokens['access']