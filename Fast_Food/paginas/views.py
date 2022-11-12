from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from mercadoria.models import Produto
from mercadoria.models import Encomenda

# Create your views here.

class IndexView(ListView):
    model = Produto
    template_name = "index.html"
   
