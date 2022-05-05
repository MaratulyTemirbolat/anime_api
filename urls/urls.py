"""Main urls for anime api."""
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

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
    path(
        settings.ADMIN_SITE_URL,
        admin.site.urls
    ),
    path(
        'api/v1/',
        include(router.urls)
    ),
    path(
        'api/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
    path(
        'api/token/verify/',
        TokenVerifyView.as_view(),
        name='token_verify'
    ),
] + static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
print(router.urls)
if settings.DEBUG:
    urlpatterns += [
        path('__debug__/', include('debug_toolbar.urls')),
    ]
