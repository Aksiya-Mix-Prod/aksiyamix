from django.contrib import admin

from .models.category import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'parent', 'created_at')
    list_display_links = ('id', 'name')
    list_filter = ('name', 'slug', 'parent')
    prepopulated_fields = {'slug': ('name',)}



