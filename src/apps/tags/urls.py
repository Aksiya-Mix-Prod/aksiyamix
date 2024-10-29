from django.urls import path

from apps.tags import views


urlpatterns = [
    path('filter/', views.SearchTagsGenericAPIView.as_view() , name='filter_tags'),
    path('create/', views.TagsCreateAPIView.as_view() , name='create_tags'),
]