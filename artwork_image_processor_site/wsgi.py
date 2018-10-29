"""
WSGI config for artwork_image_processor_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
#added 2104
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'artwork_image_processor_site.settings')

application = get_wsgi_application()
