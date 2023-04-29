from django.test import TestCase, Client
from django.urls import reverse
from main.models import *


from django.test import TestCase
from main.models import Exercise

class ExerciseModelTest(TestCase):
    
    def setUp(self):
        self.exercise = Exercise.objects.create(
            muscleGroup='Chest',
            nameOfExercise='Bench Press',
            level='Intermediate',
            firstMuscleGroup='Chest',
            secondMuscleGroup='Triceps'
        )

    def test_string_representation(self):
        exercise = self.exercise
        expected = 'Chest,Bench Press,Intermediate,Chest'
        self.assertEqual(str(exercise), expected)
        
    
    def test_muscle_group_choices(self):
        exercise = self.exercise
        expected_choices = [
            ('Chest', 'Chest'),
            ('Biceps', 'Biceps'),
            ('Tricep', 'Tricep'),
            ('Legs', 'Legs'),
            ('Abs', 'Abs'),
            ('Back', 'Back'),
            ('Shoulder', 'Shoulder'),
            ('Cardio', 'Cardio')
        ]
        self.assertEqual(exercise.muscleGroupOptions, expected_choices)

class FoodModelTest(TestCase):

    
    def setUp(self):
        Food.objects.create(MealType='Breakfast', title='Omelette', ingredients='Eggs, cheese, ham', steps='Whisk eggs, add fillings, cook in pan', nutrition='Calories: 300, Fat: 20g, Protein: 25g')

    def test_meal_type_label(self):
        food = Food.objects.get(id=1)
        field_label = food._meta.get_field('MealType').verbose_name
        self.assertEqual(field_label, 'MealType')


 


    