# Generated by Django 4.2.1 on 2023-05-25 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BlogCocina', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulo',
            name='fecha_publicacion',
        ),
    ]
