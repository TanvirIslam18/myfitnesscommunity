from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Exercise(models.Model):
    muscleGroupOptions = [
        ('Chest','Chest'),
        ('Biceps','Biceps'),
        ('Tricep','Tricep'),
        ('Legs','Legs'),
        ('Abs','Abs'),
        ('Back','Back'),
        ('Shoulder','Shoulder'),
        ('Cardio','Cardio'),
    ]

    muscleGroup = models.CharField(max_length=255, choices=muscleGroupOptions)
    nameOfExercise = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    firstMuscleGroup =     models.CharField(max_length=255)
    secondMuscleGroup = models.CharField(max_length=255, blank=True, null=True)
    workoutImage = models.ImageField(upload_to='static/images/allWorkouts',null=True)

    def __str__(self) :
        return self.muscleGroup + ',' +self.nameOfExercise + ',' + self.level + ',' + self.firstMuscleGroup
    
class Food(models.Model):
    
    MealType = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    ingredients = models.CharField(max_length=1000)
    steps = models.CharField(max_length=2000)
    nutrition = models.CharField(max_length=255,null=True)
    foodImage = models.ImageField(null=True,upload_to='static/images/food')

    def __str__(self) :
        return self.MealType + ',' +self.title 
     

class UserPhysiqueInfo(models.Model):
    GENDER_CHOICES = (("Male", "Male"),("Female", "Female"))
    fitness_choice = (('sedentary', 'Sedentary'), ('light', 'Light'),
        ('moderate', 'Moderate'), ('active', 'Active'),
        ('very_active', 'Very Active'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    height = models.FloatField( )
    weight = models.FloatField( )
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    activity_level = models.CharField(max_length=20, choices=fitness_choice, default='moderate')


class WorkoutRoutine(models.Model):
    DAY_CHOICES = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10,choices=DAY_CHOICES,null=False)


class userInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    profileImage = models.ImageField(null=True, blank=True)



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.FileField(upload_to='posts', null=True, blank=True)

    
