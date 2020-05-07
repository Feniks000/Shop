"""
Django settings for shop project.

Generated by 'django-admin startproject' using Django 3.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'j)ua8xprpk@%rhi_@_n*5b^blj_c353*i=k#fm6xh)hy%&ap5u'

DEBUG = True
# DEBUG = False
ALLOWED_HOSTS = [
    '127.0.0.1',
    'starshop25.herokuapp.com',
]
VALIDATION_LINK = 'https://starshop25.herokuapp.com/accounts/validation'
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # loaded apps
    'showcase.apps.ShowcaseConfig',
    'private_office.apps.PrivateOfficeConfig',
    'storages',
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

ROOT_URLCONF = 'shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'shop.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbcqnbc4vcq78r',
        'USER': 'kgvbecpbwvbcjl',
        'PASSWORD': '95f5802188968b0e3b6bf69b6c633c7b6b6a20ef3b18c60cf7a5a31b02ab4995',
        'HOST': 'ec2-54-247-118-139.eu-west-1.compute.amazonaws.com',
        'PORT': '5432',

    }
}

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

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Asia/Vladivostok'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AWS_ACCESS_KEY_ID = 'AKIAUQJGDX7YJXFBSUZM'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'starshop25'
AWS_URL = 'https://starshop25.s3.eu-north-1.amazonaws.com/'

AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'

MEDIA_URL = AWS_URL + 'media/'
STATIC_URL = AWS_URL + 'static/'
MEDIA_ROOT = AWS_URL + 'media/'
STATIC_ROOT = AWS_URL + 'static/'
AWS_DEFAULT_ACL = None

STATICFILES_STORAGE = 'shop.storage_backends.StaticStorage'
DEFAULT_FILE_STORAGE = 'shop.storage_backends.MediaStorage'

LOGIN_REDIRECT_URL = '/'

if DEBUG:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': 'debug.log',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'DEBUG',
                'propagate': True,
            },
        },
    }

# Email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'noreply.starshop25@gmail.com'
EMAIL_HOST_PASSWORD = 'wsAu4s6Fs54QfSM'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
