from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

from apps.discounts.models import Discount
from apps.likes.models.likes import DiscountLike
from apps.likes.models.dislikes import DiscountDislike
from apps.base.views.viewsets import CustomGenericViewSet
from apps.likes.serializers.likes import DiscountLikeSerializer
from apps.likes.serializers.dislikes import DiscountDislikeSerializer
from apps.likes.permissions.permissions import IsAdminOrLikeOrDislikeOwner
from apps.likes.serializers.stats import DiscountLikesDislikesStatisticsSerializer



class DiscountReactionViewSet(CustomGenericViewSet):
    """
    ViewSet for handling discount likes and dislikes.
    """
    permission_classes = [IsAdminOrLikeOrDislikeOwner]
    serializer_class = DiscountLikeSerializer

    def get_queryset(self):
        """
        Filter queryset based on the action being performed.
        """
        if self.action in ['like', 'list_likes']:
            return DiscountLike.objects.filter(user=self.request.user)
        elif self.action in ['dislike', 'list_dislikes']:
            return DiscountDislike.objects.filter(user=self.request.user)
        return DiscountLike.objects.none()

    @action(detail=True, methods=['post'], url_path='like')
    def like(self, request, pk=None) -> Response:
        """
        Like a discount.
        If the discount was previously disliked, remove the dislike.
        """
        discount = get_object_or_404(Discount, pk=pk)

        # ========= Remove any existing dislike =========
        DiscountLike.objects.filter(user=request.user, discount=discount).delete()

        like, created = DiscountLike.objects.get_or_create(
            user=request.user,
            discount=discount,
        )

        if not created:
            like.delete()
            return Response({"message": "Like removed 😞"}, status=status.HTTP_201_CREATED)


    @action(detail=True, methods=['post'], url_path='dislike')
    def dislike(self, request, pk=None) -> Response:
        """
        Dislike a discount.
        If the discount was previously liked, remove the like.
        """
        discount = get_object_or_404(Discount, pk=pk)

        # ========= Remove any existing like ========
        DiscountDislike.objects.filter(user=self.request.user, discount=discount).delete()

        # ========= Toggle dislike ========
        dislike, created = DiscountDislike.objects.get_or_create(
            user=request.user,
            discount=discount
        )

        if not created:
            dislike.delete()
            return Response({"message": "Dislike removed"}, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['get'], url_path='stats')
    def stats(self, request, pk=None) -> Response:
        """
        Get like/dislike statistics for a discount.
        """
        discount = get_object_or_404(Discount, pk=pk)

        stats = {
            'total_likes': discount.like_counts,
            'total_dislikes': discount.dislike_counts,
            'user_has_liked': discount.objects.filter(
                user=request.user,
                discount=discount
            ).exists() if request.user.is_authenticated else False,
        }

        serializer = DiscountLikesDislikesStatisticsSerializer(data=stats)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='user-likes')
    def list_likes(self, request) -> Response:
        """
        List all discounts liked by the current user.
        """
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='user-dislikes')
    def list_dislikes(self, request) -> Response:
        """
        List all discounts disliked by the current user.
        """
        queryset = DiscountDislike.objects.filter(user=request.user)
        serializer = DiscountDislikeSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


