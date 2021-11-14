from django.urls import path
from .views import home
# from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home, name='inicio')
    
]
