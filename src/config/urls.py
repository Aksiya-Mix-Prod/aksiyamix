from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    #Django
    path('admin/', admin.site.urls),

    # debug toolbar
    path('__debug__/', include('debug_toolbar.urls')),
]


urlpatterns += [
    # category
    path('api/v1/categories/', include('apps.categories.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
