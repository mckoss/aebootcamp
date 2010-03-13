import os

ENVIRONMENT = "unknown"
try:
    if os.environ["SERVER_SOFTWARE"].lower().startswith("dev"):
        ENVIRONMENT = "local"
    elif os.environ["SERVER_SOFTWARE"].lower().startswith("google apphosting"):
        ENVIRONMENT = "hosted"
except:
    pass

DEBUG = (ENVIRONMENT == "local")
#DEBUG = False

ADMINS = (
    # TODO: Change to your name and email address
    ('Mike Koss', 'mckoss@startpad.org'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = ''           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'ado_mssql'.
DATABASE_NAME = ''             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

TIME_ZONE = 'PST8PDT US'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
MEDIA_ROOT = ''
MEDIA_URL = ''
ADMIN_MEDIA_PREFIX = '/media/'
SECRET_KEY = ''

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    )

# For django.middleware.common.CommonMiddleware
APPEND_SLASH = False
PREPEND_WWW = False

ROOT_URLCONF = 'urls'

import os.path
dirHome = os.path.dirname(__file__)

TEMPLATE_DIRS = (
    os.path.join(dirHome, 'templates').replace('\\', '/'),
)

CACHE_MIDDLEWARE_SECONDS = 7*24*60*60

INSTALLED_APPS = (
    'django.contrib.humanize',
)

#TEMPLATE_STRING_IF_INVALID = "***ERROR***"
