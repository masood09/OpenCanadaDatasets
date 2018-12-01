
# OpenCanadaDatasets

# Introduction

OpenCanadaDatasets is a simple Django application. This application can be used to pull datasets from Open Canada Datasets.

# Issues

OpenCanadaDatasets was written in a very short period of time, literally in few hours. Although it has been tested on many different Python versions, database engines and Django versions, I would recommend you have the latest version of Python, Django and other dependencies to avoid any nasty surprises.

# Prerequisites

The following are the software requirements to run OpenCanadaDatasets.

* Docker

# Installation

The documentation is written from OS X/Linux user perspective. Most of the commands should work on a Windows box, but I give no guarantee. Please google or drop me an email if you are stuck.

```bash
git clone https://github.com/masood09/OpenCanadaDatasets.git
cd OpenCanadaDatasets
docker-compose up -d
```

To install all the dependencies for this project, execute the following command from the OpenCanadaDatasets directory

```bash
docker-compose exec application pip install -r requirements.txt
```

To complete the installation of this project, please follow the below instructions

```bash
docker-compose exec application python manage.py migrate
```

To test the application and gather coverage information execute the following commands

```bash
docker-compose exec application coverage run manage.py test
docker-compose exec application coverage -m
```

Phew!!

Now we are ready to fire up the server and see how the application works

```
docker-compose exec application python manage.py runserver 0:8000
```

The application would be listening on 8000 of localhost [http://127.0.0.1:8000](http://127.0.0.1:8000)


# API's

The following API's are provided:

#### Refresh API
This API will refresh the data in our database with datasets from the UUID specified in the URL.

Example: [http://localhost:8000/api/v1/events/refresh/fd3355a7-ae34-4df7-b477-07306182db69/](http://localhost:8000/api/v1/events/refresh/fd3355a7-ae34-4df7-b477-07306182db69/)


#### GET Events
This API will fetch all the events in our database

Example: [http://localhost/api/v1/events/](http://localhost/api/v1/events/)


#### GET a single event
This API will fetch a single event

Example: [http://localhost/api/v1/events/aeb4a545-a861-4785-9611-c2899902b2c3/](http://localhost/api/v1/events/aeb4a545-a861-4785-9611-c2899902b2c3/)

#### Create an event
This API will create an event. The API expects the content to be in body of request as JSON. The JSON schema needs to be same as GET a single event API response.

Example: [POST to http://localhost/api/v1/events/](http://localhost/api/v1/events/)


#### UPDATE an event
This API will update an event. The API expects the content to be in body of request as JSON. The JSON schema needs to be same as GET a single event API response.

Example: [PUT to http://localhost/api/v1/events/aeb4a545-a861-4785-9611-c2899902b2c3/](http://localhost/api/v1/events/aeb4a545-a861-4785-9611-c2899902b2c3/)


#### DELETE an event
This API will delete an event.

Example [DELETE to http://localhost/api/v1/events/aeb4a545-a861-4785-9611-c2899902b2c3/](http://localhost/api/v1/events/aeb4a545-a861-4785-9611-c2899902b2c3/)


You can over-ride any settings of the application by creating **local_settings.py** file in Gale/config file. Any settings defined thier would over-ride the settings specified in settings.py file.

