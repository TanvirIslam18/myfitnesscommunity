from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from main.forms import *
from django.contrib.auth.forms import UserCreationForm

class LoginLogoutRegisterTests(TestCase):
    
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'testpassword'
            
        }
        User.objects.create_user(**self.credentials)

    def test_login_success(self):
        response = self.client.post(reverse('loginPage'), self.credentials)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_login_failure(self):
        response = self.client.post(reverse('loginPage'), {'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Username or password is incorrect')

    def test_logout(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('logoutUser'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('loginPage'))

    def test_register_success(self):
        form_data = {
            'first_name': 'test',
            'last_name': 'user',
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'pleasework123',
            'password2': 'pleasework123'
        }
        response = self.client.post(reverse('Register'), form_data)
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(User.objects.first().username, 'testuser') 
        self.assertRedirects(response, reverse('loginPage'))  

    def test_register_failure(self):
        form_data = {
            'first_name': 'test',
            'last_name': 'user',
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        }
        response = self.client.post(reverse('Register'), form_data)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'A user with that username already exists')
        self.assertFalse(User.objects.filter(email='testuser@example.com').exists())

