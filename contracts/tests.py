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
from contracts.models import Contract


class ContractTest(APITestCase, URLPatternsTestCase):
    """Test module for Client."""

    urlpatterns = [
        path('api/', include('accounts.urls')),
        path('api/', include("contracts.urls")),
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

        self.contract = Contract(
            title='contract1',
            client=self.client1,
            amount='4785',
            payment_due_date='2022-12-28 00:00:00',
        )

        self.contract.save()

    def test_create_contract(self):
        """Test if a sales user can create a contract."""
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
            'title': 'contract1',
            'client': self.client1.id,
            'amount': '5664',
            'payment_due_date': '27/12/2022',
        }
        response = client.post(reverse('list_create_contract'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_access_denied_create_contract_no_authenticated(self):
        """Test create contract. Restricted to IsAuthenticated."""
        # Test the endpoint
        client = APIClient()
        data = {
            'title': 'contract2',
            'client': self.client1.id,
            'amount': '7899',
            'payment_due_date': '20/04/2022',
        }
        response = client.post(reverse('list_create_contract'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_access_denied_create_contract_support(self):
        """Test if a sales user can create a contract."""
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
            'title': 'contract1',
            'client': self.client1.id,
            'amount': '5664',
            'payment_due_date': '27/12/2022',
        }
        response = client.post(reverse('list_create_contract'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_access_denied_create_contract_no_client_sales_contact(self):
        """Test if not sales contact can't create a contract."""
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
            'title': 'contract1',
            'client': self.client1.id,
            'amount': '5664',
            'payment_due_date': '27/12/2022',
        }
        response = client.post(reverse('list_create_contract'), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_all_contracts(self):
        """Test fetching all contracts."""
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
        response = client.get(reverse('list_create_contract'))
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Contract.objects.count(), len(response_data))

    def test_access_denied_all_contracts_no_authenticated(self):
        """Test fetching all contracts. Restricted to IsAuthenticated."""
        # Test the endpoint
        client = APIClient()
        response = client.get(reverse('list_create_contract'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_one_contract(self):
        """Test fetching one contract."""
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
        response = client.get(reverse('update_destroy_retrieve_contract', kwargs={'pk': self.contract.id}))
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data['title'], self.contract.title)

    def test_access_denied_get_one_contract_no_authenticated(self):
        """Test fetching one contract. Restricted to IsAuthenticated."""
        # Test the endpoint
        client = APIClient()
        response = client.get(reverse('update_destroy_retrieve_contract', kwargs={'pk': self.contract.id}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_contract(self):
        """Test if a sales contact can update a contract."""
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
            'title': 'contract1',
            'amount': '5664',
            'payment_due_date': '27/12/2022',
            'is_finished': '1',
            'is_paid': '1',
        }
        response = client.put(reverse('update_destroy_retrieve_contract', kwargs={'pk': self.contract.id}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_access_denied_update_contract_no_authenticated(self):
        """Test update a contract. Restricted to IsAuthenticated."""
        # Test the endpoint
        client = APIClient()
        data = {
            'title': 'contract1',
            'amount': '5664',
            'payment_due_date': '27/12/2022',
            'is_finished': '1',
            'is_paid': '1',
        }
        response = client.put(reverse('update_destroy_retrieve_contract', kwargs={'pk': self.contract.id}), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_access_denied_update_contract_support(self):
        """Test if a support can't update a contract."""
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
            'title': 'contract1',
            'amount': '5664',
            'payment_due_date': '27/12/2022',
            'is_finished': '1',
            'is_paid': '1',
        }
        response = client.put(reverse('update_destroy_retrieve_contract', kwargs={'pk': self.contract.id}), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_access_denied_update_client_no_sales_contact(self):
        """Test if not sales contact can't update a contract."""
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
            'title': 'contract1',
            'amount': '5664',
            'payment_due_date': '27/12/2022',
            'is_finished': '1',
            'is_paid': '1',
        }
        response = client.put(reverse('update_destroy_retrieve_contract', kwargs={'pk': self.contract.id}), data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_contract(self):
        """Test if a sales contact can delete a contract."""
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
        response = client.delete(reverse('update_destroy_retrieve_contract', kwargs={'pk': self.contract.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_access_denied_delete_contract_no_authenticated(self):
        """Test delete a contract. Restricted to IsAuthenticated."""
        # Test the endpoint
        client = APIClient()
        response = client.delete(reverse('update_destroy_retrieve_contract', kwargs={'pk': self.contract.id}))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_access_denied_delete_contract_support(self):
        """Test if a support can't delete a contract."""
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
        response = client.delete(reverse('update_destroy_retrieve_contract', kwargs={'pk': self.contract.id}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_access_denied_delete_contract_no_sales_contact(self):
        """Test if not sales contact can't delete a contract."""
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
        response = client.delete(reverse('update_destroy_retrieve_contract', kwargs={'pk': self.contract.id}))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
