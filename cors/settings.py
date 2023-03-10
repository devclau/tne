"""
Django settings for cors project.

Generated by 'django-admin startproject' using Django 3.2.16.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
import cx_Oracle
import os

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/
cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_21_7")
#cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_11_2")



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&vd(*y-o!oak@go@#ldz4jc+k03nu1jxeb=3huv%v+w+t4$!qz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tne',
    'crispy_forms',
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

ROOT_URLCONF = 'cors.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
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

WSGI_APPLICATION = 'cors.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / '++++++',
    },

    'DELFOS': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': '++++++',
        'USER': '+++++',
        'PASSWORD': '+++++',
    },
}



# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

#PARA LINUX

#STATIC_URL = '/static/'
#STATIC_ROOT = (
#    os.path.join(BASE_DIR, 'static'),
#)

#PARA WINDOWS
STATIC_ROOT = ''
STATIC_URL = '/static/'
STATICFILES_DIRS = ('static',)


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

###LDAP
import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType, PosixGroupType


# Baseline configuration.
AUTH_LDAP_SERVER_URI = "ldap://+++++++"

AUTH_LDAP_BIND_DN = "cn=readadmin,dc=ulagos,dc=cl"
AUTH_LDAP_BIND_PASSWORD = "++++"
#AUTH_LDAP_USER_SEARCH = LDAPSearch(
#    "ou=people,dc=ulagos,dc=cl", ldap.SCOPE_SUBTREE, "(uid=%(user)s)"
#)
# Or:

AUTH_LDAP_USER_DN_TEMPLATE = 'uid=%(user)s,ou=people,dc=ulagos,dc=cl'

# Set up the basic group parameters.
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    'ou=group,dc=ulagos,dc=cl',
    ldap.SCOPE_SUBTREE,
    '(objectClass=posixGroup)',
)
AUTH_LDAP_GROUP_TYPE = PosixGroupType()
AUTH_LDAP_USER_ATTR_MAP = {
    'first_name': 'givenName',
    'last_name': 'sn',
    'email': 'mail',
    'PERS_COD':'carLicense'
    
}
#objectClass=organizationalUnit

AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    'is_active': 'cn=Personal,ou=group,dc=ulagos,dc=cl',
    'is_staff': 'cn=Personal,ou=group,dc=ulagos,dc=cl',
    'is_superuser': 'cn=Personal,ou=group,dc=ulagos,dc=cl',
}


# Keep ModelBackend around for per-user permissions and maybe a local
# superuser.
AUTHENTICATION_BACKENDS = (
    "django_auth_ldap.backend.LDAPBackend",
    "django.contrib.auth.backends.ModelBackend",
)

import logging

logger = logging.getLogger('django_auth_ldap')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)
