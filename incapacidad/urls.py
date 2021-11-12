from django.urls import path
from .import views
from django.urls.resolvers import URLPattern

urlpatterns = [
    path('',views.home, name='home'),
    path('agregar_inc/', views.agregar_incapacidad, name='agregar_inc'),
]