# -*- coding: utf-8 -*-
"""
Local settings

- Run in Debug mode
- Use console backend for emails
- Add Django Debug Toolbar
- Add django-extensions as app
"""

from .local import *  # noqa

import logging

DATABASES = {
    "default": {
        "ENGINE": "django_db_geventpool.backends.postgresql_psycopg2",
        "HOST": "db",
        "USER": "postgres",
        "NAME": "postgres",
        "PASSWORD": "",
        "PORT": 5432,
        "ATOMIC_REQUESTS": False,
        "CONN_MAX_AGE": 0,
        "OPTIONS": {"MAX_CONNS": 50},
    }
}

