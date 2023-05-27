from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class Escritor(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    def __str__(self):
        return f"{self.nombre} | {self.apellido} | {self.email} | {self.fecha_nacimiento}"

class Lector(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    def __str__(self):
        return f"{self.nombre} | {self.apellido} | {self.email} | {self.fecha_nacimiento}"
    
class Articulo(models.Model):
    titulo = models.CharField(max_length=256)
    subtitulo = models.TextField()
    cuerpo = models.TextField()
    autor = models.CharField(max_length=256)
    imagen = models.ImageField(upload_to="img/", null=True, blank=True)
    creador = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.titulo} | {self.subtitulo} | {self.autor}"