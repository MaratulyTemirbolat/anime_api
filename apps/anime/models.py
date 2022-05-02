"""Models (tables) for anime api."""
from typing import (
    Tuple,
)
from datetime import datetime

from django.db import models
from django.db.models import QuerySet

from abstracts.models import AbstractDateTime


class Description(models.Model):
    """Description entity."""

    text_en = models.TextField(
        verbose_name="Описание (Англ)",
        default=""
    )
    text_ru = models.TextField(
        verbose_name="Описание (Рус)",
        default=""
    )

    class Meta:  # noqa
        ordering: Tuple[str] = (
            'id',
        )
        verbose_name: str = 'Описание'
        verbose_name_plural: str = 'Описания'

    def __str__(self) -> str:  # noqa
        return f'Описание тайтла: {self.text_en[:50]}...'


class Title(models.Model):
    """Title entity."""

    name = models.CharField(
        verbose_name="Имя",
        max_length=50
    )
    link = models.TextField(
        verbose_name="Ссылка"
    )

    class Meta:  # noqa
        ordering: Tuple[str] = (
            'id',
        )
        verbose_name: str = 'Наименование'
        verbose_name_plural: str = 'Наименования'


class ReleaseDate(models.Model):
    """Release date entity."""

    published = models.CharField(
        verbose_name="Выпущен",
        max_length=20
    )
    date = models.DateTimeField(
        verbose_name="Дата"
    )

    class Meta:  # noqa
        ordering: Tuple[str] = (
            '-id',
        )
        verbose_name: str = 'Дата выпуска'
        verbose_name_plural: str = 'Даты выпуска'

    def __str__(self) -> str:  # noqa
        return f'Дата выпуска: {self.published}'


class AnimeQuerySet(QuerySet):
    """Anime queryset."""

    def get_deleted(self) -> QuerySet['Anime']:  # noqa
        return self.filter(
            datetime_deleted__isnull=False
        )

    def get_not_deleted(self) -> QuerySet['Anime']:  # noqa
        return self.filter(
            datetime_deleted__isnull=True
        )


class Anime(AbstractDateTime):
    """Anime entity."""

    studio = models.CharField(
        verbose_name="Студия",
        max_length=100
    )
    rating = models.IntegerField(
        verbose_name="Рейтинг"
    )
    release_date = models.ForeignKey(
        ReleaseDate,
        on_delete=models.PROTECT,
        verbose_name='Дата выпуска'
    )
    title = models.OneToOneField(
        Title,
        on_delete=models.CASCADE,
        verbose_name='Название'
    )
    description = models.OneToOneField(
        Description,
        on_delete=models.CASCADE,
        verbose_name="Описание"
    )
    objects = AnimeQuerySet().as_manager()

    class Meta:  # noqa
        ordering: Tuple[str] = (
            '-datetime_created',
        )
        verbose_name: str = 'Аниме'
        verbose_name_plural: str = 'Аниме'

    def __str__(self) -> str:  # noqa
        return f'{self.studio} | {self.title.name}, {self.rating}'

    def save(self, *args: tuple, **kwargs: dict) -> None:  # noqa
        self.full_clean()
        super().save(*args, **kwargs)

    def delete(self) -> None:  # noqa
        self.datetime_deleted = datetime.now()
        self.save(
            update_fields=['datetime_deleted']
        )
        # super().delete()


class Genre(models.Model):
    """Genre entiry."""

    name = models.CharField(
        verbose_name="Имя",
        max_length=50
    )
    anime = models.ManyToManyField(
        Anime,
        related_name="genres",
        verbose_name="аниме"
    )

    class Meta:  # noqa
        ordering: Tuple[str] = (
            'name',
        )
        verbose_name: str = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self) -> str:  # noqa
        return f'Жанр: {self.name}'
