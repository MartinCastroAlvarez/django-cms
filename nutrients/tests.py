"""
In computer programming, unit testing is a software testing
method by which individual units of source code—sets of one
or more computer program modules together with associated control
data, usage procedures, and operating procedures—are tested
to determine whether they are fit for use.
"""

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from nutrients.views import nutrient_list_view
from nutrients.models import Nutrient, Unit


class NutrientsViewsTest(TestCase):
    """
    Class responsible for testing Nutrients Views.
    """

    def setUp(self) -> None:
        """
        Initializing Test User.
        """
        self.user: User = User.objects.get_or_create(username='testuser')[0]

    def test_auth_required(self) -> None:
        """
        Test that Nutrients are private.
        """
        client: Client = Client()
        response = client.get(reverse('nutrients.list'))
        self.assertEquals(response.status_code, 302)

    def test_list_nutrients(self) -> None:
        """
        Test that the User can list Nutrients.
        """
        Nutrient(name="test-nutrient-1", unit=Unit.GRAM.value).save()
        Nutrient(name="test-nutrient-2", unit=Unit.GRAM.value).save()
        client: Client = Client()
        client.force_login(self.user)
        response = client.get(reverse('nutrients.list'))
        self.assertEquals(response.status_code, 200)
        self.assertIn("test-nutrient-1", response.content.decode('utf-8'))
        self.assertIn("test-nutrient-2", response.content.decode('utf-8'))

    def test_search_nutrients_by_name(self) -> None:
        """
        Test that the User can search Nutrients by name.
        """
        Nutrient(name="nutrient-test-1", unit=Unit.GRAM.value).save()
        Nutrient(name="nutrient-test-2", unit=Unit.GRAM.value).save()
        client: Client = Client()
        client.force_login(self.user)
        response = client.get(reverse('nutrients.list') + "?name=" + "-test-2")
        self.assertEquals(response.status_code, 200)
        self.assertNotIn("nutrient-test-1", response.content.decode('utf-8'))
        self.assertIn("nutrient-test-2", response.content.decode('utf-8'))
