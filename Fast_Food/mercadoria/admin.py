from django.contrib import admin
from .models import Encomenda, Produto

# Register your models here.
admin.site.register(Encomenda)
admin.site.register(Produto)
