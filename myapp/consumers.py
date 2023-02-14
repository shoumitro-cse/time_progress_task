from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer
from myapp.tasks import progress_scheduled_create, task_1, task_2, task_3
import json
from time_progress_task import celery_app


class ProgressConsumer(JsonWebsocketConsumer):

    def connect(self):
        self.group_name = 'progress_group'
        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        self.channel_layer.group_discard(self.group_name, self.channel_name)

    # celery -A time_progress_task worker -l info  -c 1 -n my_worker1 -Q queue1
    # celery -A time_progress_task worker -l info  -c 1 -n my_worker2 -Q queue2
    # celery -A time_progress_task worker -l info  -c 1 -n my_worker3 -Q queue3
    def receive(self, text_data):
        json_data = json.loads(text_data)
        if json_data["progress_id"] == 'progress_one':
            celery_app.send_task('myapp.tasks.task_1', args=[self.group_name, json_data], kwargs={}, queue='queue1')
            # task_1.apply_async((self.group_name, json_data))
        elif json_data["progress_id"] == 'progress_two':
            celery_app.send_task('myapp.tasks.task_2', args=[self.group_name, json_data], kwargs={}, queue='queue2')
            # task_2.apply_async((self.group_name, json_data))

        else:
            celery_app.send_task('myapp.tasks.task_3', args=[self.group_name, json_data], kwargs={}, queue='queue3')
            # task_3.apply_async((self.group_name, json_data))

    def send_message(self, event):
        del event['type']
        self.send_json(event)


