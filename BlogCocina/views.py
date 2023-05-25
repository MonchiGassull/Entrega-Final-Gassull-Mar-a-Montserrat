from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from BlogCocina.models import Escritor, Lector, Articulo

class ArticuloListView(ListView):
    model = Articulo
    template_name = 'BlogCocina/lista_articulos.html'
    
class ArticuloCreateView(CreateView):
    model = Articulo
    fields = ('titulo', 'subtitulo', 'desarrollo', 'autor')
    success_url = reverse_lazy('lista-articulos')

class ArticuloDetailView(DetailView):
    model = Articulo
    success_url = reverse_lazy('lista-articulos')
    
class ArticuloUpdateView(UpdateView):
    model = Articulo
    fields = ('titulo', 'subtitulo', 'desarrollo')
    success_url = reverse_lazy('lista-articulos')
    
class ArticuloDeleteView(DeleteView):
    model = Articulo
    success_url = reverse_lazy('lista-articulos')