FROM python:3.6


WORKDIR /srv/www/web-report
COPY . .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DOCKER_ENV 1

COPY Pipfile Pipfile.lock ./

RUN echo 'Hi, I am in your container'
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --dev --system --deploy
#RUN pip install pipenv
#RUN pipenv install --system --deploy
#RUN psql simple_site_with_tests < gims_db.sql
#RUN python manage.py runserver 127.0.0.1:8000
#RUN echo 'Hi, I am in your container 2'
