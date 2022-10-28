from django.db import models

# Create your models here.



class Pagina(models.Model):
    titulo_pagina = models.CharField(max_length=500)

    def __str__(self):
        return self.titulo_pagina


class Seccion(models.Model):
    titulo = models.CharField(max_length=500)
    icono = models.TextField(blank=True,null=True)
    imagen = models.ImageField(blank=True,null=True)
    url_source = models.CharField(max_length=500, blank=True,null=True)
    posicion = models.IntegerField()
    pagina = models.ForeignKey(Pagina, on_delete=models.CASCADE)

class SubTitulo(models.Model):
    sub_titulo = models.CharField(max_length=500)
    icono = models.TextField()
    posicion = models.IntegerField()
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE)
