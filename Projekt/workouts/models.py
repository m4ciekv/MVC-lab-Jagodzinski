from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Workout(models.Model):
    nazwa = models.CharField(max_length=100) # 
    rodzaj = models.CharField(max_length=50) # 
    # Walidacja: intensywność tylko w skali 1-10 
    intensywnosc = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    ) # 

    def __str__(self):
        return self.nazwa
# Create your models here.
