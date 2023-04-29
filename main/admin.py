from django.contrib import admin

# Register your models here.

from .models import Exercise, Food,WorkoutRoutine, userInformation, Post
admin.site.register(Exercise)
admin.site.register(Food)
admin.site.register(WorkoutRoutine)
admin.site.register(userInformation)
admin.site.register(Post)

