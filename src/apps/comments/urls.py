from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.comments.views import CommentViewSet, CommentReplyViewSet

router = DefaultRouter()
router.register(r'comments', CommentViewSet, basename='comments')
router.register(r'comment/replies', CommentReplyViewSet, basename='reply')

urlpatterns = [
    path('', include(router.urls)),
]
