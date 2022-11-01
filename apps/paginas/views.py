from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.

from .serializer import PaginaSerializers, SeccionSerializers, ContenidoSerializers
from .models import Pagina, Seccion, Contenido

from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.decorators import action

class PaginaView(viewsets.ModelViewSet):
    """
     A simple ViewSet for listing or retrieving users.
    """
    queryset = Seccion.objects.all()
    serializer_class  = SeccionSerializers



class SeccionView(viewsets.ModelViewSet):
    serializer_class = SeccionSerializers
    queryset = Seccion.objects.all()


class ContenidoView(viewsets.ModelViewSet):
    serializer_class = ContenidoSerializers
    queryset = Contenido.objects.all()
