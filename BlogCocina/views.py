from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from BlogCocina.models import Escritor, Lector, Articulo

class ArticuloListView(ListView):
    model = Articulo
    template_name = 'BlogCocina/lista_articulos.html'
    
class ArticuloCreateView(LoginRequiredMixin, CreateView):
    model = Articulo
    fields = ('titulo', 'subtitulo', 'cuerpo', 'autor', 'imagen', 'fecha')
    success_url = reverse_lazy('lista-articulos')
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        response = super().form_valid(form)

#        if 'imagen' in self.request.FILES:
#            imagen = self.request.FILES['imagen']
#            self.object.imagen = imagen
#            self.object.save()
        
        return response

class ArticuloDetailView(DetailView):
    model = Articulo
    success_url = reverse_lazy('lista-articulos')
    
class ArticuloUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articulo
    fields = ('titulo', 'subtitulo', 'cuerpo')
    success_url = reverse_lazy('lista-articulos')
    def test_func(self):
        objeto = self.get_object()
        return self.request.user == objeto.usuario
    
class ArticuloDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articulo
    success_url = reverse_lazy('lista-articulos')
    def test_func(self):
        objeto = self.get_object()
        return self.request.user == objeto.usuario
    