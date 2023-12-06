"""test profile models"""
from django.contrib.auth.models import User
from django.test import TestCase

from profiles.models import Profile


class ProfilesModelsTestCase(TestCase):
    def test_profile_model(self):
        """test an instance of profile model"""
        user = User.objects.create(username="test_user_name")
        profile = Profile.objects.create(user=user, favorite_city="My favorite city")
        expected_value = "test_user_name"
        # assert False
        assert str(profile) == expected_value
