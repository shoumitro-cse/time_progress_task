### Time progress bar app

A simple Django application where there are three tasks which takes 50, 100 and 120 seconds* to complete respectively.
Users can start any task from the UI and can see the status of the task in the progress bar.

Note : Here, we have used Django Channel, Celery, RabbitMQ/Redis and Docker.

### Installation

```
# Python version 3.11
git clone https://github.com/shoumitro-cse/time_progress_task.git
cd time_progress_task
cp env.example .env
sed -i -e 's/host.docker.internal/0.0.0.0/g' .env
python -m venv venv
source ./venv/bin/activate
pip install -r requirments.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic
rm -rf static
mv staticfiles static
python manage.py runserver

# Another terminal
docker run --restart always --name redis_container -p 6379:6379 -d redis
celery -A time_progress_task worker -l info -c 4 \
 -Q progress_one_queue,progress_two_queue,progress_three_queue --autoscale 1,10
```

### Docker Installation
```
docker run --restart always --name redis_container -p 6379:6379 -d redis
docker-compose up --build -d
```

### Celery worker & queue

```
sudo docker run --restart always --name redis_container -p 6379:6379 -d redis

celery -A time_progress_task worker --help


# same worker and multiple queue, here c=4, will have four child process of a each queue
celery -A time_progress_task worker -l info -c 4 -n my_worker -Q queue1,queue2,queue3


# worker auto scale 1 to 10
celery -A time_progress_task worker -l info -c 4 -Q queue1,queue2,queue3 --autoscale 1,10


# multiple worker and multiple queue
celery -A time_progress_task worker -l info  -c 1 -n my_worker1 -Q queue1
celery -A time_progress_task worker -l info  -c 1 -n my_worker2 -Q queue2
celery -A time_progress_task worker -l info  -c 1 -n my_worker3 -Q queue3
    
```

### Progress bar UI

![](https://github.com/shoumitro-cse/time_progress_task/blob/main/images/progress_ui.png?raw=true)

