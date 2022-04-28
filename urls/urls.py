from django.contrib import admin
from django.urls import (
    path,
    include,
)
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

from auths.views import CustomUserViewSet
from anime.views import AnimeViewSet

# ---------------------------------------------
# API Endpoints
#
router: DefaultRouter = DefaultRouter(
    trailing_slash=False
)
router.register('auths', CustomUserViewSet)
router.register('anime', AnimeViewSet)

urlpatterns = [
    path(settings.ADMIN_SITE_URL, admin.site.urls),
    path(
        'api/v1/',
        include(router.urls)
    ),
] + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
