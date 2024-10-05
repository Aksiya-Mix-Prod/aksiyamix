from django.urls import path

from apps.users import views


urlpatterns = [
    # ========== Forgot Password ========== #
    path('forgot_password/', views.ForgotPasswordAPIView.as_view(), name='forgot_password'),
    path('forgot_password/confirm/', views.NewPasswordAPIView.as_view(), name='new_password'),
]