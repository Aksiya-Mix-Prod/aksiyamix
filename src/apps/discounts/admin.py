from django.contrib import admin

from src.apps.discounts.models.servicediscount import ServiceDiscount

@admin.register(ServiceDiscount)
class ServiceDiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'is_active')
    list_display_links = ('name', 'slug', 'is_active')

    prepopulated_fields = {'slug': ('name',)}

    search_fields = ('name', 'slug')

    ordering = ('name',)

    readonly_fields = ('slug',)
