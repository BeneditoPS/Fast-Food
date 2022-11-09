from django.urls import path
from .views import Criar, Listar, Alterar, Apagar

urlpatterns = [
    path("criar/", Criar.as_view(), name="criar-produto"),
    path("listar/", Listar.as_view(), name="lista-de-produto"),
    path("alterar/<int:pk>/", Alterar.as_view(), name="alterar-produto"),
    path("apagar/<int:pk>/", Apagar.as_view(), name="apagar-produto")
]