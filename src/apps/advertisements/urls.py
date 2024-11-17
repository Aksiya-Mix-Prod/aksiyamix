from django.urls import path

from .views.advertisement import AdvertisementViewSet


urlpatterns = [
    path('/', AdvertisementViewSet.as_view()),
]