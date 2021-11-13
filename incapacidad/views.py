from django.forms.forms import Form
from django.http import request
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import IncapacidadForm
# Create your views here.

def home(request):
    incapacidades = Incapacidades.objects.all()
    context ={'incapacidades':incapacidades}
    return render(request,'home.html',context)

def agregar_incapacidad(request):
    if request.method =='POST':
        form = IncapacidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = IncapacidadForm()
    
    context = {'form' : form}
    return render(request,'agregar_inc.html',context)

def eliminar_inc(request, id):
    incapacidad = get_object_or_404(Incapacidades, pk=id)
    if Incapacidades:
        incapacidad.delete()
    return redirect('home')

def editar_inc(request, id):
    incapacidad = get_object_or_404(Incapacidades, pk=id)
    if request.method =='POST':
        form = IncapacidadForm(request.POST, instance=incapacidad)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = IncapacidadForm(instance=incapacidad)
    
    context = {'form' : form}
    return render(request,'editar_inc.html',context)