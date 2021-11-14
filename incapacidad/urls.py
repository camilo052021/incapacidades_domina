from django.contrib import admin
from django.urls import path
from .import views
from .views import *
from django.urls.resolvers import URLPattern

urlpatterns = [
    path('incapacidad',views.incapacidad, name='incapacidad'),
    path('agregar_inc/', agregar_incapacidad, name='agregar_inc'),
    path('eliminar_inc/<int:id>/', eliminar_inc, name='eliminar_inc'),
    path('editar_inc/<int:id>/', editar_inc, name='editar_inc'),
]