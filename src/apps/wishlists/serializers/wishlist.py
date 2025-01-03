from apps.base.serializers import CustomModelSerializer
from apps.discounts.serializers.discount import DiscountCreateUpdateSerializer
from apps.wishlists.models.wishlist import Wishlist


class WishListSerializer(CustomModelSerializer):
    discount = DiscountCreateUpdateSerializer(read_only=True)
    
    class Meta:
        model = Wishlist
        fields = ['id', 'user', 'discount']
