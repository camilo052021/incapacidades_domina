from django import forms
from django.db.models import fields
from .models import *

class IncapacidadForm(forms.ModelForm):

    class Meta:
        model = Incapacidades
        fields = '__all__'

        widgets = {
            'cedula' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Cédula'}),
            'origen' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Tipo Consulta'}),
            'clasificacion' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Tipo Enfermedad'}), 
            'fecha_inicio' : forms.DateInput(format=('%Y-%m-%d'),attrs = {'class':'form-control mt-2', 'type':'date'}),
            'fecha_fin' : forms.DateInput(format=('%Y-%m-%d'),attrs = {'class':'form-control mt-2', 'type':'date'}),  
            'total_incapacidad' : forms.NumberInput(attrs = {'class':'form-control mt-2', 'placeholder':'Días Incapacidad'}),
            'archivo_inc' : forms.ClearableFileInput(attrs = {'class':'form-control mt-2'}),
            'valor_incapacidad' : forms.NumberInput(attrs = {'class':'form-control mt-2', 'placeholder':'Valor Incapacidad'}),
            'valor_asumido_empresa' : forms.NumberInput(attrs = {'class':'form-control mt-2', 'placeholder':'Valor Empresa'}),
            'valor_asumido_eps' : forms.NumberInput(attrs = {'class':'form-control mt-2', 'placeholder':'Valor EPS'}),
                  
        }

class EmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresa
        fields = '__all__'

        widgets = {
            'nombre' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Nombre'}),
            'nit' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Nit'}),
            'actividad' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Actividad'}),
            'nivel_riesgo' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Nivel Riesgo'}),
            'direccion' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Dirección'}),
            'ciudad' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Ciudad'}),
            'departamento' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Departamento'}),
            'cant_trabajadores' : forms.NumberInput(attrs = {'class':'form-control mt-2', 'placeholder':'Trabajadores'}),
            'naturaleza_empresa' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Naturaleza'}),
            'telefonos' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Teléfonos'}),
            'correo' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Correo'}),
            'tipo' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Tipo Capital'}),
        }

class AreaForm(forms.ModelForm):

    class Meta:
        model = Areas
        fields = '__all__'
        widgets = {
            'nit_empresa' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Nit'}),
            'nombre_area' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Nombre Area'}),
            'centro_costo' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Cecos'}),
        }


class NivelAcademicoForm(forms.ModelForm):

    class Meta:
        model = NivelAcademico
        fields = '__all__'
        widgets = {
            'nivel' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Nivel'}),
        }

class CargoForm(forms.ModelForm):

    class Meta:
        model = Cargos
        fields = '__all__'        
        widgets = {
            'cargo' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Cargo'}),
            'salario_cargo' : forms.NumberInput(attrs = {'class':'form-control mt-2', 'placeholder':'Salario'}),
        }
class EmpleadoForm(forms.ModelForm):

    class Meta:
        model = Empleado
        fields = '__all__'    

        widgets = {
            'cedula' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Cédula'}),
            'area' : forms.NumberInput(attrs = {'class':'form-control mt-2', 'placeholder':'Área'}),
            'cargo' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Cargo'}),
            'nivel_academico' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Nivel'}),
            'fecha_ingreso' : forms.DateInput(format=('%Y-%m-%d'),attrs = {'class':'form-control mt-2', 'type':'date'}),
            'salario_basico' : forms.NumberInput(attrs = {'class':'form-control mt-2', 'placeholder':'Salario'}),
            'arl' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Arl'}),
            'tipo_contrato' : forms.Select(attrs = {'class':'form-control mt-2'}),
            'antiguedad' : forms.NumberInput(attrs = {'class':'form-control mt-2', 'placeholder':'Antiguedad'}),
            'barrio' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Barrio'}),
            'ciudad' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Ciudad'}),
            'departamento' : forms.TextInput(attrs = {'class':'form-control mt-2', 'placeholder':'Departamento'}),
            'estrato' : forms.NumberInput(attrs = {'class':'form-control mt-2', 'placeholder':'Estrato'}),
        }