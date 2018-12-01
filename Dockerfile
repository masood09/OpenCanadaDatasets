FROM python:3.7-alpine

MAINTAINER Masood Ahmed "masood.ahmed09@gmail.com"

EXPOSE 8000

ENV HOME /root
ENV APP_HOME /application/

WORKDIR $APP_HOME

# Install required packages
RUN apk update
RUN apk add postgresql-libs
RUN apk add --virtual .build-deps gcc musl-dev postgresql-dev

# Add requirements files first (helpful for docker cache)
ADD ./requirements.txt $APP_HOME
RUN mkdir $APP_HOME/requirements
ADD ./requirements/* $APP_HOME/requirements/

# Install requirements
RUN pip install -r requirements.txt

# Remove no longer necessary packages
RUN apk --purge del .build-deps

# Remove the requirements files
RUN rm -rf requirements
RUN rm -rf requirements.txt

ADD . $APP_HOME

CMD ["tail", "-f", "/dev/null"]

