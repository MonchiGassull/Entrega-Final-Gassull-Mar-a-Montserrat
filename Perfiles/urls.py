from django.contrib import admin
from django.urls import path, include
from Perfiles.views import registro, login_view, CustomLogoutView, MiPerfilUpdateView, agregar_avatar
from blog.views import inicio, about

urlpatterns = [
   path('registro/', registro, name="registro"),
   path('login/', login_view, name="login"),
   path('logout/', CustomLogoutView.as_view(), name="logout"), 
   path('editar-perfil/', MiPerfilUpdateView.as_view(), name="editar-perfil"), 
   path('agregar-avatar/', agregar_avatar, name="agregar-avatar"),
   path('editar-perfil/about/',about, name='about2'),
]
