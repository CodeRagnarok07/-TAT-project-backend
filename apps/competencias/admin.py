from django.contrib import admin

# Register your models here.
from .models import Competencias
from django_summernote.admin import SummernoteModelAdmin
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)


admin.site.register(Competencias, PostAdmin)