from apps.wishlists.views import WishlistCreateAPIView
from django.urls import path

urlpatterns = [
    path('create/', WishlistCreateAPIView.as_view(), name="wishlist_create"),
]
