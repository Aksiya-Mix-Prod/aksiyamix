from django.urls import path

from .views.notifications import NotificationViewSet

urlpatterns = [
    path(
        "register-device/",
        NotificationViewSet.as_view({"post": "create"}),
        name="notification-list",
    ),
]
