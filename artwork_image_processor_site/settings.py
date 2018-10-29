"""
Django settings for artwork_image_processor_site project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
try:
    # Configure Django App for Heroku.
    ## Activate Django-Heroku.
    import django_heroku
    django_heroku.settings(locals())
except ImportError:
    found = False

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@&n+hghx4ktg!%fr(qd-ve@!n03s3d*_x0k=d47z4@yag%eops'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['artwork-image-processor.herokuapp.com','*']


# Application definition

INSTALLED_APPS = [
    'artwork_image_processor.apps.ArtworkImageProcessorConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'artwork_image_processor_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'artwork_image_processor_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True

#--------------------------------------
# Static files (CSS, JavaScript, Images)
#STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# https://docs.djangoproject.com/en/2.1/howto/static-files/

#STATIC_ROOT = os.path.join(MEDIA_ROOT, 'static')
#STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

#STATIC_URL = '/static/'
#MEDIA_URL = '/media/'

#STATICFILES_DIRS = [
#    os.path.join(MEDIA_ROOT, "static"),
    #'/var/www/static/',
#]
#--------------------------------------

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(MEDIA_ROOT, "static"),
    #'/var/www/static/',
]
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
#django_heroku.settings(locals())
print("OLD BASE_DIR " + os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) ##/home/travis/build/wunyanw/artwork-image-processor/
print("NEW BASE_DIR? " + os.path.dirname(os.path.dirname(__file__))) #/home/travis/build/wunyanw/artwork-image-processor
print("THIRD NEW BASE_DIR " +os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
print("STATICFILES_DIRS " + os.path.join(MEDIA_ROOT, "static")) #/home/travis/build/wunyanw/artwork-image-processor/media/static
print("BASE_DIR with static " + os.path.join(BASE_DIR, "static")) #/home/travis/build/wunyanw/artwork-image-processor/static
print("PROJECT_ROOT with staticfiles " + os.path.join(PROJECT_ROOT, 'staticfiles')) #/home/travis/build/wunyanw/artwork-image-processor/artwork_image_processor_site/staticfiles
