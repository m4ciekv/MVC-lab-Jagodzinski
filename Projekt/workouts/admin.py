from django.contrib import admin
from .models import Workout, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nazwa',)

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    
    list_display = ('nazwa', 'category', 'intensywnosc')
    
    search_fields = ('nazwa',)
    
    list_filter = ('category', 'intensywnosc')