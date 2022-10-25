# pull official base image
FROM python:3.9-alpine

RUN mkdir /usr/src/app

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev curl

# for wait other containers
ADD     https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait ./wait
RUN     chmod +x ./wait

# install dependencies
RUN pip3 install pip --upgrade
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .