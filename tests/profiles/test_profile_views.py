"""test profiles views"""
from django.contrib.auth.models import User
# from django.core.cache import cache
from django.test import TestCase
# from django.urls import reverse
# from pytest_django.asserts import assertTemplateUsed

# from profiles.models import Profile


class ProfilesViewsTestCase(TestCase):
    def setUp(self):
        """setup a new user"""
        self.user = User.objects.create(username="test_user_name")

    # def test_profile_index_view(self):
    #     """test profile index view"""
    #     Profile.objects.create(user=self.user, favorite_city="My favorite city")
    #     path = reverse("profiles:index")
    #     response = self.client.get(path)
    #     expected_content = (
    #         '<h1 class="page-header-ui-title mb-3 display-6">Profiles</h1>'
    #     )
    #     self.assertContains(response, expected_content, status_code=200)
    #     assertTemplateUsed(response, "profiles/index.html")

    # def test_profile_view(self):
    #     """test profile view"""
    #     profile = Profile.objects.create(
    #         user=self.user, favorite_city="My favorite city"
    #     )
    #     path = reverse("profiles:profile", args=[profile.user.username])
    #     response = self.client.get(path)
    #     expected_content = '<h1 class="page-header-ui-title mb-3 display-6">'
    #     expected_content += self.user.username + "</h1>"
    #     self.assertContains(response, expected_content, status_code=200)
    #     assertTemplateUsed(response, "profiles/profile.html")

    # def test_profile_404_view(self):
    #     """test 404 view"""
    #     path = reverse("profiles:profile", args=["inconnu"])
    #     response = self.client.get(path)
    #     expected_content = "<h1>Page not found</h1>"
    #     self.assertContains(response, expected_content, status_code=404)
    #     assertTemplateUsed(response, "base/404.html")

    # def test_profile_noprofile_view(self):
    #     """test no profile found"""
    #     cache.clear()
    #     path = reverse("profiles:index")
    #     response = self.client.get(path)
    #     expected_content = "<p>No profiles are available.</p>"
    #     self.assertContains(response, expected_content, status_code=200)
    #     assertTemplateUsed(response, "profiles/index.html")
