from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from main.models import *
import json

# class TestViews(TestCase):

#     def setUp(self):
#         self.client = Client()
#         self.user = User.objects.create_user(username='dummy_test', password='firstuser')
    
#     def test_eatbetter(self):
#         client = Client()
#         self.client.login(username='testuser', password='testpass')

#         response = client.get(reverse('EatBetter'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'main/EatBetter.html')



    