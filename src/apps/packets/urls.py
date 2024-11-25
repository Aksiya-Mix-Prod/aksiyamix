from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.packets.views.packets import PacketGenericViewSet

router = DefaultRouter()
router.register(r'', PacketGenericViewSet, basename='packets')

urlpatterns = [
    path('', include(router.urls)),
]