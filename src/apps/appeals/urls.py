from django.urls import path
from apps.appeals.views.appeals import AppealCreateViewSet


urlpatterns = [
    path('', AppealCreateViewSet.as_view({'post': 'create'}), name="appeal-create"),
]

