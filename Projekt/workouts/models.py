from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Nowy model kategorii (Wymóg na 5.0 z dokumentacji)
class Category(models.Model):
    nazwa = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nazwa

class Workout(models.Model):
    nazwa = models.CharField(max_length=100)
    
    # Zmieniamy zwykły tekst na relację klucza obcego do nowego modelu
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Rodzaj")
    
    intensywnosc = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )

    @property
    def intensywnosc_procent(self):
        return self.intensywnosc * 10

    def __str__(self):
        return self.nazwa