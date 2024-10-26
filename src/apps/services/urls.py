from django.urls import path

from apps.services import views


urlpatterns = [
    path('list/', views.ServiceListAPIView.as_view(), name='service-list'),
    path('create/', views.ServiceCreateAPIView.as_view(), name='service-create'),
]