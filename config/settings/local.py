# -*- coding: utf-8 -*-
"""
Local settings

- Run in Debug mode
- Use console backend for emails
- Add Django Debug Toolbar
- Add django-extensions as app
"""

from .common import *  # noqa

import logging

DATABASES['default']['ENGINE'] = "django_db_geventpool.backends.postgresql_psycopg2"
DATABASES['default']['ATOMIC_REQUESTS'] = False
DATABASES['default']['CONN_MAX_AGE'] = 0
DATABASES['default']['OPTIONS'] = {"MAX_CONNS": 50}

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool("DJANGO_DEBUG", default=True)
# DEBUG = False

ALLOWED_HOSTS = ["localhost", "api"]
TEMPLATES[0]["OPTIONS"]["debug"] = DEBUG

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env(
    "DJANGO_SECRET_KEY", default="j##=9%n86#+%p#%ad%d*!o@9*9(0x-uvl-@(7q4-vwcu(cz71a"
)

# Mail settings
# ------------------------------------------------------------------------------
EMAIL_HOST = "localhost"
EMAIL_PORT = 1025

# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

INTERNAL_IPS = ("127.0.0.1", "10.0.2.2")

# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ("django_extensions",)

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = "django.test.runner.DiscoverRunner"

########## CELERY
# In development, all tasks will be executed locally by blocking until the task returns
CELERY_TASK_ALWAYS_EAGER = True
########## END CELERY

# print logging to the console
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {"format": "%(asctime)s %(levelname)s %(module)s: %(message)s"}
    },
    "filters": {"require_debug_true": {"()": "django.utils.log.RequireDebugTrue"}},
    "handlers": {
        "console": {
            # 'filters': ['require_debug_true'],
            "class": "logging.StreamHandler",
            "formatter": "simple",
        }
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": env.str("DJANGO_LOG_LEVEL", default="INFO"),
        },
        "period": {"handlers": ["console"], "level": logging.DEBUG},
        "simpl.games.apis": {"handlers": ["console"], "level": logging.DEBUG},
    },
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

SIMPL_WEBHOOK_ALLOW_LOCALHOST = True
SIMPL_WEBHOOK_ALLOW_HTTP = True
