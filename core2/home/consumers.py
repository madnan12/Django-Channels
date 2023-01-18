from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class TestConsumer(WebsocketConsumer):

    def connect(self):
        self.room_name = 'test_consumer'
        self.room_group_name = 'test_consumer_group'

        async_to_sync(self.channel_layer.group_add)(
            self.room_name, self.room_group_name
        )

        self.accept()
        self.send(text_data=json.dumps({'status': 'connetced'}))


    def receive(self, text_data=None, bytes_data=None):
        # # Called with either text_data or bytes_data for each frame
        # # You can call:
        # self.send(text_data="Hello world!")
        # # Or, to send a binary frame:
        # self.send(bytes_data="Hello world!")
        # # Want to force-close the connection? Call:
        # self.close()
        # # Or add a custom WebSocket error code!
        # self.close(code=4123)
        pass

    def disconnect(self, close_code):
        # Called when the socket closes
        pass