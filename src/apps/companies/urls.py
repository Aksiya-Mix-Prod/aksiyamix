from django.urls import path

from .views.company import (CompanyListViewSet, CompanyRetrieveViewSet, CompanyCreateViewSet, CompanyUpdateViewSet,
                            CompanyDeleteViewSet)


urlpatterns = [
    # =================   URLS OF COMPANY   =================
    path('company-list', CompanyListViewSet.as_view, name='company-list'),
    path('company-retrieve/<int:pk>/', CompanyRetrieveViewSet.as_view, name='company-retrieve'),
    path('company-create', CompanyCreateViewSet.as_view, name='company-create'),
    path('company-update/<int:pk>/', CompanyUpdateViewSet.as_view, name='company-update'),
    path('company-delete/<int:pk>/', CompanyDeleteViewSet.as_view, name='company-delete'),
]
