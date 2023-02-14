from django.urls import path
from myapp import views

app_name = 'myapp'

urlpatterns = [
    path('progress-bar/', views.progress_view, name='progress_bar_url'),
]
