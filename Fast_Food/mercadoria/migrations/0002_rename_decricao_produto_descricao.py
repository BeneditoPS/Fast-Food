# Generated by Django 3.2.9 on 2022-11-09 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mercadoria', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='decricao',
            new_name='descricao',
        ),
    ]