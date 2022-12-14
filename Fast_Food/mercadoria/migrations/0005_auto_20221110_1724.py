# Generated by Django 3.2.9 on 2022-11-10 17:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mercadoria', '0004_produto_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.CreateModel(
            name='Encomenda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('localizacao', models.CharField(max_length=50)),
                ('tempo', models.DateField(default=datetime.datetime)),
                ('quantidade', models.IntegerField()),
                ('estado', models.CharField(choices=[('Em Andamento', 'Em Andamento'), ('Entregue', 'Entregue')], default='Em Andamento', max_length=20)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mercadoria.produto')),
            ],
        ),
    ]
