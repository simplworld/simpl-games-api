from .local import *  # noqa

# Speeding up the tests

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    # 'allauth.account.auth_backends.AuthenticationBackend',
)

PASSWORD_HASHERS = (
    'django.contrib.auth.hashers.MD5PasswordHasher',
)


class DisableMigrations(object):

    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return "notmigrations"

MIGRATION_MODULES = DisableMigrations()
