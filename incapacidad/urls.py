from django.contrib import admin
from django.urls import path
from .import views
from .views import *
from django.urls.resolvers import URLPattern

urlpatterns = [

    # urls de las empresas

    path('empresa',views.empresa, name='empresa'),
    path('agregar_empresa/', agregar_empresa, name='agregar_empresa'),
    path('eliminar_empresa/<int:id>/', eliminar_empresa, name='eliminar_empresa'),
    path('editar_empresa/<int:id>/', editar_empresa, name='editar_empresa'),

    # urls de las Areas

    path('area',views.area, name='area'),
    path('agregar_area/', agregar_area, name='agregar_area'),
    path('eliminar_area/<int:id>/', eliminar_area, name='eliminar_area'),
    path('editar_area/<int:id>/', editar_area, name='editar_area'),

    # urls de los niveles academicos

    path('nivel_academico',views.nivel_academico, name='nivel_academico'),
    path('agregar_nivel_academico/', agregar_nivel_academico, name='agregar_nivel_academico'),
    path('eliminar_nivel_academico/<int:id>/', eliminar_nivel_academico, name='eliminar_nivel_academico'),
    path('editar_nivel_academico/<int:id>/', editar_nivel_academico, name='editar_nivel_academico'),

    # urls de los cargos

    path('cargo',views.cargo, name='cargo'),
    path('agregar_cargo/', agregar_cargo, name='agregar_cargo'),
    path('eliminar_cargo/<int:id>/', eliminar_cargo, name='eliminar_cargo'),
    path('editar_cargo/<int:id>/', editar_cargo, name='editar_cargo'),


    # urls de los Empleados

    path('empleado',views.empleado, name='empleado'),
    path('agregar_empleado/', agregar_empleado, name='agregar_empleado'),
    path('eliminar_empleado/<int:id>/', eliminar_empleado, name='eliminar_empleado'),
    path('editar_empleado/<int:id>/', editar_empleado, name='editar_empleado'),

     # urls de las incapacidades
    path('incapacidad',views.incapacidad, name='incapacidad'),
    path('agregar_inc/', agregar_incapacidad, name='agregar_inc'),
    path('eliminar_inc/<int:id>/', eliminar_inc, name='eliminar_inc'),
    path('editar_inc/<int:id>/', editar_inc, name='editar_inc'),

]