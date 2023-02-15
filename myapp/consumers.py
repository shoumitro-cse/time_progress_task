from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer
import json
from time_progress_task import celery_app


class ProgressConsumer(JsonWebsocketConsumer):

    def connect(self):
        self.group_name = 'progress_group'
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        self.channel_layer.group_discard(self.group_name, self.channel_name)

    def receive(self, text_data):
        json_data = json.loads(text_data)
        celery_app.send_task('myapp.tasks.progress_scheduled_create', args=[self.group_name, json_data],
                             kwargs={}, queue=json_data["progress_id"]+'_queue')

    def send_message(self, event):
        del event['type']
        self.send_json(event)


