from rest_framework.permissions import BasePermission
from rest_framework.request import Request as DRF_Request


class AnimePermission(BasePermission):
    """Determines permission for Anime."""

    SAFE_METHODS = (
        'list', 'retrieve',
    )
    USER_METHODS = SAFE_METHODS + (
        'create', 'partial_update', 'update',
    )
    ADMIN_METHODS = (
        'destroy',
    )

    def __init__(self) -> None:
        """Set initial values to fields."""
        self._admin_access: bool = False
        self._user_access: bool = False
        self._DENIED_ACCESS: bool = False

    def _initialize_permissions(self, request: DRF_Request) -> None:
        """Initialize base permissions."""
        self._user_access = (
            request.user and request.user.is_active
        )
        self._admin_access = self._user_access and (
            request.user.is_staff and
            request.user.is_superuser
        )

    def has_permission(
        self,
        request: DRF_Request,
        view
    ) -> bool:
        """Permissions for AnimeViewSet."""
        self._initialize_permissions(
            request
        )
        if view.action in self.USER_METHODS:
            return self._user_access
        if view.action in self.ADMIN_METHODS:
            return self._admin_access
        return self._DENIED_ACCESS
