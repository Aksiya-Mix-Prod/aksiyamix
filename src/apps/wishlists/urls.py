from apps.wishlists import views
from django.urls import path

urlpatterns = [
    path("create/<str:discount_id>", views.WishlistCreateAPIView.as_view(), name="wishlist_create"),
    path("list", views.WishListAPIView.as_view(), name="wishlist_list"),
]
