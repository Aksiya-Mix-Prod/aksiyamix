from django.core.cache import cache
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

from apps.base import serializers
from apps.base.exceptions import CustomExceptionError
from apps.authentication.utils import generate_jwt_tokens
from apps.users.utils.sms_providers import EskizUz
from apps.users.validators import phone_validate


class SendCodeSerializer(serializers.CustomSerializer):
    username = serializers.CharField(validators=[phone_validate])

    def validate_username(self, phone_number):
        if get_user_model().objects.filter(phone_number=phone_number).exists():
            raise CustomExceptionError(code=400, detail="User with this phone number already exists.")
        return phone_number

    def save(self, *args, **kwargs):
        """
        Send registration code to phone number user.
        """
        # ForgotPasswordSerializer.check_limit(self.context['request'])

        code = EskizUz.send_sms(
            send_type='AUTH_CODE',
            phone_number=self.validated_data['username'],
            )

        self.validated_data['code'] = code


class VerifyCodeSerializer(serializers.CustomSerializer):
    username = serializers.CharField(validators=[phone_validate])
    code = serializers.IntegerField()

    def validate(self, attrs):
        attrs = super().validate(attrs)
        phone_number, code = attrs['username'], attrs['code']

        if cache.get(EskizUz.AUTH_CODE_KEY.format(phone_number=phone_number)) != code:
            raise CustomExceptionError(code=404, detail='Неверный номер телефона или код')

        return attrs
    

class RegisterSerializer(VerifyCodeSerializer):
    password = serializers.CharField(max_length=128, validators=[validate_password], write_only=True)
    refresh = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        phone_number, password = attrs['username'], attrs['password']

        user = get_user_model().objects.create_user(phone_number=phone_number, password=password)

        cache.delete(EskizUz.AUTH_CODE_KEY.format(phone_number=phone_number))

        tokens = generate_jwt_tokens(user)

        attrs = {**attrs, **tokens}

        return attrs