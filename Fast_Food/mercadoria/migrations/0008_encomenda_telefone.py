# Generated by Django 3.2.9 on 2022-11-10 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mercadoria', '0007_encomenda_bilhete'),
    ]

    operations = [
        migrations.AddField(
            model_name='encomenda',
            name='telefone',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
