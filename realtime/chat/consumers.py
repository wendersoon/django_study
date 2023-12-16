import json

from channels.generic.websocket import AsyncWebsocketConsumer # The class we're using
from asgiref.sync import sync_to_async # Implement later


class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        print("Connecting")
        self.room_name = self.scope['url_route']['kwargs']['nome_sala']
        self.room_group_name = f'chat_{self.room_name}'
        
        # entrar na sala
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.room_name,
        )
        
        await self.accept()
        
        
    async def disconnect(self, code):
        # sai da sala
        print('oi')
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )
        
    # Recebe mensagem do WebSocket
    async def receive(self, text_data):
        text_data_json = json.load(text_data)
        mensagem = text_data_json['mensagem']
        
        # Envia a mensagem para a sala
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message':mensagem
            }
        )
        
    # Recebe a mensagem da sala
    async def chat_message(self, event):
        mensagem = event['message']
        
        # Envia a mensagem para o WebSocket
        await self.send(text_data=json.dumps({
            'mensagem':mensagem
        }))