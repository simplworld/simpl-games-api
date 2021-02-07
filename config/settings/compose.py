# -*- coding: utf-8 -*-
"""
docker-compose settings
"""

from .local import *  # noqa

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
