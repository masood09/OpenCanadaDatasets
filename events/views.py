import requests, json

from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets

from .serializers import EventSerializer
from .models import Event

def refresh(request, uuid):
    Event.objects.all().delete()

    source_url = 'https://open.canada.ca/data/api/action/package_show?id=' + str(uuid)

    response = requests.get(source_url)

    if response.status_code != 200:
        try:
            data = json.loads(response.text)
            return JsonResponse(data, status=response.status_code)
        except Exception as e:
            print(e)
            return HttpResponse(response.text, response.status_code)

    errors = []

    try:
        data = json.loads(response.text)

        if ('result' in data) and ('resources' in data['result']):
            resources = data['result']['resources']

            for resource in resources:
                serializer = EventSerializer(data=resource)

                if (serializer.is_valid()):
                    serializer.save()
                else:
                    errors.append(serializer.errors)

            if len(errors) == 0:
                events = Event.objects.all()
                serializer = EventSerializer(events, many=True)
                return JsonResponse(serializer.data, status=201, safe=False)
        else:
            errors.append("Not able to parse the data")
    except Exception as e:
        errors.append(e)

    return JsonResponse(errors, status=400, safe=False)



class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

