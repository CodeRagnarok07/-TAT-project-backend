from django.db import models

# Create your models here.


class Autoridad(models.Model):
    nombre = models.CharField(max_length=500)
    titulo = models.CharField(max_length=500)
    imagen = models.ImageField()
    descrpcion = models.TextField()
    def __str__(self):
        return f'{self.titulo} {self.nombre}'

class Equipo(models.Model):
    nombre = models.CharField(max_length=500)
    titulo = models.CharField(max_length=500)
    imagen = models.ImageField()
    descrpcion = models.TextField()
    def __str__(self):
        return f'{self.titulo} {self.nombre}'
