"""
Django settings for project_name project.

Generated by 'django-admin startproject' using Django 3.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"
APPS_DIR = BASE_DIR / "apps"

env = environ.Env()

READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=True)
if READ_DOT_ENV_FILE:
    # OS environment variables take precedence over variables from .env
    env.read_env(str(BASE_DIR / ".env"))

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DJANGO_DEBUG", False)
# Local time zone. Choices are
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# though not all of them may be available with every OS.
# In Windows, this must be set to your system time zone.
TIME_ZONE = "UTC"
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "en-us"
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths
LOCALE_PATHS = [str(BASE_DIR / "locale")]

# PROJECT DETAILS
# ------------------------------------------------------------------------------
# These variables are used to populate data in the default templates
PROJECT_VERBOSE_NAME = env.str('PROJECT_VERBOSE_NAME', default='{{ project_name }}')
PROJECT_LOGO_URL = env.str('PROJECT_LOGO_URL', default=None)
PROJECT_PHONE_NUMBER = env('PROJECT_PHONE_NUMBER', default='')

# APPS
# ------------------------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
]

LIBRARY_APPS = [
    # django-webpack-loader (https://github.com/owais/django-webpack-loader)
    'webpack_loader',
    # django-crispy-forms (https://django-crispy-forms.readthedocs.io/en/latest/)
    'crispy_forms',
    # django-rest-framework (https://www.django-rest-framework.org/#)
    'rest_framework',
    # django-elasticsearch-dsl (https://django-elasticsearch-dsl.readthedocs.io/en/latest/)
    'django_elasticsearch_dsl',
    # django-allauth (https://django-allauth.readthedocs.io/en/latest/)
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    # django-tinymce (http://django-tinymce.readthedocs.org/)
    'tinymce',
]

PROJECT_APPS = [
    'apps.api',
    'apps.main',
    'apps.users',
]
# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + LIBRARY_APPS + PROJECT_APPS


# DATABASES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    "default": env.db("DATABASE_URL", default="postgres://postgres:postgres@db:5432/{{ project_name }}-db")
}

# MIDDLEWARE
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URLS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = '{{ project_name }}.urls'
# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = '{{ project_name }}.wsgi.application'


# TEMPLATES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR / "templates"), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'apps.main.context_processors.project_context',
            ],
        },
    },
]


# SECURITY
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#session-cookie-httponly
SESSION_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#csrf-cookie-httponly
CSRF_COOKIE_HTTPONLY = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secure-browser-xss-filter
SECURE_BROWSER_XSS_FILTER = True
# https://docs.djangoproject.com/en/dev/ref/settings/#x-frame-options
X_FRAME_OPTIONS = "DENY"


# AUTHENTICATION
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#authentication-backends
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-user-model
AUTH_USER_MODEL = "users.User"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
# LOGIN_REDIRECT_URL = "users:redirect"
# https://docs.djangoproject.com/en/dev/ref/settings/#login-url
# LOGIN_URL = "account_login"
# https://docs.djangoproject.com/en/dev/ref/settings/#logout-redirect-url
LOGOUT_REDIRECT_URL = 'index'


# PASSWORDS
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#password-hashers
PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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

# STATIC
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#manifeststaticfilesstorage
STATICFILES_STORAGE = env.str(
    'DJANGO_STATICFILES_STORAGE',
    'django.contrib.staticfiles.storage.StaticFilesStorage'
)
# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = env.str("DJANGO_STATIC_ROOT", str(BASE_DIR / "staticfiles"))
# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = MEDIA_URL = env.str("DJANGO_STATIC_URL", "/static/")
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [
    str(FRONTEND_DIR / "static"),
    str(BASE_DIR / "static"),
]
# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# MEDIA
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = env.str("DJANGO_MEDIA_ROOT", str(BASE_DIR / "media"))
# https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = env.str("DJANGO_MEDIA_URL", "/media/")

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#default-from-email
DEFAULT_FROM_EMAIL = env(
    "DJANGO_DEFAULT_FROM_EMAIL", default="{{ project_name }} <info@example.com>"
)
# https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = env("DJANGO_SERVER_EMAIL", default=DEFAULT_FROM_EMAIL)
# https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = env(
    "DJANGO_EMAIL_SUBJECT_PREFIX", default="[Django]"
)
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend"
)
# https://docs.djangoproject.com/en/dev/ref/settings/#email-timeout
EMAIL_TIMEOUT = 5


# ADMIN
# ------------------------------------------------------------------------------
# Django Admin URL regex.
ADMIN_URL = env("DJANGO_ADMIN_URL", default="admin")
# https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = []
# https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS


# Third Party Apps Settings
# ------------------------------------------------------------------------------

# DJANGO ALLAUTH
# ------------------------------------------------------------------------------
# https://django-allauth.readthedocs.io/en/latest/configuration.html
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': env('GOOGLE_CLIENT_ID', default=None),
            'secret': env('GOOGLE_CLIENT_SECRET', default=None)
        }
    }
}


# Celery
# ------------------------------------------------------------------------------
# https://docs.celeryproject.org/en/stable/userguide/configuration.html

# https://docs.celeryproject.org/en/stable/userguide/configuration.html#std-setting-broker_url
CELERY_BROKER_URL = env('DJANGO_CELERY_BROKER_URL', default='redis://redis:6379')
# https://docs.celeryproject.org/en/stable/userguide/configuration.html#std-setting-result_backend
CELERY_RESULT_BACKEND = env('DJANGO_CELERY_RESULT_BACKEND', default='redis://redis:6379/0')
# https://docs.celeryproject.org/en/stable/userguide/configuration.html#std-setting-accept_content
CELERY_ACCEPT_CONTENT = ['application/json']

# Django ELASTICSEARCH DSL
# ------------------------------------------------------------------------------
# https://django-elasticsearch-dsl.readthedocs.io/en/latest/settings.html
ELASTICSEARCH_DSL = {
    'default': {
        'hosts': env('DJANGO_ELASTICSEARCH_HOST', default='elasticsearch:9200'),
        'timeout': 30,
    },
}

# Django Crispy Forms
# ------------------------------------------------------------------------------
# http://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = "bootstrap4"

# Django REST Framework
# ------------------------------------------------------------------------------
# https://www.django-rest-framework.org/api-guide/settings/
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

# Django Webpack Loader
# ------------------------------------------------------------------------------
# https://github.com/owais/django-webpack-loader
WEBPACK_LOADER = {
    'DEFAULT': {
        'CACHE': not DEBUG,
        'BUNDLE_DIR_NAME': '',  # must end with slash
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
        'POLL_INTERVAL': 0.1,
        'TIMEOUT': None,
        'IGNORE': [r'.+\.hot-update.js', r'.+\.map']
    }
}

# TinyMCE
# ------------------------------------------------------------------------------
# https://django-tinymce.readthedocs.io/en/latest/installation.html#configuration
TINYMCE_SPELLCHECKER = True
TINYMCE_INCLUDE_JQUERY = False
TINYMCE_DEFAULT_CONFIG = {
    'branding': False,
    'plugins': 'image link lists media save help',
    'menubar': '',
    'toolbar': 'undo redo | styleselect | alignleft aligncenter alignright indent outdent | bullist numlist | bold italic underline strikethrough | link image media | help',
    'statusbar': True,
}
