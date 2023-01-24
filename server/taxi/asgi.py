"""
ASGI config for taxi project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

from trips.consumers import TaxiConsumer

import os

from django.core.asgi import get_asgi_application
from django.urls import path

from channels.routing import ProtocolTypeRouter, URLRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taxi.settings')


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        'websocket': URLRouter([
            path('taxi/', TaxiConsumer.as_asgi()),
        ])
    }
)
