FROM python:3.11

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update
RUN apt-get install -y iputils-ping apt-utils nano  nginx
       
WORKDIR /progress_app

COPY requirments.txt /progress_app/requirments.txt
RUN pip install -r requirments.txt

COPY ./server_config/nginx.conf /etc/nginx/sites-available/progress_bar_server
RUN ln -s /etc/nginx/sites-available/progress_bar_server /etc/nginx/sites-enabled
COPY . /progress_app

ENTRYPOINT ["/bin/bash", "server_config/setup.sh"]

