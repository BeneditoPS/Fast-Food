from django.shortcuts import render
from django.views.generic.list import ListView
from mercadoria.models import Produto

# Create your views here.

class IndexView(ListView):
    model = Produto
    template_name = "index.html"
