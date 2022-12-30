FROM python:3.9

COPY . /srv/www/web-report
WORKDIR /srv/www/web-report

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
#ENV DOCKER_ENV 1

#COPY Pipfile Pipfile.lock ./

RUN echo 'Hi, I am in your container'
RUN python -m pip install --upgrade pip
RUN pip install pipenv && pipenv install --dev --system --deploy