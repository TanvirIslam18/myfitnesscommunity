from django.urls import path
from . import views 

urlpatterns = [
path("", views.home, name="home"),

path("loginPage" , views.loginPage , name="loginPage"),
path("logoutUser" , views.logoutUser , name="logoutUser"),
path("Register" , views.Register , name="Register"),

path("EatBetter" , views.EatBetter , name="EatBetter"),
path("MarketPlace" , views.MarketPlace , name="MarketPlace"),


path("viewProfile" , views.viewProfile , name="viewProfile"),
path("BMI", views.BMI, name="BMI"),
path("calorieCalculator" , views.calorieCalculator, name="calorieCalculator"),

path("upload-post" , views.upload_post , name="upload_post"),
path("delete-post/<post_id>" , views.delete_post , name="delete_post"),

path("delete-routine/<routine_id>" , views.delete_workout_routine, name="delete_workout_routine"),

path("viewWorkout" , views.viewWorkout , name="viewWorkout"),
path("viewPlans" , views.viewPlans , name="viewPlans"),
path("search" , views.search , name="search"),

path("foodDetail/<int:pk>" , views.foodDetail , name="foodDetail"),

path("viewWorkout/chest" , views.chestExercises , name="chestExersies"),
path("viewWorkout/bicept" , views.biceptExercises , name="biceptExersies"),
path("viewWorkout/tricep" , views.tricepExercises , name="tricepExersies"),
path("viewWorkout/shoulder" , views.shoulderExercises , name="shoulderExersies"),
path("viewWorkout/back" , views.backExercises , name="backExersies"),
path("viewWorkout/legs" , views.legsExercises, name="legsExersies"),
path("viewWorkout/abs" , views.absExercises , name="absExersies"),
path("viewWorkout/cardio" , views.cardio , name="cardio"),
]