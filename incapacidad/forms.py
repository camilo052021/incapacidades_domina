from django import forms
from django.db.models import fields
from .models import Incapacidades

class IncpacidadForm(forms.ModelForm):

    class Meta:
        model = Incapacidades
        fields = [
            'mes',
            'origen',
            'clasificacion',
            'fecha_inicio',
            'fecha_fin',
            'archivo_inc',
            'total_incapacidad',
            'valor_incapacidad',
            'valor_asumido_empresa',
            'valor_asumido_eps',
            ]