from django.test import TestCase
from django.urls import reverse
from django.core.exceptions import ValidationError
from lettings.models import Address, Letting


# -----------------------------
# Tests pour Address
# -----------------------------
class AddressModelTest(TestCase):
    def test_create_valid_address(self):
        address = Address.objects.create(
            number=123,
            street="Main Street",
            city="Paris",
            state="FR",
            zip_code=75000,
            country_iso_code="FRA"
        )
        self.assertEqual(str(address), "123 Main Street")
        self.assertEqual(address._meta.verbose_name, "Adress")
        self.assertEqual(address._meta.verbose_name_plural, "Adresses")

    def test_invalid_zip_code(self):
        address = Address(
            number=1,
            street="Rue Test",
            city="Lyon",
            state="FR",
            zip_code=123456,  # Trop grand (> 99999)
            country_iso_code="FRA"
        )
        with self.assertRaises(ValidationError):
            address.full_clean()  # force la validation


# -----------------------------
# Tests pour Letting
# -----------------------------
class LettingModelTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=10,
            street="Rue Victor Hugo",
            city="Marseille",
            state="FR",
            zip_code=13000,
            country_iso_code="FRA"
        )

    def test_create_letting(self):
        letting = Letting.objects.create(title="Super Appart", address=self.address)
        self.assertEqual(str(letting), "Super Appart")
        self.assertEqual(letting.address.city, "Marseille")


# -----------------------------
# Tests pour les vues
# -----------------------------
class ViewsTest(TestCase):
    def setUp(self):
        self.address = Address.objects.create(
            number=99,
            street="Boulevard Voltaire",
            city="Paris",
            state="FR",
            zip_code=75011,
            country_iso_code="FRA"
        )
        self.letting = Letting.objects.create(title="Bel appartement", address=self.address)

    def test_index_view(self):
        response = self.client.get(reverse("lettings_index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/index.html")
        self.assertContains(response, "Bel appartement")

    def test_index_view_lettings_list_not_empty(self):
        response = self.client.get(reverse("lettings_index"))
        lettings_list = response.context["lettings_list"]
        self.assertTrue(len(lettings_list) > 0)
        self.assertIn(self.letting, lettings_list)

    def test_index_view_lettings_list_empty(self):
        Letting.objects.all().delete()
        response = self.client.get(reverse("lettings_index"))
        lettings_list = response.context["lettings_list"]
        self.assertEqual(len(lettings_list), 0)

    def test_letting_view_success(self):
        url = reverse("lettings:letting", args=[self.letting.pk])  # pk au lieu de id
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/letting.html")

        # Vérifie le contexte
        self.assertEqual(response.context["title"], "Bel appartement")
        self.assertEqual(response.context["address"], self.address)

        # Vérifie le rendu HTML
        self.assertContains(response, "Bel appartement")
        self.assertContains(response, "99 Boulevard Voltaire")
        self.assertContains(response, "Paris, FR 75011")
        self.assertContains(response, "FRA")

    def test_letting_view_not_found(self):
        url = reverse("lettings:letting", args=[999])  # id inexistant
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
