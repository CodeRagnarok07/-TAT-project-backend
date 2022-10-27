from turtle import position
from django.db import models

# Create your models here.



class Pagina(models.Model):
    titulo_pagina = models.CharField()


class Seccion(models.Model):
    titulo = models.CharField()
    icono = models.TextField()
    url = models.TextField()
    url = models.ImageField()
    posicion = models.IntegerField()
    pagina = models.ForeignKey(Pagina, on_delete=models.CASCADE)

class SubTitulo(models.Model):
    titulo = models.CharField()
    icono = models.TextField()
    posicion = models.IntegerField()
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)

