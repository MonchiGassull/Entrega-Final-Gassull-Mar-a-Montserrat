from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Escritor(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()

class Lector(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    
class Articulo(models.Model):
    titulo = models.CharField(max_length=256)
    subtitulo = models.TextField()
    desarrollo = models.TextField()
    autor = models.CharField(max_length=256)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)