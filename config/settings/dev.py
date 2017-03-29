from .common import *
env = environ.Env(
    DATABASE_NAME=(str, 'simpl'),
    DATABASE_USER=(str, 'simpl'),
    DATABASE_HOST=(str, 'localhost'),
    DATABASE_PASSWORD=str,
    SECRET_KEY=str,
)

SECRET_KEY = env('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'HOST': env('DATABASE_HOST'),
        'PASSWORD': env('DATABASE_PASSWORD'),
    },
}
DATABASES['default']['ATOMIC_REQUESTS'] = True
