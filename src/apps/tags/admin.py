from django.contrib import admin

from apps.tags.models import Tag


@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'created_at']
    list_display_links = list_display
    list_filter = ['created_at']
    search_fields = ['name']


