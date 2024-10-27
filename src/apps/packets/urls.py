from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.packets.views.packets import PacketViewSet

router = DefaultRouter()
router.register(r'', PacketViewSet, basename='packets')

urlpatterns = [
    path('', include(router.urls)),
]