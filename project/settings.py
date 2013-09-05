# Django settings for project project.
import mimetypes
import os

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
from django.core.urlresolvers import reverse_lazy
import django_cache_url
import dj_database_url


PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
ROOT_DIR = os.path.dirname(PROJECT_DIR)

DEBUG = bool(os.environ.get('DEBUG', False))
DEVELOPMENT_SITE = bool(os.environ.get('DEVELOPMENT_SITE', False))

DATABASES = {'default': dj_database_url.config(default='postgres://localhost/project')}

CACHES = {'default': django_cache_url.config()}

ADMINS = (('Admin', 'bugs@incuna.com'),)
MANAGERS = ADMINS
ADMIN_EMAILS = zip(*ADMINS)[1]
EMAIL_SUBJECT_PREFIX = '[project] '
SERVER_EMAIL = DEFAULT_FROM_EMAIL = 'info@incuna.com'
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')

TIME_ZONE = 'UTC'
USE_L10N = True  # Locale
USE_TZ = True

LANGUAGE_CODE = 'en-GB'
USE_I18N = False  # Internationalization

# Static
MEDIA_ROOT = os.path.join(ROOT_DIR, 'client_media')
MEDIA_URL = '/client_media/'
STATICFILES_DIR = os.path.join(PROJECT_DIR, 'static')
STATICFILES_DIRS = (STATICFILES_DIR,)
STATIC_ROOT = os.path.join(ROOT_DIR, 'static_media')
STATIC_URL = os.environ.get('STATIC_URL', '/static/')
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

CSS_DEBUG = bool(os.environ.get('CSS_DEBUG', False))

mimetypes.add_type('text/x-component', '.htc')

TEMPLATE_DEBUG = DEBUG
TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'never_cache_post.middleware.NeverCachePostMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

LOGIN_URL = reverse_lazy('auth_login')
LOGOUT_URL = reverse_lazy('auth_logout')
LOGIN_REDIRECT_URL = '/'

ROOT_URLCONF = 'project.urls'
SECRET_KEY = 'pmk0s)va^_dt&@hexnfj@hqh7iy7+#sbb+#%kloq@-bmi&vrz1'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')
SITE_ID = 1
WSGI_APPLICATION = 'project.wsgi.application'

INSTALLED_APPS = (
    # Project Apps
    'project',

    # Libraries
    'south',
    'debug_toolbar',
    'django_extensions',
    'gunicorn',
    'raven.contrib.django',
    'never_cache_post',

    # Django
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
)

SENTRY_DSN = os.environ.get('SENTRY_DSN')
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'console': {
            'format': '[%(asctime)s][%(levelname)s] %(name)s %(filename)s:%(funcName)s:%(lineno)d | %(message)s',
            'datefmt': '%H:%M:%S',
        },
    },
    'filters': {
        'require_debug_false': {'()': 'django.utils.log.RequireDebugFalse'}
    },
    'handlers': {
        'sentry': {
            'level': 'DEBUG',
            'filters': ['require_debug_false'],
            'class': 'raven.contrib.django.handlers.SentryHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['sentry', 'console'],
            'level': 'ERROR',
            'propagate': True,
        },
        'incuna.default': {
            'handlers': ['sentry', 'console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'sentry.errors': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propogate': True,
        },
    }
}

# Debug Toolbar
DEBUG_TOOLBAR_CONFIG = {'INTERCEPT_REDIRECTS': False}
INTERNAL_IPS = ('127.0.0.1',)

# Sorl settings
THUMBNAIL_DEBUG = DEBUG
THUMBNAIL_SUBDIR = '_thumbs'
THUMBNAIL_QUALITY = 95
