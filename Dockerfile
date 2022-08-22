FROM python:3.7-alpine3.13

ADD requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

ADD . /app

WORKDIR /app

EXPOSE 8050