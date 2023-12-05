"""test profiles urls"""
from django.contrib.auth.models import User
from django.test import TestCase
# from django.urls import resolve, reverse

# from profiles.models import Profile


class ProfilesUrlsTestCase(TestCase):
    def setUp(self):
        """setup a new user"""
        self.user = User.objects.create(username="test_user_name")

    # def test_profile_index_url(self):
    #     """test profile index url"""
    #     Profile.objects.create(user=self.user, favorite_city="My favorite city")
    #     path = reverse("profiles:index")

    #     assert path == "/profiles/"
    #     assert resolve(path).view_name == "profiles:index"

    # def test_profile_url(self):
    #     """test a profile url"""
    #     profile = Profile.objects.create(
    #         user=self.user, favorite_city="My favorite city"
    #     )
    #     path = reverse("profiles:profile", args=[profile.user.username])
    #     assert path == "/profiles/test_user_name/"
    #     assert resolve(path).view_name == "profiles:profile"
