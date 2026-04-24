from django.contrib import admin
from .models import Workout

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    # Te kolumny będą widoczne na liście w panelu admina
    list_display = ('nazwa', 'rodzaj', 'intensywnosc')
    
    # Dodajemy wyszukiwarkę też w panelu admina
    search_fields = ('nazwa', 'rodzaj')
    
    # Dodajemy filtrowanie po boku
    list_filter = ('rodzaj', 'intensywnosc')