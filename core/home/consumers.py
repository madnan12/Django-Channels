from channels.generic.websocket import WebsocketConsumer, AsyncJsonWebsocketConsumer
from asgiref.sync import async_to_sync
import json


class TestConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = 'test_consumer'
        self.room_group_name = 'test_consumer_group'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,

        )

        self.accept()
        self.send(text_data=json.dumps({'status': 'connetced'}))


    def receive(self, text_data):
        self.send(text_data=json.dumps({'status': 'we received data!'}))

    def disconnect(self):
        pass
    
    def send_notifications(self, event):
        data = json.loads(event.get('data'))
        self.send(text_data=json.dumps({'notification': data}))


class NewComsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.room_name = 'test_consumer'
        self.room_group_name = 'test_consumer_group'

        await(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )

        await self.accept()
        await self.send(text_data=json.dumps({'status': 'connetced'}))


    async def receive(self, text_data):
        self.send(text_data=json.dumps({'status': 'we received data!'}))

    async def disconnect(self):
        pass
    
    async def send_notifications(self, event):
        data = json.loads(event.get('data'))
        await self.send(text_data=json.dumps({'notification': data}))