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


### vista para las Areas
def area(request):
    areas = Areas.objects.all()
    context ={'areas':areas}
    return render(request,'area.html',context)

def agregar_area(request):
    if request.method =='POST':
        form = AreaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('area')
    else:
        form = AreaForm()
    
    context = {'form' : form}
    return render(request,'agregar_area.html',context)

def eliminar_area(request, id):
    area = get_object_or_404(Areas, pk=id)
    if Areas:
        area.delete()
    return redirect('area')

def editar_area(request, id):
    area = get_object_or_404(Areas, pk=id)
    if request.method =='POST':
        form = AreaForm(request.POST, instance=area)
        if form.is_valid():
            form.save()
            return redirect('area')
    else:
        form = AreaForm(instance=area)
    
    context = {'form' : form}
    return render(request,'editar_area.html',context)


### vista para los niveles Academicos
def nivel_academico(request):
    niveles_academicos = NivelAcademico.objects.all()
    context ={'niveles_academicos':niveles_academicos}
    return render(request,'nivel_academico.html',context)

def agregar_nivel_academico(request):
    if request.method =='POST':
        form = NivelAcademicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nivel_academico')
    else:
        form = NivelAcademicoForm()
    
    context = {'form' : form}
    return render(request,'agregar_nivel_academico.html',context)

def eliminar_nivel_academico(request, id):
    nivel_academico = get_object_or_404(NivelAcademico, pk=id)
    if NivelAcademico:
        nivel_academico.delete()
    return redirect('nivel_academico')

def editar_nivel_academico(request, id):
    nivel_academico = get_object_or_404(NivelAcademico, pk=id)
    if request.method =='POST':
        form = NivelAcademicoForm(request.POST, instance=nivel_academico)
        if form.is_valid():
            form.save()
            return redirect('nivel_academico')
    else:
        form = NivelAcademicoForm(instance=nivel_academico)
    
    context = {'form' : form}
    return render(request,'editar_nivel_academico.html',context)



### vistas para los cargos
def cargo(request):
    cargos = Cargos.objects.all()
    context ={'cargos':cargos}
    return render(request,'cargo.html',context)

def agregar_cargo(request):
    if request.method =='POST':
        form = CargoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cargo')
    else:
        form = CargoForm()
    
    context = {'form' : form}
    return render(request,'agregar_cargo.html',context)

def eliminar_cargo(request, id):
    cargo = get_object_or_404(Cargos, pk=id)
    if Cargos:
        cargo.delete()
    return redirect('cargo')

def editar_cargo(request, id):
    cargo = get_object_or_404(Cargos, pk=id)
    if request.method =='POST':
        form = CargoForm(request.POST, instance=cargo)
        if form.is_valid():
            form.save()
            return redirect('cargo')
    else:
        form = CargoForm(instance=cargo)
    
    context = {'form' : form}
    return render(request,'editar_cargo.html',context)


### vistas para los Empleados
def empleado(request):
    empleados = Empleado.objects.all()
    context ={'empleados': empleados}
    return render(request,'empleado.html',context)

def agregar_empleado(request):
    if request.method =='POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empleado')
    else:
        form = EmpleadoForm()
    
    context = {'form' : form}
    return render(request,'agregar_empleado.html',context)

def eliminar_empleado(request, id):
    empleado = get_object_or_404(Empleado, pk=id)
    if Empleado:
        empleado.delete()
    return redirect('empleado')

def editar_empleado(request, id):
    empleado = get_object_or_404(Empleado, pk=id)
    if request.method =='POST':
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('empleado')
    else:
        form = EmpleadoForm(instance=empleado)
    
    context = {'form' : form}
    return render(request,'editar_empleado.html',context)


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