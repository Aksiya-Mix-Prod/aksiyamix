from django.contrib import admin

from apps.tags.models import Tag


@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'is_active', 'created_at']
    list_display_links = ['id', 'name', 'created_at']
    list_filter = ['is_active', 'created_at']
    list_editable = ['is_active']
    search_fields = ['name']


