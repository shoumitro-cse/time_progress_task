import redis
from django.conf import settings

rd = redis.Redis(host=settings.REDIS_HOST, port=6379, db=1)


def set_progress_id(progress_id):
    rd.mset({progress_id: 'True'})


def get_progress_id(progress_id):
    return rd.get(progress_id)


def remove_progress_id(progress_id):
    rd.delete(progress_id)
