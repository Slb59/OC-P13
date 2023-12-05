"""test letting urls"""
import pytest
from django.test import TestCase
# from django.urls import resolve, reverse

from lettings.models import Letting


class LettingsUrlsTestCase(TestCase):
    @pytest.fixture(autouse=True)
    def prepare_fixture(self, myaddress):
        self.myaddress = myaddress

    def setUp(self):
        """setup an instance of letting and address"""
        self.address = self.myaddress
        self.letting = Letting.objects.create(title="My letting", address=self.address)

    # def test_letting_index_url(self):
    #     """test index url"""
    #     path = reverse("lettings:index")
    #     assert path == "/lettings/"
    #     assert resolve(path).view_name == "lettings:index"

    # def test_letting_url(self):
    #     """test first letting url"""
    #     path = reverse("lettings:letting", args=[1])
    #     assert path == "/lettings/1/"
    #     assert resolve(path).view_name == "lettings:letting"
