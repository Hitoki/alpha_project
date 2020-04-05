from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('music/', include('music.urls')),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + urlpatterns

