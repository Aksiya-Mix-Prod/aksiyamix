from django.urls import path

from apps.services import views


urlpatterns = [
    path('list/', views.ServiceListAPIView.as_view(), name='service-list'),
]