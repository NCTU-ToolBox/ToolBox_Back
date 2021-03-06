"""
Django settings for toolbox project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')=1(@+df(5x+z65bq3#!q#u+^6jh0n&4k9-i8_6jed4)u0i!@t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
DEVELOPE = True
if DEVELOPE is True:
	from .local_settings import *

ALLOWED_HOSTS = []
# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.sites',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'toolbox',
	'rest_framework',
	'django_filters',
	'rest_framework_docs',
	'api',
]
SITE_ID = 1
MIDDLEWARE_CLASSES = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'toolbox.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [
		],
		'APP_DIRS': True,
		'OPTIONS': {
			'context_processors': [
				'django.contrib.auth.context_processors.auth',
				'django.template.context_processors.debug',
				'django.template.context_processors.i18n',
				'django.template.context_processors.media',
				'django.template.context_processors.static',
				'django.template.context_processors.tz',
				'django.contrib.messages.context_processors.messages',
			]
		}

	}
]

WSGI_APPLICATION = 'toolbox.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),}}

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [{'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
                            {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
                            {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
                            {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',}, ]

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
	#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

REST_FRAMEWORK = {'DEFAULT_AUTHENTICATION_CLASSES': (
	'rest_framework.authentication.BasicAuthentication',
	'rest_framework.authentication.SessionAuthentication',
)}
AUTH_USER_MODEL = 'api.CustomUser'
SWAGGER_SETTINGS = {
	'LOGIN_URL': 'rest_framework:login',
	'LOGOUT_URL': 'rest_framework:logout',
	'USE_SESSION_AUTH': True,
	'DOC_EXPANSION': 'list',
	'APIS_SORTER': 'alpha',
	'SHOW_REQUEST_HEADERS': True
}
