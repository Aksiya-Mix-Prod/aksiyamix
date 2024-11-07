from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.base.exceptions import CustomExceptionError
from apps.base.validators import validate_uuid
from apps.base.views import CustomAPIView
from apps.discounts.models.discount import Discount
from apps.wishlists.models import Wishlist


class WishlistCreateAPIView(CustomAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if not request.GET.get('discount_id'):
            raise CustomExceptionError(code=400, detail={'discount_id': 'discount_id is required'})
        validate_uuid(request.GET.get('discount_id'))
        discount = get_object_or_404(Discount, id=request.GET.get('discount_id'))
        create, wishlist = Wishlist.objects.get_or_create(user=request.user, discount=discount)
        return Response({'success': create})