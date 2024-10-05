from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .yasg import schema_view


urlpatterns = [
    # Django
    path('admin/', admin.site.urls),

    # Swagger
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
