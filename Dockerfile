FROM python:3.8

COPY . /srv/www/web-report
WORKDIR /srv/www/web-report

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DOCKER_ENV 1

RUN echo 'Hi, I am in your container'
RUN pip install pipenv
RUN pipenv install --system --deploy
#RUN psql simple_site_with_tests < gims_db.sql
#RUN python manage.py runserver 127.0.0.1:8000
#RUN echo 'Hi, I am in your container 2'
