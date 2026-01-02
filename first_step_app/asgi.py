import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import gestion.routing as routing_layer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_step_app.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            routing_layer.websocket_urlpatterns
        )
    ),
})