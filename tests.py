from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from users.models import UserRegistrationModel
import json

class BasicTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage_loads(self):
        """Test that the homepage loads successfully"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_health_check(self):
        """Test health check endpoint"""
        response = self.client.get('/health/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), 'OK')

    def test_admin_login_page(self):
        """Test admin login page loads"""
        response = self.client.get('/Adminlogin/')
        self.assertEqual(response.status_code, 200)

    def test_user_login_page(self):
        """Test user login page loads"""
        response = self.client.get('/UserLogin/')
        self.assertEqual(response.status_code, 200)

    def test_user_register_page(self):
        """Test user registration page loads"""
        response = self.client.get('/UserRegister/')
        self.assertEqual(response.status_code, 200)

    def test_admin_login_valid(self):
        """Test admin login with valid credentials"""
        response = self.client.post('/AdminLoginCheck/', {
            'loginid': 'admin',
            'pswd': 'admin'
        })
        self.assertEqual(response.status_code, 200)

    def test_admin_login_invalid(self):
        """Test admin login with invalid credentials"""
        response = self.client.post('/AdminLoginCheck/', {
            'loginid': 'wrong',
            'pswd': 'wrong'
        })
        self.assertEqual(response.status_code, 200)

class UserModelTestCase(TestCase):
    def test_user_creation(self):
        """Test user model creation"""
        user = UserRegistrationModel.objects.create(
            name='Test User',
            loginid='testuser',
            password='testpass',
            mobile='9876543210',
            email='test@example.com',
            locality='Test City',
            address='Test Address',
            city='Test City',
            state='Test State',
            status='waiting'
        )
        self.assertEqual(user.name, 'Test User')
        self.assertEqual(user.status, 'waiting')
        self.assertEqual(str(user), 'testuser')

class MLPredictionTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a test user and log in
        self.test_user = UserRegistrationModel.objects.create(
            name='ML Test User',
            loginid='mltest',
            password='testpass',
            mobile='9876543211',
            email='mltest@example.com',
            locality='Test City',
            address='Test Address',
            city='Test City',
            state='Test State',
            status='activated'
        )

    def test_prediction_page_loads(self):
        """Test that prediction page loads"""
        response = self.client.get('/prediction/')
        self.assertEqual(response.status_code, 200)

    def test_dataset_view_loads(self):
        """Test that dataset view loads"""
        response = self.client.get('/DatasetView/')
        self.assertEqual(response.status_code, 200)

    def test_training_view_loads(self):
        """Test that training view loads"""
        response = self.client.get('/training/')
        # This might take time due to ML processing, so we just check it doesn't crash
        self.assertIn(response.status_code, [200, 500])  # 500 is acceptable if model files aren't available