from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from django_eel.consumers import EelConsumer

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    "websocket": URLRouter([
        re_path(r"^eel$", EelConsumer),
    ]),
})
