from collections import defaultdict
from itertools import groupby
from django.shortcuts import render, redirect
from django.http import HttpResponse 
from django.contrib.auth.models import User

from .forms import CreateUserForm, Userinformation, WorkoutForm, calorieInfo, PostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *

import base64
from urllib.parse import urlencode
import requests
# Create your views here.



def loginPage(request):
    if request.user.is_authenticated:
         return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username = username, password = password)

            if user is not None:
                login(request,user)
                return redirect ('home')
            else:
                messages.info(request, 'Username or password is incorrect')

        return render(request, "main/login.html")

def logoutUser(request):
    logout(request)
    return redirect('loginPage')
    
def Register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for' + user)

                return redirect(loginPage)                 
    return render(request, "main/Register.html", {'form':form} )

@login_required(login_url='loginPage')
def home(request):
    return render(request, "main/home.html", {} )

@login_required(login_url='loginPage')
def EatBetter(request):
    Foods = Food.objects.all()
    
    breakfast = Food.objects.filter(MealType = "Breakfast")
    lunch = Food.objects.filter(MealType = "Lunch")
    dinner = Food.objects.filter(MealType = "Dinner")

    context = {'Foods': Foods, 'breakfast': breakfast, 'lunch': lunch, 'dinner': dinner}
    return render(request, "main/EatBetter.html", context )

@login_required(login_url='loginPage')
def foodDetail(request,pk):
    
    Foods = Food.objects.get(id=pk)

    context = {'Foods': Foods}
    return render(request, "main/foodDetail.html", context )

@login_required(login_url='loginPage')
def MarketPlace(request):
    if request.method == "GET":

        try:
            search_gym_item = request.GET.get("search_gym_item", "lifting belts")
        except:
            return render(request, "main/MarketPlace.html", {})
 
        ebay_key = "TanvirIs-myFitnes-PRD-f75719fb7-8af1146d:PRD-75719fb71712-bb16-4327-a4c8-d67c"

        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": "Basic " + base64.b64encode(bytes(ebay_key, encoding="utf-8")).decode("ascii"),
        }
        data = urlencode(
            {
                "grant_type": "client_credentials",
                "scope": "https://api.ebay.com/oauth/api_scope",
            }
        )
        response = requests.post("https://api.ebay.com/identity/v1/oauth2/token", headers=headers, data=data)
        token = response.json()["access_token"]
        headers = {"Authorization": "Bearer " + token, "X-EBAY-C-MARKETPLACE-ID": "EBAY-GB"}

        params = {"q": search_gym_item,"limit": "12"}
        response = requests.get(
            "https://api.ebay.com/buy/browse/v1/item_summary/search", headers=headers, params=params
        )
        response = response.json()["itemSummaries"]
        
        return render(request, "main/MarketPlace.html", {"search_gym_item": search_gym_item, "items": response} )


@login_required(login_url='loginPage')
def viewWorkout(request):
    Exercises = Exercise.objects.all()
    
    
    if request.method == 'POST':

        user = request.user
        exercise_id = request.POST.get('exercise_id')
        day_of_week = request.POST.get('day_of_week')


        exercise = Exercise.objects.get(id=exercise_id)
        workout = WorkoutRoutine(user=user, exercise=exercise, day_of_week=day_of_week)
        workout.save()
        return redirect('viewWorkout') # Redirect to a success page or workouts page

    return render(request, "main/viewWorkout.html", {'Exercises': Exercises} )




@login_required(login_url='loginPage')
def viewPlans(request):
    person = userInformation.objects.get(user=request.user)
    workout = WorkoutRoutine.objects.filter(user=request.user)
    monday = workout.filter(day_of_week="monday")
    tuesday = workout.filter(day_of_week="tuesday")
    wednesday = workout.filter(day_of_week="wednesday")
    thursday = workout.filter(day_of_week="thursday")
    friday = workout.filter(day_of_week="friday")
    saturday = workout.filter(day_of_week="saturday")
    sunday = workout.filter(day_of_week="sunday")

    context = {'workout': workout, 'monday': monday, 'tuesday': tuesday, 'wednesday': wednesday,
        'thursday': thursday, 'friday': friday, 'saturday': saturday, 'sunday': sunday, 'person': person}
    return render(request, 'main/viewPlans.html', context)

  




@login_required(login_url='loginPage')
def viewProfile(request):
    
    post_form = PostForm()
    person = userInformation.objects.get(user=request.user)
    posts = Post.objects.filter(user=request.user)
    
    return render(request, "main/viewProfile.html", { 'person':person, 'post_form': post_form, 'posts': posts} )





@login_required(login_url='loginPage')
def BMI(request):
    person = userInformation.objects.get(user=request.user)
    if request.method == 'POST':
        form = Userinformation(request.POST)
        if form.is_valid():

            weight = float(request.POST.get('weight'))
            height = float(request.POST.get('height'))
            height = height/100
            bmi = weight/(height*height)
            bmi = round(bmi,2)
            if bmi < 18.5:
                message = "You are underweight"
            elif bmi >= 18.5 and bmi <= 24.9:
                message = "You are normal weight"
            elif bmi >= 25 and bmi <= 29.9:
                message = "You are overweight"
            elif bmi >= 30:
                message = "You are obese"
            return render(request, "main/BMI.html", {'bmi' : bmi, 'message' : message,'form':form, 'person':person} )
        else:
            form = Userinformation()
            return render(request, "main/BMI.html", {'form':form} )
        
    else:
        form = Userinformation()
        return render(request, "main/BMI.html", {'form':form, 'person':person} )
    
