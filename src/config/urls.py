from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

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
    # ========= tags =========
    path('api/v1/tags/', include('apps.tags.urls')),
    # ========= services =========
    path('api/v1/services/', include('apps.services.urls')),
    # ========= wishlists =========
    path('api/v1/wishlists/', include('apps.wishlists.urls')),
    # ========= tops =========
    path('api/v1/tops/', include('apps.tops.urls')),
    # ========= notifications =========
    # path('api/v1/notifications/', include('apps.notifications.urls')),


    # ========= Mukhsin's Apps ========
    path('api/v1/comments/', include('apps.comments.urls')),
    path('api/v1/likes/', include('apps.likes.urls')),
    path('api/v1/packages/', include('apps.packets.urls')),
    path('api/v1/payments/', include('apps.payments.urls')),









    # ========= Mukhsin's Apps finish line ========

    # ========= Oybek =========
    path('api/v1/companies/', include('apps.companies.urls')),
    path('api/v1/branches/', include('apps.branches.urls')),
    path('api/v1/followers/', include('apps.followers.urls')),
    path('api/v1/complaints/', include('apps.complaints.urls')),
    path('api/v1/advertisements/', include('apps.advertisements.urls')),
    path('api/v1/notifications/', include('apps.notifications.urls')),
]

urlpatterns += [
    # ========= categories ================
    path('api/v1/categories/', include('apps.categories.urls')),

    # ========= ratings ================
    path('api/v1/ratings/', include('apps.ratings.urls')),

    # ========= appeals ================
    path('api/v1/appeals/', include('apps.appeals.urls')),
]

    # ========== Iskandar ============

urlpatterns += [
    # ========= products ================
    path('api/v1/products/', include('apps.products.urls')),

    # ========= discount ============
    path('api/v1/discounts/', include('apps.discounts.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)