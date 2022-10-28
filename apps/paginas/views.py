from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializer import PaginaSerializers, SeccionSerializers, SubTituloSerializers
from .models import Pagina, Seccion, SubTitulo


class Paginas(viewsets.ModelViewSet):
    serializer_class = PaginaSerializers
    queryset = Pagina.objects.all()

class Seccion(viewsets.ModelViewSet):
    serializer_class = SeccionSerializers
    queryset = Seccion.objects.all()

class SubTitulo(viewsets.ModelViewSet):
    serializer_class = SubTituloSerializers
    queryset = SubTitulo.objects.all()