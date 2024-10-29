from django.urls import path

from apps.ratings.views.ratings import RatingCreateViewSet


urlpatterns = [
    path('create/', RatingCreateViewSet.as_view({'post': 'create'}), name="rating-create"),
]

