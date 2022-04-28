from typing import (
    Tuple,
    Optional,
)

from django.core.handlers.wsgi import WSGIRequest
from django.contrib import admin

from anime.models import (
    Description,
    Title,
    ReleaseDate,
    Anime,
    Genre,
)


@admin.register(ReleaseDate)
class ReleaseDateAdmin(admin.ModelAdmin):  # noqa

    readonly_fields: Tuple[str] = (
        'published',
        'date',
    )


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):  # noqa

    readonly_fields: Tuple[str] = ()


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):  # noqa

    readonly_fields: Tuple[str] = ()


@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):  # noqa

    readonly_fields: Tuple[str] = (
        'datetime_created',
        'datetime_updated',
        'datetime_deleted',
    )
    list_display: Tuple[str] = (
        'studio', 'rating', 'release_date',
        'title', 'description',
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):  # noqa

    readonly_fields: Tuple[str] = ()
