from django.urls import path

from .views.branches import (BranchCreateViewSet, BranchDeleteViewSet,
                             BranchDetailViewSet, BranchListViewSet,
                             BranchUpdateViewSet)

urlpatterns = [
    # =================   URLS OF BRANCH COMPANY   =================
    path('branch-list', BranchListViewSet.as_view({'get': 'list'}),
         name='branch-list'),
    path('branch-retrieve/<int:id_branch>/', BranchDetailViewSet.as_view({'get': 'retrieve'}),
         name='branch-retrieve'),
    path('branch-create', BranchCreateViewSet.as_view({'post': 'create'}),
         name='branch-create'),
    path('branch-update/<int:id_branch>/', BranchUpdateViewSet.as_view({'patch': 'partial_update'}),
         name='branch-update'),
    path('branch-delete/<int:id_branch>/', BranchDeleteViewSet.as_view({'delete': 'destroy'}),
         name='branch-delete'),
]
