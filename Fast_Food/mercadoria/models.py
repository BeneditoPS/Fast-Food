from datetime import datetime
from email.policy import default
from datetime import datetime
from random import choices
from secrets import choice
from symbol import return_stmt
from django.db import models

# Create your models here.
disponibilidade_choices = [
    ("Disponível", "Disponível"),
    ("Indisponível", "Indisponível")
]
estado_choices = [
    ("Em Andamento", "Em Andamento"),
    ("Entregue", "Entregue")
]

class Produto (models.Model):
    nome = models.CharField (max_length=50)
    descricao = models.TextField (max_length=100, verbose_name="Descrição")
    preco = models.DecimalField (max_digits=10, decimal_places=2)
    disponibilidade = models.CharField(max_length=20, choices=disponibilidade_choices, default="Disponível")
    imagem = models.ImageField(upload_to = "img/")

    def __str__(self):
        return "{} {}".format(self.nome, self.preco)

class Encomenda (models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    nome = models.CharField(max_length=50)
    bilhete = models.CharField(max_length=14)
    telefone = models.IntegerField()
    localizacao = models.CharField(max_length=50)
    tempo = models.DateTimeField(default=datetime.now)
    quantidade = models.IntegerField()
    estado = models.CharField(max_length=20, choices=estado_choices, default="Em Andamento")

    def __str__(self):
        return "{} {} {}".format(self.produto, self.nome, self.quantidade)



