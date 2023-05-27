from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from BlogCocina.models import Escritor, Lector, Articulo

class ArticuloListView(ListView):
    model = Articulo
    template_name = 'BlogCocina/lista_articulos.html'
    
class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    fields = ('titulo', 'subtitulo', 'cuerpo', 'autor', 'imagen')
    success_url = reverse_lazy('lista-articulos')

class ArticuloDetailView(DetailView):
    model = Articulo
    success_url = reverse_lazy('lista-articulos')
    
class ArticuloUpdateView(LoginRequiredMixin, UpdateView):
    model = Articulo
    fields = ('titulo', 'subtitulo', 'cuerpo')
    success_url = reverse_lazy('lista-articulos')
    
class ArticuloDeleteView(LoginRequiredMixin, DeleteView):
    model = Articulo
    success_url = reverse_lazy('lista-articulos')
    