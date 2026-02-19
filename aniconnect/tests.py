from django.test import TestCase
from django.db import connections
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

# Create your tests here.

class DatabaseConnectionTest(SimpleTestCase):
    """Sanity check that the configured default DB accepts connections."""

    databases = {"default"}

    def test_default_database_connection(self):
        connection = connections["default"]
        connection.ensure_connection()

        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()

        self.assertEqual(result[0], 1)


class SmokeTest(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)