from django.contrib import admin

from apps.tops.models import TopTariff


@admin.register(TopTariff)
class TopTariffAdmin(admin.ModelAdmin):
    list_display = ('id', 'quantity', 'price')
    list_display_links = list_display
    search_fields = ('quantity', 'price')