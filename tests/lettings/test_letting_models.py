"""test letting models"""
import pytest
from django.test import TestCase

from lettings.models import Letting


class LettingsModelsTestCase(TestCase):
    @pytest.fixture(autouse=True)
    def prepare_fixture(self, myaddress):
        self.myaddress = myaddress

    def test_address_model(self):
        """test an instance of Address model"""
        expected_value = "100 My street"
        assert str(self.myaddress) == expected_value

    def test_letting_model(self):
        """test an instance of letting model"""
        letting = Letting.objects.create(title="My letting", address=self.myaddress)
        expected_value = "My letting"
        assert str(letting) == expected_value
