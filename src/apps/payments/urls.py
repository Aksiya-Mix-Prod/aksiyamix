from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.payments.views import PaymeGenericViewSet, PaymeInitGenericViewSet


router = DefaultRouter()
router.register('payme', PaymeGenericViewSet, basename='payme')
router.register('payme/initialize', PaymeInitGenericViewSet, basename='initialize')

urlpatterns = [
    path('', include(router.urls))
]
