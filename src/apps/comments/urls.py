from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.comments.views import DiscountCommentViewSet

router = DefaultRouter()
router.register(r'', DiscountCommentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
]