"""
ASGI config for django_snippets project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

#  Copyright (c) 2021.
#  Julio Cezar Riffel <julioriffel@gmail.com>

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_snippets.settings')

application = get_asgi_application()
