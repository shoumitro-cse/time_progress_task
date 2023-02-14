from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import asyncio
import time


def progress_scheduled_create(group_name, json_data):
	task_time = int(json_data["task_time"])
	for item in range(1, task_time+1):
		async_to_sync(get_channel_layer().group_send)(group_name, {
			"type": "send_message",
			'progress_data': (100 * item) / task_time,
			'progress_id': json_data["progress_id"],
		})
		time.sleep(1)
	return None


@shared_task
def task_1(group_name, json_data):
	progress_scheduled_create(group_name, json_data)


@shared_task
def task_2(group_name, json_data):
	progress_scheduled_create(group_name, json_data)


@shared_task
def task_3(group_name, json_data):
	progress_scheduled_create(group_name, json_data)

# @shared_task
# async def progress_scheduled_create(group_name, json_data):
# 	for item in range(1, int(json_data["task_time"])):
# 		from channels.layers import get_channel_layer
# 		await get_channel_layer().group_send(group_name, {
# 			"type": "send_message",
# 			'progress_data': item,
# 		})
# 		print("hello")
# 		# await asyncio.sleep(1)





