# Stage 1
FROM python:3.10-slim as base

ENV PYTHONUNBUFFERED 1

RUN apt-get update

ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

ADD . /app
WORKDIR /app

ARG BUILD_DATE
ARG REVISION
ARG VERSION
# LABEL maintainer "marianovaldez92@gmail.com"
# LABEL created $BUILD_DATE
# LABEL url "https://reflej.ar"
# LABEL source "git@github.com:reflejar/pis.git"
# LABEL version $VERSION
# LABEL revision $REVISION
# LABEL vendor "Reflejar"
# LABEL title "Pesticidas introducidos silenciosamente"
# LABEL description "Democracia en Red"

EXPOSE 8050