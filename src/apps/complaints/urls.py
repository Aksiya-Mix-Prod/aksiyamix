from django.urls import path

from .views.complaint import ComplaintViewSet


urlpatterns = [
    path('complaints/', ComplaintViewSet.as_view({'get': 'list', 'post': 'create'}),
         name='complaints'), # List and create complaints
    path('complaints/<int:pk>/', ComplaintViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                           'patch': 'partial_update', 'delete': 'destroy'}),
         name='complaint-detail') # Retrieve, update, and delete a specific complaint
]