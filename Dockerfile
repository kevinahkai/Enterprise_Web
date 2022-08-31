FROM python:3.8-slim-buster

RUN apt-get update
RUN apt-get install vim -y
RUN pip3 install django
RUN apt-get install python3-dev default-libmysqlclient-dev build-essential -y
RUN pip3 install mysqlclient==2.0.3

RUN django-admin startproject app
WORKDIR /app

CMD python manage.py runserver 0.0.0.0:8000
