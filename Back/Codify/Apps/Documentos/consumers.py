import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from .models import Documento, Carpeta
import channels
class DocumentConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        await self.send({
            "type":"websocket.accept",
        })

        # await asyncio.sleep(10)
        # await self.send({
        #     "type":"websocket.close",
        # })
        username = self.scope['session']['sesion']
        # await self.send({
        #     "type":"websocket.send",
        #     "text": username,
        # })

    async def websocket_receive(self, event):
        texto = event['text'].replace(u'\xa0', u' ')
        await self.send({
            "type":"websocket.send",
            "text": texto + str(self.scope['session']['sesion']),
        })

    
    async def websocket_disconnect(self, event):
        print("Deconectado", event) 