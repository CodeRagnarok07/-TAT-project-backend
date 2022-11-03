from django.urls import path, include
from .views import NoticiasListView, NoticiaView

urlpatterns = [
    path('noticias/',  NoticiasListView.as_view(), name="noticias"),
    path('noticias/<str:titulo>/',  NoticiaView.as_view(), name="view_noticias"),

]