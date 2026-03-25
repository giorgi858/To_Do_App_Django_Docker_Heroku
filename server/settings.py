from pathlib import Path
import os
from datetime import timedelta
from environs import Env
import dj_database_url
from django.utils.translation import gettext_lazy as _

env = Env()
env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------
# SECURITY
# -----------------------

SECRET_KEY = env("DJANGO_SECRET_KEY")

DEBUG = env.bool("DJANGO_DEBUG", default=False)

ALLOWED_HOSTS = env.list(
    "DJANGO_ALLOWED_HOSTS",
    default=[".herokuapp.com"]
)

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_SSL_REDIRECT = env.bool(
    "DJANGO_SECURE_SSL_REDIRECT",
    default=not DEBUG
)

SESSION_COOKIE_SECURE = env.bool(
    "DJANGO_SESSION_COOKIE_SECURE",
    default=not DEBUG
)

CSRF_COOKIE_SECURE = env.bool(
    "DJANGO_CSRF_COOKIE_SECURE",
    default=not DEBUG
)

SECURE_HSTS_SECONDS = env.int(
    "DJANGO_SECURE_HSTS_SECONDS",
    default=2592000
)

SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True


# -----------------------
# I18N
# -----------------------

LANGUAGE_CODE = "en"

LANGUAGES = [
    ("en", _("English")),
    ("ka", _("Georgian")),
]

TIME_ZONE = "UTC"

USE_I18N = True
USE_TZ = True

LOCALE_PATHS = [
    BASE_DIR / "locale",
]


# -----------------------
# APPS
# -----------------------

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",

    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",

    "django.contrib.sites",

    "corsheaders",

    "crispy_forms",
    "crispy_bootstrap5",

    "rest_framework",

    "allauth",
    "allauth.account",

    "django_celery_beat",
    "djcelery_email",

    "note",
    "api",
]


SITE_ID = 1


# -----------------------
# MIDDLEWARE
# -----------------------

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",

    "corsheaders.middleware.CorsMiddleware",

    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",

    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",

    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    "allauth.account.middleware.AccountMiddleware",
]


# -----------------------
# TEMPLATES
# -----------------------

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


ROOT_URLCONF = "server.urls"
WSGI_APPLICATION = "server.wsgi.application"


# -----------------------
# DATABASE
# -----------------------

DATABASES = {
    "default": dj_database_url.config(
        conn_max_age=600,
        ssl_require=True,
        default=os.getenv("DATABASE_URL")
    )
}

# -----------------------
# STATIC
# -----------------------

STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

STATIC_ROOT = BASE_DIR / "staticfiles"

STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)


# -----------------------
# AUTH
# -----------------------

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

LOGIN_REDIRECT_URL = "home"

ACCOUNT_SESSION_REMEMBER = True

ACCOUNT_EMAIL_VERIFICATION = "mandatory"

ACCOUNT_ADAPTER = "note.adapter.CeleryAccountAdapter"

ACCOUNT_SIGNUP_FIELDS = [
    "email*",
    "username*",
    "password1*",
    "password2*",
]


# -----------------------
# EMAIL
# -----------------------

EMAIL_BACKEND = "djcelery_email.backends.CeleryEmailBackend"

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")


# -----------------------
# CORS
# -----------------------

CORS_ALLOW_ALL_ORIGINS = env.bool(
    "CORS_ALLOW_ALL_ORIGINS",
    default=False
)


# -----------------------
# DRF + JWT
# -----------------------

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=15),
    "REFRESH_TOKEN_LIFETIME": timedelta(minutes=30),
}


# -----------------------
# SESSION
# -----------------------

SESSION_COOKIE_AGE = 60 * 60
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SAVE_EVERY_REQUEST = True


# -----------------------
# CELERY
# -----------------------

CELERY_BROKER_URL = os.getenv(
    "REDIS_URL",
    "redis://redis:6379/0"
)

CELERY_RESULT_BACKEND = os.getenv(
    "REDIS_URL",
    "redis://redis:6379/0"
)

CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"


CELERY_BEAT_SCHEDULE = {
    "test-every-minute": {
        "task": "note.tasks.test_task",
        "schedule": 60.0,
    },
}


# -----------------------
# DEFAULT PK
# -----------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"