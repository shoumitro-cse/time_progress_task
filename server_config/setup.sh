if [ ! -d "./static" ] 
then
    python manage.py collectstatic
	rm -rf static
	mv staticfiles static
    echo "static directory created." 
fi

#python manage.py runserver localhost:8000

nginx
celery -A time_progress_task worker -l info -c 4 -Q progress_one_queue,progress_two_queue,progress_three_queue --autoscale 1,10 &
gunicorn -b 127.0.0.1:7001  time_progress_task.wsgi --reload &
daphne -b 127.0.0.1 -p 7002 time_progress_task.asgi:application 



