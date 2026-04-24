from django.shortcuts import render, redirect, get_object_or_404
from .models import Workout
from django.db.models import Q # Potrzebne do zaawansowanego wyszukiwania

# 1. Widok listy z WYSZUKIWARKĄ (dodatek na wyższą ocenę)
def workout_list(request):
    query = request.GET.get('q') # Pobieramy frazę z wyszukiwarki
    if query:
        # Filtrujemy treningi po nazwie lub rodzaju
        treningi = Workout.objects.filter(
            Q(nazwa__icontains=query) | Q(rodzaj__icontains=query)
        )
    else:
        treningi = Workout.objects.all()
    
    return render(request, 'workouts/list.html', {'treningi': treningi})

# 2. Widok dodawania treningu
def workout_create(request):
    if request.method == "POST":
        nazwa = request.POST.get('nazwa')
        rodzaj = request.POST.get('rodzaj')
        intensywnosc = request.POST.get('intensywnosc')
        
        # Tworzymy i zapisujemy obiekt w modelu
        Workout.objects.create(nazwa=nazwa, rodzaj=rodzaj, intensywnosc=intensywnosc)
        return redirect('workout_list') # Powrót do listy po zapisie
    
    return render(request, 'workouts/form.html')

# 3. Widok edycji treningu
def workout_edit(request, pk):
    trening = get_object_or_404(Workout, pk=pk)
    if request.method == "POST":
        trening.nazwa = request.POST.get('nazwa')
        trening.rodzaj = request.POST.get('rodzaj')
        trening.intensywnosc = request.POST.get('intensywnosc')
        trening.save()
        return redirect('workout_list')
    
    return render(request, 'workouts/form.html', {'trening': trening})

# 4. Widok usuwania treningu
def workout_delete(request, pk):
    trening = get_object_or_404(Workout, pk=pk)
    if request.method == "POST":
        trening.delete()
        return redirect('workout_list')
    return render(request, 'workouts/confirm_delete.html', {'trening': trening})
