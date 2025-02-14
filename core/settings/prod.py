import os

from core.settings.base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:
   ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql',
       'NAME': os.environ['POSTGRES_DB'],
       'USER': os.environ['POSTGRES_USER'],
       'PASSWORD': os.environ['POSTGRES_PASSWORD'],
       'HOST': os.environ['POSTGRES_HOST'],
       'PORT': os.environ['POSTGRES_DB_PORT'],
       'OPTIONS': {
           'sslmode': 'require',
       },
   }
}

#Admin user credentials

ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'Password123')
ADMIN_EMAIL =os.getenv('ADMIN_EMAIL', 'admin@gmail.com')
POSITION = "manager"
