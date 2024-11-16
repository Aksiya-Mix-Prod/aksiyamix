from django.contrib import admin

from .models.appeal import Appeal


@admin.register(Appeal)
class AppealAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'company', 'phone_number', 'subject')
    list_display_links = ('id', 'user')
    list_filter = ('user', 'company', 'phone_number', 'subject')



