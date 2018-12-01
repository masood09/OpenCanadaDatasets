FROM python:3.7-alpine

MAINTAINER Masood Ahmed "masood.ahmed09@gmail.com"

EXPOSE 8000

ENV HOME /root
ENV APP_HOME /application/

WORKDIR $APP_HOME

ADD . $APP_HOME

CMD ["tail", "-f", "/dev/null"]

