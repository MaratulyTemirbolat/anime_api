"""All views (ViewSets, APIViews) for anime api."""
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response as DRF_Response
from rest_framework.request import Request as DRF_Request

from django.db.models import QuerySet

from abstracts.validators import APIValidator
from abstracts.paginators import (
    AbstractPageNumberPaginator,
    AbstractLimitOffsetPaginator,
)
from anime.models import Anime
from anime.serializers import (
    AnimeSerializer,
)
from anime.permissions import (
    AnimePermission,
)
from abstracts.handlers import DRFResponseHandler


class AnimeViewSet(DRFResponseHandler, ViewSet):
    """ViewSet for Anime."""

    permission_classes: tuple = (
        AnimePermission,
    )
    queryset: QuerySet[Anime] = Anime.objects.get_not_deleted()
    serializer_class: AnimeSerializer = AnimeSerializer
    pagination_class: AbstractPageNumberPaginator = \
        AbstractPageNumberPaginator

    def get_queryset(self) -> QuerySet:  # noqa
        return self.queryset

    @action(
        methods=['get'],
        detail=False,
        url_path='list-2',
        permission_classes=(
            permissions.AllowAny,
        )
    )
    def list_2(self, request: DRF_Request) -> DRF_Response:
        """Handle GET-request to list Anime."""
        paginator: AbstractLimitOffsetPaginator = \
            AbstractLimitOffsetPaginator()

        response: DRF_Response = self.get_drf_response(
            request=request,
            data=self.get_queryset(),
            serializer_class=self.serializer_class,
            many=True,
            paginator=paginator
        )

        # print("---------------BREAKPOINT--------------------")
        # breakpoint()

        # objects: list = paginator.paginate_queryset(
        #     self.get_queryset(),
        #     request
        # )
        # serializer: AnimeSerializer = \
        #     self.serializer_class(
        #         objects,
        #         many=True
        #     )
        # response: DRF_Response = \
        #     paginator.get_paginated_response(
        #         serializer.data
        #     )
        return response

    def list(self, request: DRF_Request) -> DRF_Response:
        """Handle GET-request to list Anime."""
        paginator: AbstractPageNumberPaginator = \
            self.pagination_class()

        objects: list = paginator.paginate_queryset(
            self.get_queryset(),
            request
        )
        serializer: AnimeSerializer = self.serializer_class(
            objects,
            many=True
        )
        response: DRF_Response = \
            paginator.get_paginated_response(
                serializer.data
            )
        return response

    def create(self, request: DRF_Request) -> DRF_Response:
        """Handle POST-request to show custom_users."""
        raise APIValidator(
            "warning",
            '\'POST\' ?????????? ???? ??????????????????????????????',  # ????????????
            '403'
        )

    def retrieve(self, request: DRF_Request, pk: int = 0) -> DRF_Response:
        """Handle GET-request with ID to show custom_user."""
        raise APIValidator(
            "warning",
            '\'GET\' ?????????? ???? ??????????????????????????????',  # ????????????
            '403'
        )

    def partial_update(
        self,
        request: DRF_Request,
        pk: int = 0
    ) -> DRF_Response:
        """Handle PATCH-request with ID to show custom_user."""
        raise APIValidator(
            "warning",
            '\'PATCH\' ?????????? ???? ??????????????????????????????',  # ????????????
            '403'
        )

    def update(
        self,
        request: DRF_Request
    ) -> DRF_Response:
        """Handle PUT-request with ID to show custom_user."""
        raise APIValidator(
            "warning",
            '\'PUT\' ?????????? ???? ??????????????????????????????',  # ????????????
            '403'
        )

    def destroy(
        self,
        request: DRF_Request,
        pk: int = 0
    ) -> DRF_Response:
        """Handle DELETE-request with ID to show custom_user."""
        raise APIValidator(
            "warning",
            '\'DELETE\' ?????????? ???? ??????????????????????????????',  # ????????????
            '403'
        )
