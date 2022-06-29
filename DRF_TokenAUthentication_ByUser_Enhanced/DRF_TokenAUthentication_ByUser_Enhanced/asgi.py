"""
ASGI config for DRF_TokenAUthentication_ByUser_Enhanced project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DRF_TokenAUthentication_ByUser_Enhanced.settings')

application = get_asgi_application()
