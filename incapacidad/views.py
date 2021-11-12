from django.forms.forms import Form
from django.http import request
from django.shortcuts import redirect, render
from .models import *
from .forms import IncpacidadForm
# Create your views here.

def home(request):
    incapacidades = Incapacidades.objects.all()
    context ={'incapacidades':incapacidades}
    return render(request,'home.html',context)

def agregar_incapacidad(request):
    if request.method=='POST':
        form = IncpacidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = IncpacidadForm()
    
    context = {'form': form}
    return render(request,'agregar_inc.html',context)