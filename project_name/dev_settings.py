import os

from .base_settings import *

# Dev Environment specific settings
DEBUG = True
ALLOWED_HOSTS = ['*']

# Django debug toolbar settings
INSTALLED_APPS += ['debug_toolbar',]

INTERNAL_IPS = ('::ffff:10.0.2.2',)

DEBUG_TOOLBAR_PATCH_SETTINGS = False

MIDDLEWARE_CLASSES = ('debug_toolbar.middleware.DebugToolbarMiddleware',) + MIDDLEWARE_CLASSES

#Staticfiles settings
STATIC_ROOT = os.path.join(BASE_DIR,'static')
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

# Development URLs
ROOT_URLCONF = '{{ project_name }}.dev_urls'

# CORS settings
CORS_ORIGIN_ALLOW_ALL = True

REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'] = ['rest_framework.permissions.AllowAny']
