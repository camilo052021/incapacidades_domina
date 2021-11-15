from django.contrib import admin
from django.urls import path
from .import views
from .views import *
from django.urls.resolvers import URLPattern

urlpatterns = [
    # urls de las incapacidades
    path('incapacidad',views.incapacidad, name='incapacidad'),
    path('agregar_inc/', agregar_incapacidad, name='agregar_inc'),
    path('eliminar_inc/<int:id>/', eliminar_inc, name='eliminar_inc'),
    path('editar_inc/<int:id>/', editar_inc, name='editar_inc'),

    # urls de las empresas

    path('empresa',views.empresa, name='empresa'),
    path('agregar_empresa/', agregar_empresa, name='agregar_empresa'),
    path('eliminar_empresa/<int:id>/', eliminar_empresa, name='eliminar_empresa'),
    path('editar_empresa/<int:id>/', editar_empresa, name='editar_empresa'),


]