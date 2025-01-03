from django.urls import path 

from apps.tops import views


urlpatterns = [
    path('tariffs/list/', views.TopTariffListAPIView.as_view(),  name='top_tariff_list'),
    path('tariffs/buy/', views.BuyTopTariffGenericAPIView.as_view(), name='buy_top_tariff'),
    path('list/', views.TopListAPIView.as_view(), name='top_list'),
    path('create/', views.CreateTopDiscountAPIView.as_view(), name='create_top_discount'),
]