from django.contrib import admin

from .models.notifications import Notification

admin.site.register(Notification)
