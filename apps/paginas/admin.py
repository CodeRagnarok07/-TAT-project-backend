from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import  Pagina, Seccion, SubTitulo
# Register your models here.


class SubTituloInline(admin.StackedInline):
    extra = 1
    model = SubTitulo

class SeccionInline(admin.StackedInline):
    extra = 1
    model = Seccion
    inlines = [SubTituloInline, ]




@admin.register(Seccion)
class SeccionAdmin(SummernoteModelAdmin):
    list_display = ('titulo','posicion','pagina', )
    search_fields = ['titulo']
    list_filter = ('pagina__titulo_pagina',)

    inlines = [SubTituloInline, ]


@admin.register(Pagina)
class PaginaAdmin(SummernoteModelAdmin):
    list_display = ('titulo_pagina', )
    search_fields = ['titulo']

    # summernote_fields = ['descripcion', ]
    inlines = [SeccionInline, ]

    # autocomplete_fields = ['']
    # def get_search_results(self, request, queryset, search_term):
    #     print("In get search results")
    #     results = super().get_search_results(request, queryset, search_term)
    #     return results

   
