from django.shortcuts import render

# Create your views here.
from .models import Noticia, GaleriaNoticia
from .serializer import NoticiaSerializers, GaleriaNoticiaSerializers


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.pagination import PageNumberPagination

from django.db.models import Q



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
            'page_size': self.page_size,
            'results': data
        })

class PaginationHandlerMixin(object):
    @property
    def paginator(self):
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator
    def paginate_queryset(self, queryset):
        
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset,
                   self.request, view=self)
    def get_paginated_response(self, data):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)


# TODO endpoins:
# - [x] api de todas las noticias
# - [x] ordenadas por fecha
# - [x] paginacion de las noticias
# class NoticiasListView(generics.ListAPIView):
#     queryset = Noticia.objects.all().order_by("-fecha")
#     serializer_class = NoticiaSerializers
#     pagination_class = PaginationEntradas

# List all with pagination




class NoticiasListView(APIView, PaginationHandlerMixin):
    queryset = Noticia.objects.all().order_by("-fecha")
    serializer_class = NoticiaSerializers
    pagination_class = PaginationEntradas

    # List all with filter and query search
    def get(self, request, format=None, *args, **kwargs):
        """
        lista completa con paginacion: http://127.0.0.1:8000/noticias/
        filtro de año: http://127.0.0.1:8000/noticias/?page=1&year=2005
        parametro de busqueda: http://127.0.0.1:8000/noticias/?search=hola&year=2005
        """
        # products = Noticia.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        search = request.GET.get('search', '')
        year = request.GET.get('year', '')

        queryset = Noticia.objects.all().order_by("-fecha")
        if year:
            queryset = queryset.filter(fecha__year=year)
        if search:
            queryset = queryset.filter(Q(titulo__icontains=search) | Q(contenido__icontains=search))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



# - [ ] detail noticia
class NoticiaView(APIView):
    """
    url: http://127.0.0.1:8000/noticias/titulo
    """
    def get(self, request, titulo):
        queryset = Noticia.objects.filter(titulo=titulo)
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
