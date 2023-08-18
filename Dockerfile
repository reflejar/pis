FROM nginx as web
ARG BUILD_DATE
ARG REVISION
ARG VERSION
LABEL created $BUILD_DATE
LABEL version $VERSION
LABEL revision $REVISION
LABEL maintainer "marianovaldez92@protonmail.com"
LABEL url "https://pis.org.ar"
LABEL title "PIS web"
LABEL description "Pagina web del proyecto PIS"
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY . /usr/share/nginx/html
EXPOSE 80