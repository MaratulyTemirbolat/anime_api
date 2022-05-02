from django.apps import AppConfig


class AnimeConfig(AppConfig):  # noqa
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'anime'

    def ready(self) -> None:  # noqa
        import anime.signals  # noqa