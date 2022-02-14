"""
WSGI config for DRF_ModelViewSet_And_ReadyOnlyModelViewSet_API project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DRF_ModelViewSet_And_ReadyOnlyModelViewSet_API.settings')

application = get_wsgi_application()
