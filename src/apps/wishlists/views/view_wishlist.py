from rest_framework.permissions import IsAuthenticated

from apps.base.views import CustomListAPIView
from apps.wishlists.serializers import WishListSerializer
from apps.wishlists.models.wishlist import Wishlist


class WishListAPIView(CustomListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WishListSerializer
    queryset = Wishlist.objects.all()
    
    def get_queryset(self):
        return Wishlist.objects.filter(user=self.request.user).select_related('discount').prefetch_related('discount__images', 'discount__discount_features')