from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.cache import cache
from django.db.models import Q
from rest_framework import serializers

from apps.authentication.services.username_type import check_username_type
from apps.authentication.utils import generate_jwt_tokens
from apps.base.exceptions import CustomExceptionError
from apps.base.serializers import CustomSerializer
from apps.users.utils.sms_providers import EskizUz


class SendCodeSerializer(CustomSerializer):
    username = serializers.CharField()

    def validate_username(self, username):
        #validation username
        username_type = check_username_type(username)

        # checking username unique
        user = get_user_model().objects.filter(Q(phone_number=username) | Q(email=username))
        if user.exists():
            raise CustomExceptionError(code=400, detail=f"User with this {username_type} already exists.")

        return username

    def save(self, *args, **kwargs):
        """
        Send registration code to phone number user.
        """
        username_type = check_username_type(self.validated_data['username'])

        send_type = 'AUTH_CODE' if username_type == 'phone_number' else 'AUTH_CODE_EMAIL'

        # ForgotPasswordSerializer.check_limit(self.context['request'])

        code = EskizUz.send_sms(
            send_type=send_type,
            username=self.validated_data['username'],
            )

        self.validated_data['code'] = code


class VerifyCodeSerializer(CustomSerializer):
    username = serializers.CharField()
    code = serializers.IntegerField()

    def validate(self, attrs):
        attrs = super().validate(attrs)
        username, code = attrs['username'], attrs['code']

        if cache.get(EskizUz.AUTH_CODE_KEY.format(username=username)) != code:
            raise CustomExceptionError(code=404, detail='Invalid verify code or username')

        return attrs
    

class RegisterSerializer(VerifyCodeSerializer):
    fullname = serializers.CharField(max_length=128)
    password = serializers.CharField(max_length=128, validators=[validate_password], write_only=True)
    refresh = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)

        username, password, fullname = attrs['username'], attrs['password'], attrs['fullname']
        username_type = check_username_type(username)

        if username_type == 'phone_number':
            user = get_user_model().objects.create_user(username=username, fullname=fullname, phone_number=username, password=password)
        
        else:
            user = get_user_model().objects.create_user(username=username, fullname=fullname, email=username, password=password)

        cache.delete(EskizUz.AUTH_CODE_KEY.format(username=username))

        tokens = generate_jwt_tokens(user)

        attrs = {**attrs, **tokens}

        return attrs