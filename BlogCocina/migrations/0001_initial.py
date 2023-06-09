# Generated by Django 4.2.1 on 2023-05-25 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=256)),
                ('subtitulo', models.TextField()),
                ('desarrollo', models.TextField()),
                ('autor', models.CharField(max_length=256)),
                ('fecha_publicacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Escritor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256)),
                ('apellido', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Lector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=256)),
                ('apellido', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
    ]
