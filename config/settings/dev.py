from .common import *
from logging.config import dictConfig
from jslog4kube import LOGGING

dictConfig(LOGGING)

env = environ.Env(
    DATABASE_NAME=(str, 'simpl'),
    DATABASE_USER=(str, 'simpl'),
    DATABASE_HOST=(str, 'localhost'),
    DATABASE_PASSWORD=str,
    SECRET_KEY=str,
)

SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = [
    'localhost',
]

ROLLBAR['environment'] = 'development'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'HOST': env('DATABASE_HOST'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'ATOMIC_REQUESTS': True,
        'CONN_MAX_AGE': 300,
    },
}
