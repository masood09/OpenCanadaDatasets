from django.test import TestCase

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