@login_required(login_url='loginPage') 
def calorieCalculator(request):
    person = userInformation.objects.get(user=request.user)
    if request.method == 'POST':
        form = calorieInfo(request.POST)
        if form.is_valid():      
            age = form.cleaned_data['age']
            height = form.cleaned_data['height'] 
            weight = form.cleaned_data['weight']
            gender = form.cleaned_data['gender']
            activity_level = form.cleaned_data['activity_level']          

            if gender == 'male':
                bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
            else:
                bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
            
            if activity_level == 'sedentary':
                calorie_maintenance = round(bmr * 1.2)
            elif activity_level == 'light':
                calorie_maintenance = round(bmr * 1.375)
            elif activity_level == 'moderate':
                calorie_maintenance = round(bmr * 1.55)
            elif activity_level == 'active':
                calorie_maintenance = round(bmr * 1.725)
            elif activity_level == 'very_active':
                calorie_maintenance = round(bmr * 1.9)

            
            
            return render(request, "main/calorieCalculator.html", {'calorie_maintenance' : calorie_maintenance, 'form':form, 'person':person} )
        else:
            
            return render(request, "main/calorieCalculator.html", {'calorie_maintenance':form.errors} )
    else:
        form = calorieInfo()
        
        return render(request, "main/calorieCalculator.html", {'form':form, 'person':person} )
        

@login_required(login_url='loginPage') 
def upload_post(request):
    
    if request.method == 'POST':
        
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():    
            check_form = form.save(commit=False)
            check_form.user = request.user
            check_form.save()  

            return redirect('viewProfile')
        else:
            return HttpResponse(form.errors)
    else:
        
        return redirect("viewProfile")
        

@login_required(login_url='loginPage') 
def delete_post(request, post_id):
    if request.method == 'POST':
        post = Post.objects.filter(user=request.user, id=post_id)
        post.delete()
        return redirect('viewProfile')
    else:
        return redirect('viewProfile')


@login_required(login_url='loginPage') 
def delete_workout_routine(request, routine_id):
    if request.method == 'POST':
        routine = WorkoutRoutine.objects.filter(user=request.user, id=routine_id)
        routine.delete()
        return redirect('viewPlans')
    else:
        return redirect('viewPlans')


@login_required(login_url='loginPage') 
def search(request):
    query = request.GET.get('search')
    
    # search or query items
    searched_user = User.objects.filter(username__icontains=query).first()

    posts = Post.objects.filter(user=searched_user)

    workout = WorkoutRoutine.objects.filter(user=searched_user)
    monday = workout.filter(day_of_week="monday")
    tuesday = workout.filter(day_of_week="tuesday")
    wednesday = workout.filter(day_of_week="wednesday")
    thursday = workout.filter(day_of_week="thursday")
    friday = workout.filter(day_of_week="friday")
    saturday = workout.filter(day_of_week="saturday")
    sunday = workout.filter(day_of_week="sunday")

    args = {
            'person': searched_user, 
            'posts': posts,
            'monday': monday,
            'tuesday': tuesday,
            'wednesday': wednesday,
            'thursday': thursday,
            'friday': friday,
            'saturday': saturday,
            'sunday': sunday,
        }
    
    return render(request, "main/searchResults.html", args)



def chestExercises(response):
    Exercises = Exercise.objects.all().filter(muscleGroup ="Chest")

    return render(response, "main/viewWorkout.html", {'Exercises' : Exercises} )

def biceptExercises(response):
    Exercises = Exercise.objects.all().filter(muscleGroup ="Biceps")

    return render(response, "main/viewWorkout.html", {'Exercises' : Exercises} )

def tricepExercises(response):
    Exercises = Exercise.objects.all().filter(muscleGroup ="Tricep")

    return render(response, "main/viewWorkout.html", {'Exercises' : Exercises} )

def shoulderExercises(response):
    Exercises = Exercise.objects.all().filter(muscleGroup ="Shoulder")

    return render(response, "main/viewWorkout.html", {'Exercises' : Exercises} )

def backExercises(response):
    Exercises = Exercise.objects.all().filter(muscleGroup ="Back")

    return render(response, "main/viewWorkout.html", {'Exercises' : Exercises} )

def legsExercises(response):
    Exercises = Exercise.objects.all().filter(muscleGroup ="Legs")

    return render(response, "main/viewWorkout.html", {'Exercises' : Exercises} )

def absExercises(response):
    Exercises = Exercise.objects.all().filter(muscleGroup ="Abs")

    return render(response, "main/viewWorkout.html", {'Exercises' : Exercises} )

def cardio(response):
    Exercises = Exercise.objects.all().filter(muscleGroup ="Cardio")

    return render(response, "main/viewWorkout.html", {'Exercises' : Exercises} )

