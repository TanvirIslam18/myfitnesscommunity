from pydoc import resolve
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from main.views import (
    EatBetter, MarketPlace, viewProfile, BMI, calorieCalculator, viewWorkout, viewPlans, search, foodDetail,
    chestExercises, biceptExercises, tricepExercises, shoulderExercises,
    backExercises, legsExercises, absExercises, cardio
)



class TestUrls(TestCase):
    
    def setUp(self):
        
        self.client = Client()
        self.user = User.objects.create_user(
            username='dummy_test', password='firstuser'
            
        )
        self.client.login(username='dummy_test', password='firstuser')
    
    def test_chest_url(self):
        url = reverse('chestExersies')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/viewWorkout.html')
        self.assertEqual(response.resolver_match.func, chestExercises)

    def test_bicept_url(self):
        url = reverse('biceptExersies')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/viewWorkout.html')
        self.assertEqual(response.resolver_match.func, biceptExercises)

    def test_tricep_url(self):
        url = reverse('tricepExersies')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/viewWorkout.html')
        self.assertEqual(response.resolver_match.func, tricepExercises)

    def test_shoulder_url(self):
        url = reverse('shoulderExersies')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/viewWorkout.html')
        self.assertEqual(response.resolver_match.func, shoulderExercises)

    def test_back_url(self):
        url = reverse('backExersies')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/viewWorkout.html')
        self.assertEqual(response.resolver_match.func, backExercises)

    def test_legs_url(self):
        url = reverse('legsExersies')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/viewWorkout.html')
        self.assertEqual(response.resolver_match.func, legsExercises)

    def test_abs_url(self):
        url = reverse('absExersies')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/viewWorkout.html')
        self.assertEqual(response.resolver_match.func, absExercises)

    def test_cardio_url(self):
        url = reverse('cardio')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/viewWorkout.html')
        self.assertEqual(response.resolver_match.func, cardio)

    def test_EatBetter_url(self):
        url = reverse('EatBetter')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/EatBetter.html')
        self.assertEqual(response.resolver_match.func, EatBetter)

    def test_MarketPlace_url(self):
        url = reverse('MarketPlace')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/MarketPlace.html')
        self.assertEqual(response.resolver_match.func, MarketPlace)
    
    def test_viewProfile_url(self):
        url = reverse('viewProfile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/viewProfile.html')
        self.assertEqual(response.resolver_match.func, viewProfile)

    def test_BMI_url(self):
        url = reverse('BMI')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/BMI.html')
        self.assertEqual(response.resolver_match.func, BMI)

    def test_calorieCalculator_url(self):
        url = reverse('calorieCalculator')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/calorieCalculator.html')
        self.assertEqual(response.resolver_match.func, calorieCalculator)

    
    def test_viewWorkout_url(self):
        url = reverse('viewWorkout')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/viewWorkout.html')
        self.assertEqual(response.resolver_match.func, viewWorkout)

    def test_viewPlans_url(self):
        url = reverse('viewPlans')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/viewPlans.html')
        self.assertEqual(response.resolver_match.func, viewPlans)

    def test_search_url(self):
        response = self.client.get(reverse('search'), {'search': 'dummy_test'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/searchResults.html')
        self.assertEqual(response.resolver_match.func, search)


    
    

