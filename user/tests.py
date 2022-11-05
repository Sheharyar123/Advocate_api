from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class CustomUserTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.admin_user = get_user_model().objects.create_superuser(
            username="Admin User",
            email="adminuser@email.com",
            password="9a8b7c6d",
            name="admin",
        )
        cls.test_user = get_user_model().objects.create_user(
            username="Test User",
            email="testuser@email.com",
            password="9a8b7c6d",
            name="test",
        )

    def test_simple_user(self):
        self.assertEqual(self.test_user.username, "Test User")
        self.assertEqual(self.test_user.email, "testuser@email.com")
        self.assertEqual(self.test_user.name, "test")
        self.assertTrue(self.test_user.is_active)
        self.assertFalse(self.test_user.is_superuser)
        self.assertFalse(self.test_user.is_staff)

    def test_admin_user(self):
        self.assertEqual(self.admin_user.username, "Admin User")
        self.assertEqual(self.admin_user.email, "adminuser@email.com")
        self.assertEqual(self.admin_user.name, "admin")
        self.assertTrue(self.admin_user.is_active)
        self.assertTrue(self.admin_user.is_superuser)
        self.assertTrue(self.admin_user.is_staff)
