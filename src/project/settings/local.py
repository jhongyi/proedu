'''
local settings
'''

import os
from project.settings.base import *
INSTALLED_APPS += ['corsheaders',]
MIDDLEWARE = ['corsheaders.middleware.CorsMiddleware',] + MIDDLEWARE

CORS_ORIGIN_ALLOW_ALL = True

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
