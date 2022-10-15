import os

from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#*u6$v9)ngp-vutc$stt++j_qqjh$031b_x&7i_)64s6*srhdn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG")

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'mptt',
    'social_django',
    'rest_framework',
    'rest_framework_swagger',
    'graphene_django',
    'django_filters',

    'authentication',
    'user',
    'user_profile',
    'assistance',
    'petition',
    'follower',
    'api'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portal.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
            'libraries': {
                'staticfiles': 'django.templatetags.static',
            }
        },
    },
]

WSGI_APPLICATION = 'portal.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.environ.get("POSTGRES_NAME"),
        "USER": os.environ.get("POSTGRES_USER"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD"),
        "HOST": os.environ.get("POSTGRES_HOST"),
        "PORT": os.environ.get("POSTGRES_PORT"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_USER_MODEL = "authentication.User"

LOGIN_URL = "authentication:login"
LOGIN_REDIRECT_URL = "user_profile:profile"
LOGOUT_REDIRECT_URL = "authentication:login"

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "assets")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Logging

DJANGO_LOG_PATH = os.environ.get("DJANGO_LOG_PATH", os.path.join(BASE_DIR, ".data/django.log"))
CELERY_LOG_PATH = os.environ.get("CELERY_LOG_PATH", os.path.join(BASE_DIR, ".data/celery.log"))

if not os.path.exists(os.path.dirname(DJANGO_LOG_PATH)):
    os.makedirs(os.path.dirname(DJANGO_LOG_PATH))

if not os.path.exists(os.path.dirname(CELERY_LOG_PATH)):
    os.makedirs(os.path.dirname(CELERY_LOG_PATH))

LOGFILE_SIZE = 5 * 1024 * 1024

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "{levelname} | {asctime} | {module} | {process:d} | {thread:d} | {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
        "base_file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": DJANGO_LOG_PATH,
            "maxBytes": LOGFILE_SIZE,
            "formatter": "base",
        },
        "celery_file": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "filename": CELERY_LOG_PATH,
            "maxBytes": LOGFILE_SIZE,
            "formatter": "base",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "base_file"],
            "level": os.environ.get("DJANGO_LOG_LEVEL", "INFO"),
            "propagate": True,
        },
        "celery": {
            "handlers": ["console", "celery_file"],
            "level": os.environ.get("CELERY_LOG_LEVEL", "INFO"),
            "propagate": True,
        },
    },
}

# Celery

CELERY_BROKER_URL = os.environ.get("BROKER_URL")
CELERY_RESULT_BACKEND = os.environ.get("RESULT_BROKER_URL")
CELERY_TASK_DEFAULT_QUEUE = "django"

# Cache

CACHE_DEFAULT_TIMEOUT = 60 * 60 * 8
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": os.environ.get("PAGE_CACHE_REDIS_URL"),
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            "MAX_ENTRIES": 5000,
        },
        "TIMEOUT": CACHE_DEFAULT_TIMEOUT,
    }
}

# Social authentication

AUTHENTICATION_BACKENDS = (
    "social_core.backends.google.GoogleOAuth2",
    "social_core.backends.facebook.FacebookOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)

SOCIAL_AUTH_URL_NAMESPACE = "social"

# REST

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_RENDERER_CLASSES": "rest_framework.renderers.JSONRenderer"
}

# GpaphQL

GRAPHENE = {
    "SCHEMA": "api.schemas.schema"
}
