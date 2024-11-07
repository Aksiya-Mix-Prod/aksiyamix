# from django.utils import timezone

# from apps.base.views import CustomListAPIView
# from apps.tops.models import TopDiscount


# class TopListAPIView(CustomListAPIView):
#     queryset = TopDiscount.objects.all()
#     serializer_class = DiscountListSerializer
    
#     def get_queryset(self):
#         queryset = []
#         tops = super().get_queryset()
#         for_count = 0
#         for obj in tops:
#             if for_count == 3:
#                 break
#             for date in obj.dates:
#                 if date == timezone.now().date():
#                     for_count += 1
#                     queryset.append(obj.discount)
#         return queryset
