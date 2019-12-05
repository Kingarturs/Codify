from django.urls import path
from django.conf.urls import url
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from Apps.Documentos import consumers

application = ProtocolTypeRouter({

    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    url(r"^index/(?P<documento>[\w.@+-]+)$", consumers.DocumentConsumer)
                ]
            )
        )
    )
})