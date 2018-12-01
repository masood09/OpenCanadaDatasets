from django.test import TestCase

from .models import Event

class ResponseCodeTest(TestCase):
    """The unit test cases for checking the correct response codes for various URL's"""

    def test_refresh_api_valid_uuid(self):
        """When the Refresh API is passed with valid UUID, the response code should be 201"""
        response = self.client.get("/api/v1/refresh/fd3355a7-ae34-4df7-b477-07306182db69/")
        self.assertEquals(response.status_code, 201)

    def test_refresh_api_invalid_uuid(self):
        """When the Refresh API is passed with invalid UUID, the response code should be 404"""
        response = self.client.get("/api/v1/fd3355a7-ae34-4df7-b477-07306182db6/")
        self.assertEquals(response.status_code, 404)

class EventModelTest(TestCase):
    """The unit test cases for Event Model"""

    fixtures = ["fixtures.json"]

    def test_category_name_plural(self):
        """Test whether the plural name is correct"""
        self.assertEquals(str(Event._meta.verbose_name_plural), "events")

    def test_string_representation(self):
        """Test whether the string representation is equal to its name"""
        event = Event.objects.get(pk="aeb4a545-a861-4785-9611-c2899902b2c3")
        self.assertEquals(str(event), event.name)

