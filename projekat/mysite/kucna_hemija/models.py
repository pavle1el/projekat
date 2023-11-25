from django.db import models

# Create your models here.
from django.db import models

class Proizvodi(models.Model):
    barkod = models.CharField(max_length=20, unique=True)
    naziv_proizvoda = models.CharField(max_length=100)
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    na_stanju = models.PositiveIntegerField()

    def __str__(self):
        return self.naziv_proizvoda
