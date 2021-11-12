from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    context ={}
    return render(request,'templates/home.html',context)