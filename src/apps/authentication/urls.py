from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView
from apps.base.utils.authenticate import CustomTokenObtainPairView

from apps.authentication import views


urlpatterns = [
    # ========== Jwt Authentication ========== #
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # ========== Register ========== #
    path('register/send_code/', views.SendCodeAPIView.as_view(), name='send_code'),
    path('register/verify_code/', views.VerifyCodeAPIView.as_view(), name='verify_code'),
    path('register/', views.RegisterAPIView.as_view(), name='register'),
]