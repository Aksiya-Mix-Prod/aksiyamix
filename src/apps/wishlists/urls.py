from django.urls import path

from apps.wishlists.views import WishlistCreateAPIView

urlpatterns = [
    path('create/', WishlistCreateAPIView.as_view(), name='wishlist_create'),
]