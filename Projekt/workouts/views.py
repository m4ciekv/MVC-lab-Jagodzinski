from django.shortcuts import render, redirect, get_object_or_404
from .models import Workout, Category  # Pamiętaj o zaimportowaniu Category!
from django.db.models import Q 

# 1. Widok listy z WYSZUKIWARKĄ (zaawansowane filtrowanie relacyjne)
def workout_list(request):
    query = request.GET.get('q') 
    if query:
        # Filtrujemy po nazwie treningu LUB po nazwie powiązanej kategorii
        treningi = Workout.objects.filter(
            Q(nazwa__icontains=query) | Q(category__nazwa__icontains=query)
        )
    else:
        treningi = Workout.objects.all()
    
    return render(request, 'workouts/list.html', {'treningi': treningi})

# 2. Widok dodawania treningu
def workout_create(request):
    if request.method == "POST":
        nazwa_treningu = request.POST.get('nazwa')
        category_id = request.POST.get('category')  # Pobieramy ID wybranej kategorii z dropdownu
        intensywnosc_treningu = request.POST.get('intensywnosc')
        
        # Pobieramy obiekt kategorii z bazy danych
        kategoria = get_object_or_404(Category, pk=category_id) if category_id else None
        
        # Tworzymy obiekt z poprawną relacją klucza obcego
        Workout.objects.create(
            nazwa=nazwa_treningu, 
            category=kategoria, 
            intensywnosc=intensywnosc_treningu
        )
        return redirect('workout_list') 
    
    # Przekazujemy wszystkie kategorie do formularza, żeby wyrenderować dropdown
    kategorie = Category.objects.all()
    return render(request, 'workouts/form.html', {'kategorie': kategorie})

# 3. Widok edycji treningu
def workout_edit(request, pk):
    trening = get_object_or_404(Workout, pk=pk)
    if request.method == "POST":
        nazwa_treningu = request.POST.get('nazwa')
        category_id = request.POST.get('category')
        intensywnosc_treningu = request.POST.get('intensywnosc')
        
        kategoria = get_object_or_404(Category, pk=category_id) if category_id else None
        
        # Aktualizujemy pola obiektu
        trening.nazwa = nazwa_treningu
        trening.category = kategoria
        trening.intensywnosc = intensywnosc_treningu
        trening.save()
        return redirect('workout_list')
    
    # Przekazujemy zarówno edytowany trening, jak i listę wszystkich kategorii do dropdownu
    kategorie = Category.objects.all()
    return render(request, 'workouts/form.html', {'trening': trening, 'kategorie': kategorie})

# 4. Widok usuwania treningu
def workout_delete(request, pk):
    trening = get_object_or_404(Workout, pk=pk)
    if request.method == "POST":
        trening.delete()
        return redirect('workout_list')
    return render(request, 'workouts/confirm_delete.html', {'trening': trening})