from rest_framework import serializers

from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = (
            'id',
            'position',
            'package_id',
            'name',
            'name_translated',
            'state',
            'datastore_active',
            'hash',
            'description',
            'format',
            'mimetype',
            'mimetype_inner',
            'language',
            'url',
            'url_type',
            'data_quality',
            'revision_id',
            'cache_url',
            'cache_last_updated',
            'resource_type',
            'created',
            'last_modified',
        )

