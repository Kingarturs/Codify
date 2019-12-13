import asyncio
import json
from django.contrib.auth import get_user_model
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from .models import Documento, Carpeta
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.consumer import SyncConsumer
import channels
import io
import os

class DocumentConsumer(SyncConsumer):
    def websocket_connect(self, event):
        # print("connected", event)
        self.send({
            "type":"websocket.accept",
        })

        self.username = self.scope['session']['sesion']
        # print(self.username)
        # async_to_sync(self.channel_layer.group_add)("chat", self.channel_name)

    def websocket_receive(self, event):
        # texto = event['text'].replace(u'\xa0', u' ')
        dic = json.loads(event['text'])
        tipo = dic['tipo']

        if tipo == "1":
            cambio = json.loads(event['text'])['contenido'].replace(u'\xa0', u' ')
            ruta = json.loads(event['text'])['dir']
            nombre = json.loads(event['text'])['nombre']

            if(ruta == ""):
                with io.open("Code/%s/%s"%(self.scope['session']['sesion'], nombre), 'w', encoding='utf8') as f:
                    f.write(cambio)
            else:
                with io.open("Code/%s/%s/%s"%(self.scope['session']['sesion'], ruta, nombre), 'w', encoding='utf8') as f:
                    f.write(cambio)

            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'enviar_archivo',
                    'text': cambio
                }
            )
        else:
            ruta = json.loads(event['text'])['dir']
            nombre = json.loads(event['text'])['nombre']
            usuario = json.loads(event['text'])['usuario']
            
            
            self.room_name = usuario + "_" + ruta + "_" + nombre
            self.room_group_name = 'file_%s' % self.room_name

            async_to_sync(self.channel_layer.group_add)(
                self.room_group_name,
                self.channel_name
            )
        

    def enviar_archivo(self, event):
        # message = event['message']

        # Send message to WebSocket
        self.send({
            "type":"websocket.send",
            "text": event['text'],
        })
    
    def websocket_disconnect(self, event):
        print("Deconectado", event) 