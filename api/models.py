from django.db import models

class Proeducto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    marca = models.CharField(max_length=50)
    cantidad_min=models.IntegerField()
    cantidad_max=models.IntegerField()
    precio = models.DecimalField(max_digits=10,decimal_places=2)
