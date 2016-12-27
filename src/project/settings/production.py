'''
production settings
'''

from project.settings.base import *
import os

DEBUG = False

ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("POSTGRES_DB_NAME"),
        'USER': os.environ.get("POSTGRES_USER"),
        'HOST': os.environ.get("POSTGRES_HOST"),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD"),
        'PORT': os.environ.get('POSTGRES_PORT'),
        'CONN_MAX_AGE': 60,
    }
}


# # deploy ex: STATIC_ROOT = "/var/www/example.com/static/"
STATIC_ROOT = os.environ['STATICFILES_PATH']

REST_FRAMEWORK_DOCS = {
    'HIDE_DOCS': True  # Default: False
}

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}