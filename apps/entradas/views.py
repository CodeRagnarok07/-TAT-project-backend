from django.shortcuts import render

# Create your views here.
from .models import Noticia, GaleriaNoticia
from .serializer import NoticiaSerializers, GaleriaNoticiaSerializers


from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework import status


from rest_framework.pagination import PageNumberPagination


class PaginationEntradas(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 5
    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })

# TODO endpoins:
# - [x] api de todas las noticias
# - [x] ordenadas por fecha
# - [x] paginacion de las noticias


class NoticiasListView(APIView):
    queryset = Noticia.objects.all().order_by("-fecha")
    serializer_class = NoticiaSerializers
    pagination_class = PaginationEntradas

    def get(self, request, *args, **kwargs):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = Noticia.objects.all().order_by("-fecha")

        paginator = PaginationEntradas()
        result_page = paginator.paginate_queryset(queryset, request)
        serializer = NoticiaSerializers(result_page, many=True)

        return Response(serializer.data)


# - [ ] detail noticia
class NoticiaView(APIView):
    def get(self, request, pk):
        queryset = Noticia.objects.filter(pk=pk)
        serializer = NoticiaSerializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# - [ ] endpoint filtro de toticias por fecha
# - [ ] paginacion de las noticias con filtro

# - [ ] resultados de busqueda sin tomar en cuenta la paginacion, osea todas las entradas
# - [ ] Endpoint para buscador con su paginacion


# TODO frontend
# ## replicar en los otros tipos de entradas
# crear el buscador
# ### comoponente HOC que agrega el buscador
# - [ ] sin resultados de busqueda trae la api normal
# - [ ] con busqueda trae los resultados de todo pero tambien paginados
# - [ ] buscador con año
# - [ ] sin tag año

# Informes de Viajes Nacionales
# Edictos
# Convenios
# Acuerdos
# Leyes y Decretos
# combinando
