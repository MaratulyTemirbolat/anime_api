from typing import (
    Tuple,
)

from rest_framework.serializers import (
    ModelSerializer,
    IntegerField,
    CharField,
    # EmailField,
    # BooleanField,
    DateTimeField,
    SerializerMethodField,
)

from anime.models import (
    Description,
    Title,
    ReleaseDate,
    Anime,
    # Genre,
)


class ReleaseDateSerializer(ModelSerializer):
    """ReleseDate serializer."""

    published: CharField = CharField(
        required=True
    )
    date: DateTimeField = DateTimeField(
        read_only=True
    )  # just list/retrieve methods

    class Meta:  # noqa
        model: ReleaseDate = ReleaseDate
        fields: Tuple[str] = (
            'published',
            'date',
        )


class TitleSerializer(ModelSerializer):
    """Title serializer."""

    name: CharField = CharField(required=True)
    link: CharField = CharField(read_only=True)

    class Meta:  # noqa
        model: Title = Title
        fields: Tuple[str] = (
            'name',
            'link',
        )


class DescriptionSerializer(ModelSerializer):
    """Description serializer."""

    text_en: CharField = CharField(read_only=True)
    text_ru: CharField = CharField(read_only=True)

    class Meta:  # noqa
        model: Description = Description
        fields: Tuple[str] = (
            'text_en',
            'text_ru',
        )


class AnimeSerializer(ModelSerializer):
    """Anime serializer."""

    id: IntegerField = IntegerField(read_only=True)
    studio: CharField = CharField()
    rating: IntegerField = IntegerField()
    release_date: ReleaseDateSerializer = ReleaseDateSerializer(
        required=True
    )
    title: TitleSerializer = TitleSerializer(
        required=True
    )
    description: DescriptionSerializer = DescriptionSerializer(
        required=True
    )
    datetime_created = DateTimeField(read_only=True)
    datetime_updated = DateTimeField(read_only=True)
    datetime_deleted = DateTimeField(read_only=True)

    name = SerializerMethodField(
        method_name="get_name"
    )

    class Meta:  # noqa
        model: Anime = Anime
        fields: Tuple[str] = (
            'id',
            'studio',
            'rating',
            'release_date',
            'title',
            'description',
            'datetime_created',
            'datetime_updated',
            'datetime_deleted',
            'name',
        )

    def get_name(self, obj: Anime) -> int:  # noqa
        return f'{obj.studio} | {obj.title.name}'
