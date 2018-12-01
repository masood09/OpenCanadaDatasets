import uuid

from django.db import models
from django.contrib.postgres.fields import JSONField, ArrayField

class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    position = models.PositiveIntegerField(default=0)
    package_id = models.UUIDField(blank=True, null=True)
    name = models.CharField(max_length=200)
    name_translated = JSONField(blank=True, null=True)
    state = models.CharField(max_length=20)
    datastore_active = models.BooleanField(default=False)
    hash = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    format = models.CharField(blank=True, max_length=20)
    mimetype = models.CharField(blank=True, null=True, max_length=20)
    mimetype_inner = models.CharField(blank=True, null=True, max_length=20)
    language = ArrayField(models.CharField(max_length=10), null=True)
    url = models.URLField(max_length=250)
    url_type = models.CharField(blank=True, null=True, max_length=20)
    data_quality = ArrayField(models.CharField(max_length=200), null=True)
    revision_id = models.UUIDField(blank=True, null=True)
    cache_url = models.URLField(blank=True, null=True)
    cache_last_updated = models.DateTimeField(blank=True, null=True)
    resource_type = models.CharField(blank=True, null=True, max_length=250)
    created = models.DateTimeField()
    last_modified = models.DateTimeField(blank=True, null=True)

