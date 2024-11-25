from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.likes.views.likes import DiscountReactionViewSet

router = DefaultRouter()
router.register(r'reactions', DiscountReactionViewSet, basename='discount-reactions')

urlpatterns = [
    path('', include(router.urls)),
]
