# from django.shortcuts import render

# # Create your views here.

# from .serializer import PaginaSerializers, SeccionSerializers, SubTituloSerializers
# from .models import Pagina, Seccion, SubTitulo
# from rest_framework import viewsets

# from rest_framework.response import Response

# class Paginas(viewsets.ViewSet):
#     serializer_class = PaginaSerializers
#     queryset = Pagina.objects.all()
#     def list(self, request):
#         serializer = PaginaSerializers(self.queryset, many=True)
#         return Response(serializer.data)
#         # return Response(serializer.data)

# class Seccion(viewsets.ModelViewSet):
#     serializer_class = SeccionSerializers
#     queryset = Seccion.objects.all()

# class SubTitulo(viewsets.ModelViewSet):
#     serializer_class = SubTituloSerializers
#     queryset = SubTitulo.objects.all()