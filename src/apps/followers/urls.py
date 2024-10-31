from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.followers.views import FollowerViewSet

router = DefaultRouter()
router.register(r'followers', FollowerViewSet)

urlpatterns = [
    path('', include(router.urls))
]
