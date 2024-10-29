from django.urls import path

from .views import CheckUsernameViewSet
from .views.company import (CompanyListViewSet, CompanyRetrieveViewSet, CompanyCreateViewSet, CompanyUpdateViewSet,
                            CompanyDeleteViewSet)


urlpatterns = [
    path('check-username/', CheckUsernameViewSet.as_view({'get': 'list'}), name='check-username'),
    # =================   URLS OF COMPANY   =================
    path('company-list', CompanyListViewSet.as_view({'get': 'list'}), name='company-list'),
    path('company-retrieve/<int:pk>/', CompanyRetrieveViewSet.as_view({'get': 'retrieve'}), name='company-retrieve'),
    path('company-create', CompanyCreateViewSet.as_view({'post': 'create'}), name='company-create'),
    path('company-update/<int:pk>/', CompanyUpdateViewSet.as_view({'patch': 'partial_update'}), name='company-update'),
    path('company-delete/<int:pk>/', CompanyDeleteViewSet.as_view({'delete': 'delete'}), name='company-delete'),
]
