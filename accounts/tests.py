"""Contains the tests of accounts app."""

# json
import json

# django
from django.urls import path, include, reverse

# rest_framework
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase, APIClient

# models
from accounts.models import User


class UserTest(APITestCase, URLPatternsTestCase):
    """Test module for User."""

    urlpatterns = [
        path('api/', include("accounts.urls")),
    ]

    def setUp(self):
        """Overrides method in TestCase."""
        self.admin = User.objects.create_superuser(
            username='admin',
            email='admin@test.com',
            password='Admin74940',
            role=1,
        )

        self.user_sales = User.objects.create_user(
            username='sales',
            email='sales@test.com',
            password='Sales74940',
            role=2
        )

        self.support = User.objects.create_user(
            username='support',
            email='support@test.com',
            password='Support74940',
            role=3,
        )

    def test_login(self):
        """Test if a user can login and get a JWT response token."""
        url = reverse('login')
        data = {
            'username': 'admin',
            'password': 'Admin74940'
        }
        response = self.client.post(url, data)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in response_data)

    def test_login_denied(self):
        """Test if a user tries to connect with the wrong username or password."""
        url = reverse('login')
        data = {
            'username': 'foo',
            'password': 'Foo74940'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_all_users(self):
        """Test fetching all users."""
        # Setup the token
        url = reverse('login')
        data = {'username': 'sales', 'password': 'Sales74940'}
        response = self.client.post(url, data)
        login_response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in login_response_data)
        token = login_response_data['access']

        # Test the endpoint
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = client.get(reverse('users'))
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), len(response_data))

    def test_access_denied_all_users_no_authenticated(self):
        """Test fetching all users. Restricted to IsAuthenticated."""
        # Test the endpoint
        client = APIClient()
        response = client.get(reverse('users'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_one_user(self):
        """Test fetching one user."""
        # Setup the token
        url = reverse('login')
        data = {'username': 'sales', 'password': 'Sales74940'}
        response = self.client.post(url, data)
        login_response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in login_response_data)
        token = login_response_data['access']

        # Test the endpoint
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = client.get(reverse('user', kwargs={'pk': self.admin.id}))
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data['username'], self.admin.username)
