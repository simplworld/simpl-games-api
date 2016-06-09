from django.apps import AppConfig
from django.contrib.auth import get_user_model

from thorn import model_reverser, webhook_model

from . import events


class SimplGamesConfig(AppConfig):
    name = 'games'

    def ready(self):
        webhook_model(get_user_model(),
            on_change=events.on_user_changed,
            on_create=events.on_user_created,
            on_delete=events.on_user_deleted,
            reverse=model_reverser('simpl_api:user-detail', username='username'),
        )
