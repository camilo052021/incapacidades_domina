from django import forms
from django.db.models import fields
from .models import *

class IncapacidadForm(forms.ModelForm):

    class Meta:
        model = Incapacidades
        fields = '__all__'

class EmpresaForm(forms.ModelForm):

    class Meta:
        model = Empresa
        fields = '__all__'