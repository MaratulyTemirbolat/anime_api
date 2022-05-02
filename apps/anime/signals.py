from logging import (
    getLogger,
    Logger,
)

from django.dispatch import receiver
from django.db.models.signals import (
    post_save,
    pre_save,
    post_delete,
    pre_delete,
)
from django.core.signals import (
    request_finished,
)
from django.db.models.base import ModelBase

from anime.models import (
    Anime,
)
from abstracts.utils import send_email


logger: Logger = getLogger('wagtail.core')


@receiver(
    signal=post_save,
    sender=Anime
)
def post_save_anime(
    sender: ModelBase,
    instance: Anime,
    created: bool,
    **kwargs: dict
) -> None:
    """Signal post-save Anime."""
    # Sending Email to User linked to Anime as uploader
    #
    print("The signal post_save_anime is triggered")
    # print("---------------BREAKPOINT--------------------")
    # breakpoint()
    logger.info("The Anime is post-saved (in post_save_anime)")
    # send_email(
    #     'Test Django subject',
    #     'If you see this message, the message sender ' +
    #     f'works pretty good and Anime: "{instance}" is saved.',
    #     [
    #         'd_urmanchina@mail.ru',
    #         'damirochka_99@mail.ru',
    #         'dama260999@gmail.com'
    #     ]
    # )
    # instance.save


@receiver(
    signal=pre_save,
    sender=Anime
)
def pre_save_anime(
    sender: ModelBase,
    instance: Anime,
    *args: tuple,
    **kwargs: dict
) -> None:
    """Signal pre-save for Anime instance."""
    print("The signal pre_save_anime is triggered")
    # print("---------------BREAKPOINT--------------------")
    # breakpoint()
    logger.info("The Anime is pre-saved (in pre_save_anime)")


@receiver(
    signal=post_delete,
    sender=Anime
)
def post_delete_anime(
    sender: ModelBase,
    instance: Anime,
    *args: tuple,
    **kwargs: dict
) -> None:
    """Signal post-delete for Anime instance."""
    # print("---------------BREAKPOINT--------------------")
    # breakpoint()
    logger.info("The Anime is deleted (in post_delete_anime)")


@receiver(
    signal=pre_delete,
    sender=Anime
)
def pre_delete_anime(
    sender: ModelBase,
    instance: Anime,
    *args: tuple,
    **kwargs: dict
) -> None:
    """Signal pre-delete for Anime instance."""
    # print("---------------BREAKPOINT--------------------")
    # breakpoint()
    logger.info("The Anime is pre-deleted (in pre_delete_anime)")
