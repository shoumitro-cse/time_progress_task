from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import time, asyncio
from time_progress_task import redis_conn


@shared_task
def progress_scheduled_create(group_name, json_data):
    total_task_time = int(json_data["task_time"])
    for second in range(1, total_task_time + 1):
        event_loop = asyncio.get_event_loop()
        coroutine_obj = get_channel_layer().group_send(group_name, {
                "type": "send_message",
                'progress_data': (100 * second) / total_task_time,
                'progress_id': json_data["progress_id"],
            })
        event_loop.run_until_complete(coroutine_obj)
        time.sleep(1)
    redis_conn.remove_progress_id(json_data["progress_id"])
    return None
