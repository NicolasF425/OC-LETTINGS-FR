from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from profiles.models import Profile


# -----------------------------
# Tests pour le modèle Profile
# -----------------------------
class ProfileModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="alice", password="password123")

    def test_create_profile(self):
        profile = Profile.objects.create(user=self.user, favorite_city="Paris")
        self.assertEqual(str(profile), "alice")
        self.assertEqual(profile.favorite_city, "Paris")

    def test_profile_without_favorite_city(self):
        profile = Profile.objects.create(user=self.user)
        self.assertEqual(profile.favorite_city, "")


# -----------------------------
# Tests pour les vues profiles
# -----------------------------
class ProfilesViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="alice", password="password123")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Paris")

    def test_profile_view_success(self):
        url = reverse("profiles:profile", args=[self.user.username])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")
        self.assertContains(response, "alice")
        self.assertContains(response, "Paris")

    def test_profile_view_not_found(self):
        url = reverse("profiles:profile", args=["inexistant"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
