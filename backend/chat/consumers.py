import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User

from chat.models import Chat, Message


class ChatConsumer(AsyncWebsocketConsumer):
    chat_id = ""

    async def connect(self):
        self.chat_id = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = "{}".format(self.chat_id)
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, code):
        # leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    @database_sync_to_async
    def new_message(self, user_id, message):
        user = User.objects.get(id=user_id)
        chat = Chat.objects.get(id=self.chat_id)
        Message.objects.create(user=user, chat=chat, text=message)

    # Receive message from WebSocket
    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        user_id = text_data_json['user_id']
        message = text_data_json['message']

        await self.new_message(user_id=user_id, message=message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'user_id': user_id,
                'message': message,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        user_id = event['user_id']

        await self.send(text_data=json.dumps({
            'user_id': user_id,
            'message': message,
        }, ensure_ascii=False))
