from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Advocate, Company

# Create your tests here.
class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.company = Company.objects.create(name="Google", bio="Best tech company in the world")
        cls.advocate = Advocate.objects.create(
            company=cls.company, username="Test User", bio="I am a junior django developer"
        )

    
    def test_advocate_model_content(self):
        self.assertEqual(self.advocate.username, "Test User")
        self.assertEqual(self.advocate.bio, "I am a junior django developer")
        self.assertEqual(self.advocate.company, self.company)
        self.assertEqual(str(self.advocate), "Test User")


    def test_company_model_content(self):
        self.assertEqual(self.company.name, "Google")
        self.assertEqual(self.company.bio, "Best tech company in the world")
        self.assertEqual(self.company.advocate_set.count(), 1)
        self.assertEqual(str(self.company), "Google")


    def test_advocate_list_view(self):
        response = self.client.get(reverse("base:advocate_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Advocate.objects.count(), 1)
        self.assertContains(response, self.advocate)


    def test_advocate_detail_view(self):
        response = self.client.get(reverse("base:advocate_detail", kwargs={"pk": self.advocate.id}), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "I am a junior django developer")

    
    def test_company_list_view(self):
        response = self.client.get(reverse("base:company_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Company.objects.count(), 1)
        self.assertContains(response, self.company)


    def test_company_detail_view(self):
        response = self.client.get(reverse("base:company_detail", kwargs={"pk": self.company.id}), format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, "Best tech company in the world")

