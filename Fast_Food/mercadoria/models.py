from email.policy import default
from secrets import choice
from django.db import models

# Create your models here.
disponibilidade_choices = [
    ("Disponível", "Disponível"),
    ("Indisponível", "Indisponível")
]

class Produto (models.Model):
    nome = models.CharField (max_length=50)
    descricao = models.TextField (max_length=100, verbose_name="Descrição")
    preco = models.DecimalField (max_digits=4, decimal_places=2)
    disponibilidade = models.CharField(max_length=20, choices=disponibilidade_choices, default="Disponível")
    imagem = models.ImageField(upload_to = "img/")



