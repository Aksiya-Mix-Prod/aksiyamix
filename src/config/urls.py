from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

from .yasg import schema_view

urlpatterns = [
    # ========== Django ==========
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),

    # ========= Swagger ===========
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # ========= auth =========
    path('api/v1/auth/', include('apps.authentication.urls')),

    # ========= user =========
    path('api/v1/users/', include('apps.users.urls')),

]
urlpatterns += [
    # ========= categories ================
    path('api/v1/categories/', include('apps.categories.urls')),

    # ========= ratings ================
    path('api/v1/ratings/', include('apps.ratings.urls')),

    # ========= appeals ================
    path('api/v1/appeals/', include('apps.appeals.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)