from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


from .models import *



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1', 'password2']


class Userinformation(ModelForm):
    class Meta:
        model = UserPhysiqueInfo
        field = ['height','weight']
        exclude = ['user','age','gender','activity_level']
                   

class calorieInfo(ModelForm):
    class Meta:
        model = UserPhysiqueInfo
        field = ['age', 'gender', 'height', 'weight', 'activity_level']
        exclude = ['user']


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = WorkoutRoutine
        fields = ['exercise', 'day_of_week']
        widgets = {
            'exercises': forms.CheckboxSelectMultiple,
        }
 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['post']
 
