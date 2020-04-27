from django.apps import AppConfig
from django.contrib.auth import get_user_model

from . import events


class SimplWebhookConfig(AppConfig):
    name = 'webhooks'

    def ready(self):
        pass