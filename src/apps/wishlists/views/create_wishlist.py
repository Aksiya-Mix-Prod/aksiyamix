from django.shortcuts import get_object_or_404

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.base.serializers import EmptySerializer
from apps.base.validators import validate_uuid
from apps.base.views import CustomGenericAPIView
from apps.discounts.models.discount import Discount
from apps.wishlists.models import Wishlist


class WishlistCreateAPIView(CustomGenericAPIView):
    permission_classes = [IsAuthenticated]
    queryset = []
    serializer_class = EmptySerializer
    
    def get(self, request, discount_id):
        validate_uuid(discount_id)
        discount = get_object_or_404(Discount, id=discount_id)
        wishlist, create = Wishlist.objects.get_or_create(
            user=request.user, discount=discount
        )
        if not create:
            wishlist.delete()
        return Response({"success": create}, status=200)