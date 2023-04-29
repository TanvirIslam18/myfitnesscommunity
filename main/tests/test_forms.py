from django.test import TestCase
from main.models import Exercise, WorkoutRoutine
from main.forms import CreateUserForm, Userinformation, calorieInfo, WorkoutForm, PostForm
from django.contrib.auth.models import User


class CreateUserFormTest(TestCase):
    def test_valid_form(self):
        form = CreateUserForm(data={
            'username': 'testuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'testuser@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        })
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = CreateUserForm(data={
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
            'password1': '',
            'password2': '',
        })
        self.assertFalse(form.is_valid())

class UserinformationFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
        )
    def test_valid_form(self):
        form = Userinformation(data={
            'height': 170,
            'weight': 65,
        })
        form.instance.user = self.user
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = Userinformation(data={
            'height': '',
            'weight': '',
        })
        form.instance.user = self.user
        self.assertFalse(form.is_valid())

class calorieInfoFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
        )
    def test_valid_form(self):
        form = calorieInfo(data={
            'age': 25,
            'gender': 'Male',
            'height': 170,
            'weight': 65,
            'activity_level': 'moderate',
        })
        form.instance.user = self.user
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = calorieInfo(data={
            'age': '',
            'gender': '',
            'height': '',
            'weight': '',
            'activity_level': '',
        })
        form.instance.user = self.user
        self.assertFalse(form.is_valid())

class WorkoutFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword',
        )
        self.exercise = Exercise.objects.create(
            muscleGroup='Chest',
            nameOfExercise='Bench Press',
            level='Intermediate',
            firstMuscleGroup='Chest'
        )
        self.data = {
            'exercise': self.exercise.id,
            'day_of_week': 'monday',
        }

    def test_valid_form(self):
        form = WorkoutForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = self.data.copy()
        data['exercise'] = ''
        form = WorkoutForm(data=data)
        self.assertFalse(form.is_valid())

    def test_save_form(self):
        form = WorkoutForm(data=self.data)
        self.assertTrue(form.is_valid())
        workout = form.save(commit=False)
        workout.user = self.user
        workout.save()
        self.assertEqual(WorkoutRoutine.objects.count(), 1)


    
        