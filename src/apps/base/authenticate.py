from rest_framework import serializers
from rest_framework.response import Response

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.authentication.utils.services import generate_jwt_tokens
from apps.base.exceptions import CustomExceptionError
from apps.base.views import CustomGenericAPIView
from apps.users.models import CustomUser

# User = get_user_model()
User = CustomUser

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username = serializers.CharField()

    class Meta:
        model = User
        fields = ('username', 'password')

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        try:
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            try:
                user = User.objects.get(phone_number=username)
            except User.DoesNotExist:
                raise CustomExceptionError(code=404, detail="User not found.")

        if not user.check_password(password):
            raise CustomExceptionError(code=404, detail="User not found.")

        if not user.is_active:
            raise CustomExceptionError(code=403, detail="User is not active")

        tokens = generate_jwt_tokens(user)

        return tokens
    

class CustomTokenObtainPairView(CustomGenericAPIView):
    serializer_class = CustomTokenObtainPairSerializer
    queryset = []

    def post(self, request, *args, **kwargs):
        serializer = CustomTokenObtainPairSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=200)
        return Response(serializer.errors, status=400)
