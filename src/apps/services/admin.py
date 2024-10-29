from django.contrib import admin

from apps.services.models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'is_active')
    list_display_links = ('id', 'name')
    list_editable = ('is_active',)
    list_filter = list_editable
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}