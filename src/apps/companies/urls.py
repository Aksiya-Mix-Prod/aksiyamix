from django.urls import path

from .views import CheckUsernameViewSet
from .views.company import (
    CompanyCreateViewSet,
    CompanyDeleteViewSet,
    CompanyListViewSet,
    CompanyRetrieveViewSet,
    CompanyUpdateViewSet,
)
from .views.company_time_table import (
    CompanyTimeTableCreateViewSet,
    CompanyTimeTableDeleteViewSet,
    CompanyTimeTableListViewSet,
    CompanyTimeTableRetrieveViewSet,
    CompanyTimeTableUpdateViewSet,
)
from .views.ratings import CompanyRatingViewSet

urlpatterns = [
    # =================   URLS OF USERNAME COMPANY =================
    path(
        "check-username/",
        CheckUsernameViewSet.as_view({"get": "list"}),
        name="check-username",
    ),
    # =================   URLS OF COMPANY   =================
    path(
        "company-list", CompanyListViewSet.as_view({"get": "list"}), name="company-list"
    ),
    path(
        "company-retrieve/<int:pk>/",
        CompanyRetrieveViewSet.as_view({"get": "retrieve"}),
        name="company-retrieve",
    ),
    path(
        "company-create",
        CompanyCreateViewSet.as_view({"post": "create"}),
        name="company-create",
    ),
    path(
        "company-update/<int:pk>/",
        CompanyUpdateViewSet.as_view({"patch": "partial_update"}),
        name="company-update",
    ),
    path(
        "company-delete/<int:pk>/",
        CompanyDeleteViewSet.as_view({"delete": "delete"}),
        name="company-delete",
    ),
    # =================     URLS OF COMPANY TIMETABLE   =================
    path(
        "company-time-table-list/",
        CompanyTimeTableListViewSet.as_view({"get": "list"}),
        name="company-time-table-list",
    ),
    path(
        "company-time-table-retrieve/<int:pk>/",
        CompanyTimeTableRetrieveViewSet.as_view({"get": "retrieve"}),
        name="company-time-table-retrieve",
    ),
    path(
        "company-time-table-create/",
        CompanyTimeTableCreateViewSet.as_view({"post": "create"}),
        name="company-time-table-create",
    ),
    path(
        "company-time-table-update/<int:pk>/",
        CompanyTimeTableUpdateViewSet.as_view({"patch": "partial_update"}),
        name="company-time-table-update",
    ),
    path(
        "company-time-table-delete/<int:pk>/",
        CompanyTimeTableDeleteViewSet.as_view({"delete": "destroy"}),
        name="company-time-table-delete",
    ),
    # =================     URLS OF RATING COMPANY      =================
    path(
        "company-rating/<int:pk>/",
        CompanyRatingViewSet.as_view({"post": "create_rating"}),
        name="company-rating",
    ),
    path(
        "company-rating-update/<int:pk>/",
        CompanyRatingViewSet.as_view({"patch": "update_rating"}),
        name="company-rating-update",
    ),
    path(
        "company-rating-retrieve",
        CompanyRatingViewSet.as_view({"get": "retrieve"}),
        name="company-rating-retrieve",
    ),
]
