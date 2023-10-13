# -*- coding: utf-8 -*-
"""
Django settings for simpl project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
import environ

ROOT_DIR = environ.Path(__file__) - 3  # (/a/b/myfile.py - 3 = /)
APPS_DIR = ROOT_DIR.path("simpl")

env = environ.Env()

# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.admin",
)

THIRD_PARTY_APPS = (
    "allauth",  # registration (also has a base.html which messes stuff up)
    "allauth.account",  # registration
    "allauth.socialaccount",  # registration
    "rest_framework",
    "rest_framework.authtoken",
    "rest_auth",
    "django_filters",
    "cuser",
    "drf_yasg",
    "corsheaders",
)

# Apps specific for this project go here.
LOCAL_APPS = (
    "simpl_users",  # custom users app
    "simpl.games.apps.SimplGamesConfig",
    "simpl.webhook",
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------
MIDDLEWARE = [
    # Make sure djangosecure.middleware.SecurityMiddleware is listed first
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "rollbar.contrib.django.middleware.RollbarNotifierMiddleware",
]

# MIGRATIONS CONFIGURATION
# ------------------------------------------------------------------------------
MIGRATION_MODULES = {"sites": "simpl.contrib.sites.migrations"}

# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)

# FIXTURE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (str(APPS_DIR.path("fixtures")),)

# EMAIL CONFIGURATION
# ------------------------------------------------------------------------------
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = ()

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    "default": env.db("DATABASE_URL", default="postgres:///simpl"),
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# GENERAL CONFIGURATION
# ------------------------------------------------------------------------------
# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = "UTC"

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en-us"

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# TEMPLATE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            str(APPS_DIR.path("templates")),
        ],
        "OPTIONS": {
            "debug": DEBUG,
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# STATIC FILE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = str(ROOT_DIR("staticfiles"))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [
    str(APPS_DIR.path("static")),
]

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = str(APPS_DIR("media"))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = "/media/"

# URL Configuration
# ------------------------------------------------------------------------------
ROOT_URLCONF = "config.urls"

# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "config.wsgi.application"

# AUTHENTICATION CONFIGURATION
# ------------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

# Some really nice defaults
ACCOUNT_AUTHENTICATION_METHOD = "username"
ACCOUNT_USER_MODEL_USERNAME_FIELD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "optional"

ACCOUNT_ALLOW_REGISTRATION = env.bool("DJANGO_ACCOUNT_ALLOW_REGISTRATION", True)
ACCOUNT_ADAPTER = "simpl_users.adapters.AccountAdapter"
SOCIALACCOUNT_ADAPTER = "simpl_users.adapters.SocialAccountAdapter"

# Custom user app defaults
# Select the correct user model
AUTH_USER_MODEL = "simpl_users.User"
LOGIN_REDIRECT_URL = "users:redirect"
LOGIN_URL = "account_login"

# SLUGLIFIER
AUTOSLUG_SLUGIFY_FUNCTION = "slugify.slugify"

# Redis Configuration
REDIS_HOST = env("REDIS_HOST", default="redis")

# Celery Configuration
CELERY_BROKER_REDIS_DB = env("CELERY_BROKER_REDIS_DB", default="1")
CELERY_RESULT_REDIS_DB = env("CELERY_RESULT_REDIS_DB", default="1")

CELERY_BROKER_URL = env(
    "CELERY_BROKER_URL", default=f"redis://{REDIS_HOST}:6379/{CELERY_BROKER_REDIS_DB}"
)

CELERY_RESULT_BACKEND = env(
    "CELERY_RESULT_BACKEND",
    default=f"redis://{REDIS_HOST}:6379/{CELERY_RESULT_REDIS_DB}",
)
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "UTC"
CELERY_TASK_ALWAYS_EAGER = env.bool("CELERY_TASK_ALWAYS_EAGER", default=DEBUG)

# Location of root django.contrib.admin URL, use {% url 'admin:index' %}
ADMIN_URL = r"^admin/"

# Your common stuff: Below this line define 3rd party library settings

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_FILTER_BACKENDS": (
        # 'rest_framework.filters.DjangoFilterBackend',
        "django_filters.rest_framework.DjangoFilterBackend",
    ),
    "DEFAULT_PAGINATION_CLASS": "simpl.core.pagination.LinkHeaderPagination",
    "PAGE_SIZE": 500,
}

REST_AUTH_SERIALIZERS = {
    "USER_DETAILS_SERIALIZER": "simpl_users.apis.serializers.UserSerializer"
}

SWAGGER_SETTINGS = {
    "LOGOUT_URL": "/accounts/logout/",
    "SECURITY_DEFINITIONS": {
        "Basic": {"type": "basic"},
    },
}

CORS_ORIGIN_ALLOW_ALL = False
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

SIMPL_WEBHOOK_ALLOW_LOCALHOST = False
SIMPL_WEBHOOK_ALLOW_HTTP = False