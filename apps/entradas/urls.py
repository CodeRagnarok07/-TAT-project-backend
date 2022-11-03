from django.urls import path, include
from .views import NoticiasListView

urlpatterns = [
    path('noticias/',  NoticiasListView.as_view(), name="noticias"),
    # path('<int:page>',  PaginaView.as_view(), name="paginas"),

]