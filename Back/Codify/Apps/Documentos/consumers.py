import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from .models import Documento, Carpeta
import channels
import io
import os

class DocumentConsumer(AsyncConsumer):
    async def websocket_connect(self, event):
        print("connected", event)
        await self.send({
            "type":"websocket.accept",
        })

        self.username = self.scope['session']['sesion']
        print(self.username)

    async def websocket_receive(self, event):
        texto = event['text'].replace(u'\xa0', u' ')
        cambio = json.loads(event['text'])['contenido']
        ruta = json.loads(event['text'])['dir']
        nombre = json.loads(event['text'])['nombre']

        if(ruta == ""):
            with io.open("Code/%s/%s"%(self.scope['session']['sesion'], nombre), 'w', encoding='utf8') as f:
                f.write(cambio)
        else:
            with io.open("Code/%s/%s/%s"%(self.scope['session']['sesion'], ruta, nombre), 'w', encoding='utf8') as f:
                f.write(cambio)
    
    async def websocket_disconnect(self, event):
        print("Deconectado", event) 