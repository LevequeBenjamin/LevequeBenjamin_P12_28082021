"""Contains the tests of clients app."""

# json
import json

# django
from django.urls import path, include, reverse

# rest_framework
from rest_framework import status
from rest_framework.test import APITestCase, URLPatternsTestCase, APIClient

# models
from accounts.models import User
from clients.models import Client


class ClientTest(APITestCase, URLPatternsTestCase):
    """Test module for Client."""

    urlpatterns = [
        path('api/', include('accounts.urls')),
        path('api/', include("clients.urls")),
    ]

    def setUp(self):
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

        self.user_sales2 = User.objects.create_user(
            username='sales2',
            email='sales2@test.com',
            password='Sales274940',
            role=2
        )

        self.support = User.objects.create_user(
            username='support',
            email='support@test.com',
            password='Support74940',
            role=3,
        )

        self.client1 = Client(
            first_name='client1',
            last_name='client1',
            email='client1@test.com',
            phone='0450768549',
            mobile='0620498566',
            company_name='company1',
            sales_contact=self.user_sales,
        )

        self.client1.save()

    def test_create_client(self):
        """Test if a sales user can create a client."""
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
        data = {
            'first_name': 'client2',
            'last_name': 'client2',
            'email': 'client2@test.com',
            'phone': '0450654488',
            'mobile': '0450499044',
            'company_name': 'company1',
        }
        response = client.post(reverse('list_create_client'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_access_denied_create_client_no_authenticated(self):
        """Test create client. Restricted to IsAuthenticated."""
        # Test the endpoint
        client = APIClient()
        data = {
            'first_name': 'client3',
            'last_name': 'client3',
            'email': 'client3@test.com',
            'phone': '0450659422',
            'mobile': '0450498744',
            'company_name': 'company2',
        }
        response = client.post(reverse('list_create_client'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_access_denied_create_client_support(self):
        """Test if user support can't create a customer."""
        # Setup the token
        url = reverse('login')
        data = {'username': 'support', 'password': 'Support74940'}
        response = self.client.post(url, data)
        login_response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in login_response_data)
        token = login_response_data['access']

        # Test the endpoint
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        data = {
            'first_name': 'client3',
            'last_name': 'client3',
            'email': 'client3@test.com',
            'phone': '0450659422',
            'mobile': '0650498744',
            'company_name': 'company2',
        }
        response = client.post(reverse('list_create_client'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_all_clients(self):
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
        response = client.get(reverse('list_create_client'))
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Client.objects.count(), len(response_data))

    def test_access_denied_all_clients_no_authenticated(self):
        """Test fetching all users. Restricted to IsAuthenticated."""
        # Test the endpoint
        client = APIClient()
        response = client.get(reverse('list_create_client'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_one_client(self):
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
        response = client.get(reverse('update_destroy_retrieve_client', kwargs={'pk': self.client1.id}))
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data['email'], self.client1.email)

    def test_access_denied_get_one_client_no_authenticated(self):
        """Test fetching one user. Restricted to IsAuthenticated."""
        # Test the endpoint
        client = APIClient()
        response = client.get(reverse('update_destroy_retrieve_client', kwargs={'pk': self.client1.id}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_client(self):
        """Test if a sales contact can update a client."""
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
        data = {
            'first_name': 'client1Update',
            'last_name': 'client1',
            'email': 'client1@test.com',
            'phone': '0450768549',
            'mobile': '0620498566',
            'company_name': 'company1',
        }
        response = client.put(reverse('update_destroy_retrieve_client', kwargs={'pk': self.client1.id}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_access_denied_update_client_no_authenticated(self):
        """Test update a client. Restricted to IsAuthenticated."""
        # Test the endpoint
        client = APIClient()
        data = {
            'first_name': 'client1Update',
            'last_name': 'client1',
            'email': 'client1@test.com',
            'phone': '0450768549',
            'mobile': '0620498566',
            'company_name': 'company1',
        }
        response = client.put(reverse('update_destroy_retrieve_client', kwargs={'pk': self.client1.id}), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_access_denied_update_client_support(self):
        """Test if a support can't update a client."""
        # Setup the token
        url = reverse('login')
        data = {'username': 'support', 'password': 'Support74940'}
        response = self.client.post(url, data)
        login_response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in login_response_data)
        token = login_response_data['access']

        # Test the endpoint
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        data = {
            'first_name': 'client1Update',
            'last_name': 'client1',
            'email': 'client1@test.com',
            'phone': '0450768549',
            'mobile': '0620498566',
            'company_name': 'company1',
        }
        response = client.put(reverse('update_destroy_retrieve_client', kwargs={'pk': self.client1.id}), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_access_denied_update_client_no_sales_contact(self):
        """Test if a no sales contact can't update client."""
        # Setup the token
        url = reverse('login')
        data = {'username': 'sales2', 'password': 'Sales274940'}
        response = self.client.post(url, data)
        login_response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in login_response_data)
        token = login_response_data['access']

        # Test the endpoint
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        data = {
            'first_name': 'client1Update',
            'last_name': 'client1',
            'email': 'client1@test.com',
            'phone': '0450768549',
            'mobile': '0620498566',
            'company_name': 'company1',
        }
        response = client.put(reverse('update_destroy_retrieve_client', kwargs={'pk': self.client1.id}), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_client(self):
        """Test if a sales contact can delete a client."""
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
        response = client.delete(reverse('update_destroy_retrieve_client', kwargs={'pk': self.client1.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_access_denied_delete_client_no_authenticated(self):
        """Test delete a client. Restricted to IsAuthenticated."""
        # Test the endpoint
        client = APIClient()
        response = client.delete(reverse('update_destroy_retrieve_client', kwargs={'pk': self.client1.id}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_access_denied_delete_client_support(self):
        """Test if a support can't delete a client."""
        # Setup the token
        url = reverse('login')
        data = {'username': 'support', 'password': 'Support74940'}
        response = self.client.post(url, data)
        login_response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in login_response_data)
        token = login_response_data['access']

        # Test the endpoint
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = client.delete(reverse('update_destroy_retrieve_client', kwargs={'pk': self.client1.id}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_access_denied_delete_client_no_sales_contact(self):
        """Test if a no sales contact can't update client."""
        # Setup the token
        url = reverse('login')
        data = {'username': 'sales2', 'password': 'Sales274940'}
        response = self.client.post(url, data)
        login_response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('access' in login_response_data)
        token = login_response_data['access']

        # Test the endpoint
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + token)
        response = client.delete(reverse('update_destroy_retrieve_client', kwargs={'pk': self.client1.id}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
