from django.contrib.auth.models import User
from django.test import TestCase
from django.test import Client


class TestCaseAdminLogin(TestCase):
    """Test case with client and login as admin function."""
    admin_password = '38dsiha49sd'

    @classmethod
    def setUpTestData(cls):
        User.objects.create_superuser(username='admin', email='admin@test.com', password=cls.admin_password)

    def setUp(self):
        self.client = Client()
        self.login()

    def login(self):
        """Login as admin."""
        success = self.client.login(username='admin', password=self.admin_password)
        self.assertTrue(success)
        response = self.client.get('/admin/', follow=True)
        self.assertEqual(response.status_code, 200)
        return response


class TestAdminPages(TestCaseAdminLogin):

    def test_admin_homepage(self):
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)
