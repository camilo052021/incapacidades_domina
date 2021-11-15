from django.forms.forms import Form
from django.http import request
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import *
# Create your views here.

### vista para las empresas
def empresa(request):
    empresas = Empresa.objects.all()
    context ={'empresas':empresas}
    return render(request,'empresa.html',context)

def agregar_empresa(request):
    if request.method =='POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empresa')
    else:
        form = EmpresaForm()
    
    context = {'form' : form}
    return render(request,'agregar_empresa.html',context)

def eliminar_empresa(request, id):
    empresa = get_object_or_404(Empresa, pk=id)
    if Empresa:
        empresa.delete()
    return redirect('empresa')

def editar_empresa(request, id):
    empresa = get_object_or_404(Empresa, pk=id)
    if request.method =='POST':
        form = EmpresaForm(request.POST, instance=empresa)
        if form.is_valid():
            form.save()
            return redirect('empresa')
    else:
        form = EmpresaForm(instance=empresa)
    
    context = {'form' : form}
    return render(request,'editar_empresa.html',context)


### vistas para las incapacidades
def incapacidad(request):
    incapacidades = Incapacidades.objects.all()
    context ={'incapacidades':incapacidades}
    return render(request,'incapacidad.html',context)

def agregar_incapacidad(request):
    if request.method =='POST':
        form = IncapacidadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('incapacidad')
    else:
        form = IncapacidadForm()
    
    context = {'form' : form}
    return render(request,'agregar_inc.html',context)

def eliminar_inc(request, id):
    incapacidad = get_object_or_404(Incapacidades, pk=id)
    if Incapacidades:
        incapacidad.delete()
    return redirect('incapacidad')

def editar_inc(request, id):
    incapacidad = get_object_or_404(Incapacidades, pk=id)
    if request.method =='POST':
        form = IncapacidadForm(request.POST, instance=incapacidad)
        if form.is_valid():
            form.save()
            return redirect('incapacidad')
    else:
        form = IncapacidadForm(instance=incapacidad)
    
    context = {'form' : form}
    return render(request,'editar_inc.html',context)