from django.contrib import admin

from .models.rating import Rating


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'user', 'rating_value')
    list_display_links = ('id', 'company')
    list_filter = ('company', 'user', 'rating_value')

