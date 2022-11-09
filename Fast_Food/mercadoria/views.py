from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from mercadoria.models import Produto
# Create your views here.

class Criar(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    model = Produto
    fields = ["nome", "descricao", "preco", "disponibilidade", "imagem"]
    template_name = "criar.html"
    success_url = reverse_lazy("lista-de-produto")
    login_url = "login.html"
    group_required = u"admin", u"funcionario"

class Listar(ListView):
    model = Produto
    template_name = "listar.html"

class Alterar(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Produto
    fields = ["nome", "descricao", "preco", "disponibilidade", "imagem"]
    template_name = "criar.html"
    success_url = reverse_lazy("lista-de-produto")
    login_url = "login.html"
    group_required = u"admin", u"funcionario"

class Apagar(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    model = Produto
    template_name = "criar.html"
    success_url = reverse_lazy("lista-de-produto")
    login_url = "login.html"
    group_required = u"admin", u"funcionario"