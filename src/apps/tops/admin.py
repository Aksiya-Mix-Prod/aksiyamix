from django.contrib import admin

from apps.tops.models import TopTariff, TopDiscount, CompanyTopTariff


@admin.register(TopTariff)
class TopTariffAdmin(admin.ModelAdmin):
    list_display = ('id', 'quantity', 'price')
    list_display_links = list_display
    search_fields = ('quantity', 'price')
    

@admin.register(TopDiscount)
class TopDiscountAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = list_display
    

@admin.register(CompanyTopTariff)
class CompanyTopTariffAdmin(admin.ModelAdmin):
    list_display = ('id', 'quantity', 'price',)
    list_display_links = list_display