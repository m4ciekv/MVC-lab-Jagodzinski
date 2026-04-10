from django.shortcuts import render
from .models import Workout

def workout_list(request):
    treningi = Workout.objects.all() # Interakcja z modelem 
    return render(request, 'workouts/list.html', {'treningi': treningi}) # Przekazanie do widoku
