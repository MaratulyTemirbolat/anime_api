from rest_framework.routers import DefaultRouter

from django.urls import (
    path,
    include,
)

from auths.views import CustomUserViewSet

# ---------------------------------------------
# API Endpoints
#
router: DefaultRouter = DefaultRouter(
    trailing_slash=False
)
router.register('auths', CustomUserViewSet)

app_name = 'router'

urlpatterns = [
    path(
        'api/v1/',
        include((router.urls, app_name), namespace='v1')
    )
]
