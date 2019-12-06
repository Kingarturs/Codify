import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from .models import Documento, Carpeta


class DocumentConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        await self.send({
            "type":"websocket.accept",
        })

        user = self.scope['user']
        print(user)

        await self.send({
            "type":"websocket.send",
            "text": "user",
        })

    async def websocket_receive(self, event):
        print("Recibir", event)
    
    async def websocket_disconnect(self, event):
        print("Deconectado", event)