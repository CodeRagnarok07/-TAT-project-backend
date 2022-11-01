from django.contrib import admin
from .models import Autoridad, Equipo

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.



class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('descrpcion',)


admin.site.register(Autoridad, PostAdmin)
admin.site.register(Equipo, PostAdmin)
