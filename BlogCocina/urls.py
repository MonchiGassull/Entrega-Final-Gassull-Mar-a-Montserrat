"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from BlogCocina.views import ArticuloListView, ArticuloCreateView, ArticuloDeleteView, ArticuloDetailView, ArticuloUpdateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("articulos/", ArticuloListView.as_view(), name='lista-articulos'),
    path("articulos/<int:pk>/", ArticuloDetailView.as_view(), name='ver-articulos'),
    path("crear-articulos/", ArticuloCreateView.as_view(), name='crear-articulos'),
    path("editar-articulos/<int:pk>/", ArticuloUpdateView.as_view(), name='editar-articulos'),
    path("eliminar-articulos/<int:pk>/", ArticuloDeleteView.as_view(), name='eliminar-articulos'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)