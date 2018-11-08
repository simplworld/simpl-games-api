from __future__ import absolute_import

import os

import rollbar
import os
from celery import Celery
from django.apps import AppConfig
from django.conf import settings


if not settings.configured:
    # set the default Django settings module for the 'celery' program.
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")  # pragma: no cover


app = Celery('simpl')
rollbar_token = os.environ.get('DJANGO_ROLLBAR_TOKEN', str())
rollbar_env = os.environ.get('DJANGO_IMAGE_TAG', 'local')


class CeleryConfig(AppConfig):
    name = 'simpl.taskapp'
    verbose_name = 'Celery Config'

    def ready(self):
        # Using a string here means the worker will not have to
        # pickle the object when using Windows.

        if rollbar_token:
            rollbar.init(rollbar_token, rollbar_env)

        app.config_from_object('django.conf:settings', namespace='CELERY')
        app.autodiscover_tasks(lambda: settings.INSTALLED_APPS, force=True)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))  # pragma: no cover
