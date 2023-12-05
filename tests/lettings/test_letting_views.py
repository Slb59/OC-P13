"""test letting views"""
import pytest
from django.test import TestCase
# from django.urls import reverse
# from pytest_django.asserts import assertTemplateUsed

# from lettings.models import Letting


class LettingsViewsTestCase(TestCase):
    @pytest.fixture(autouse=True)
    def prepare_fixture(self, myaddress):
        self.myaddress = myaddress

    def setUp(self):
        """setup an instance of address"""
        self.address = self.myaddress

    # def test_letting_index_view(self):
    #     """test index view"""
    #     Letting.objects.create(title="My letting", address=self.address)
    #     path = reverse("lettings:index")
    #     response = self.client.get(path)
    #     expected_content = (
    #         '<h1 class="page-header-ui-title mb-3 display-6">Lettings</h1>'
    #     )
    #     self.assertContains(response, expected_content, status_code=200)
    #     assertTemplateUsed(response, "lettings/index.html")

    # def test_letting_view(self):
    #     """test letting view"""
    #     letting = Letting.objects.create(title="My letting", address=self.address)
    #     path = reverse("lettings:letting", args=[1])
    #     response = self.client.get(path)
    #     expected_content = '<h1 class="page-header-ui-title mb-3 display-6">'
    #     expected_content += letting.title + "</h1>"
    #     self.assertContains(response, expected_content, status_code=200)
    #     assertTemplateUsed(response, "lettings/letting.html")

    # def test_letting_404_view(self):
    #     """test page 404"""
    #     path = reverse("lettings:letting", args=[0])
    #     response = self.client.get(path)
    #     expected_content = "<h1>Page not found</h1>"
    #     self.assertContains(response, expected_content, status_code=404)
    #     assertTemplateUsed(response, "base/404.html")

    # def test_letting_noletting_view(self):
    #     """test no letting view"""
    #     path = reverse("lettings:index")
    #     response = self.client.get(path)
    #     expected_content = "<p>No lettings are available.</p>"
    #     self.assertContains(response, expected_content, status_code=200)
    #     assertTemplateUsed(response, "lettings/index.html")
