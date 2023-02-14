from django.urls import re_path, path
from . import consumers


websocket_urlpatterns = [
    path('ws/progress/data/', consumers.ProgressConsumer.as_asgi()),

]
