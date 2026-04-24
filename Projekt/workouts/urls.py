from django.urls import path
from . import views

urlpatterns = [
    # Strona główna z listą i wyszukiwarką
    path('', views.workout_list, name='workout_list'),
    
    # Dodawanie nowego treningu
    path('dodaj/', views.workout_create, name='workout_create'),
    
    # Edycja (wymaga ID treningu - pk)
    path('edytuj/<int:pk>/', views.workout_edit, name='workout_edit'),
    
    # Usuwanie (wymaga ID treningu - pk)
    path('usun/<int:pk>/', views.workout_delete, name='workout_delete'),
]
