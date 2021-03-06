"""
Base django settings for {{cookiecutter.project_name}} project.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DJANGO_DEBUG", False) in ["True", "1", "yes", "true", "TRUE", "on", "ON", "On"]

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "").split(",")

ROOT_URLCONF = '{{ cookiecutter.repo_name }}.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = '{{ cookiecutter.repo_name }}.wsgi.application'

# A tuple that lists people who get code error notifications when DEBUG=False
ADMINS = (
    ("{{ cookiecutter.author_name }}", "{{ cookiecutter.email }}")
)

MANAGERS = (
)

SITE_ID = 1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('POSTGRES_USER', "{{ cookiecutter.repo_name }}"),
        'USER': os.getenv('POSTGRES_USER', "{{ cookiecutter.repo_name }}"),
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': 'postgres',  # docker-compose linked
        'PORT': '',
    },
}

# https://docs.djangoproject.com/en/stable/topics/i18n/
LANGUAGE_CODE = 'nl'
LANGUAGES = (
    ('nl', 'Nederlands'),
)

USE_TZ = True
TIME_ZONE = '{{ cookiecutter.timezone }}'
USE_L10N = True

# STORAGE
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", None)
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", None)
AWS_STORAGE_BUCKET_NAME = '{{ cookiecutter.repo_name }}-public'
AWS_QUERYSTRING_AUTH = False
AWS_S3_HOST = "storage.googleapis.com"

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATIC_URL = "https://{}/{}/".format(AWS_S3_HOST, AWS_STORAGE_BUCKET_NAME)
STATICFILES_STORAGE = DEFAULT_FILE_STORAGE
MEDIA_URL = STATIC_URL


DJANGO_APPS = (
    'djangocms_admin_style',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
)

THIRD_PARTY_APPS = (
    'cms',  # django CMS itself
    'treebeard',  # utilities for implementing a tree
    'menus',  # helper for model independent hierarchical website navigation
    'sekizai',  # for javascript and css management
    'djangocms_picture',
    'djangocms_text_ckeditor',
    'djangocms_link',
    'debug_toolbar',
    'django_extensions',
    'djangocms_column',
    'djangocms_forms',
    'sorl.thumbnail',
    'storages',
    'djrill',
)

LOCAL_APPS = (
)

INSTALLED_APPS = LOCAL_APPS + DJANGO_APPS + THIRD_PARTY_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
        ],
        'OPTIONS': {
            'context_processors': (
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.i18n',
                'django.template.context_processors.request',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'sekizai.context_processors.sekizai',
                'cms.context_processors.cms_settings',
            ),
        }
    }
]

CMS_TEMPLATES = (
    ('cms/home.html', 'Home'),
    ('cms/default.html', 'Standaard'),
)

MIGRATION_MODULES = {
    # Some modules have their migrations not in the migrations folder, due to using south in the past:
    'djangocms_picture': 'djangocms_picture.migrations_django',
    'djangocms_column': 'djangocms_column.migrations_django',
}

THUMBNAIL_DEBUG = DEBUG

# E-mail:
SERVER_EMAIL = '{{ cookiecutter.repo_name }} webserver <server@urga.be>'
DEFAULT_FROM_EMAIL = "{{ cookiecutter.project_name }} <{{ cookiecutter.email }}>"
MANDRILL_API_KEY = os.getenv("MANDRILL_API_KEY", None)
MANDRILL_SUBACCOUNT = "{{ cookiecutter.repo_name }}"
EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'toolbar': 'CMS',
    'skin': 'moono',
    'stylesSet': [
        {'name': 'Intro', 'element': 'p', 'attributes': {'class': 'text-lead text-center'}},
        {'name': 'Horizontal list', 'element': 'ul', 'attributes': {'class': 'list-inline text-center'}},
    ],
    'contentsCss': [STATIC_URL + 'css/main.css'],
    'toolbarCanCollapse': False,
}

COLUMN_WIDTH_CHOICES = (
    ('1', ("1/12e kolom")),
    ('2', ("2/12e kolommen")),
    ('3', ("3/12e kolommen")),
    ('4', ("4/12e kolommen")),
    ('5', ("5/12e kolommen")),
    ('6', ("6/12e kolommen")),
    ('7', ("7/12e kolommen")),
    ('8', ("8/12e kolommen")),
    ('9', ("9/12e kolommen")),
    ('10', ("10/12e kolommen")),
    ('11', ("11/12e kolommen")),
    ('12', ("12/12e kolommen")),
)

DEBUG_TOOLBAR_PATCH_SETTINGS = False
