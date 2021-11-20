import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models.base import Model
from datetime import date
from django.db.models.deletion import CASCADE
from core.types.listas_desplegables import *
from django.dispatch import receiver            # Libreria para hacer los cambios en los datos
from registration.models import Profile


# Create your models here.

class Empresa(models.Model): ## Clase que se usara para la creación de las empresas
    nombre = models.CharField(verbose_name='Nombre de Empresa', max_length=200, null=False, blank=False)
    nit = models.CharField(verbose_name='NIT', max_length=15, null=False, blank=False)
    actividad = models.CharField(verbose_name='Actividad Económica', max_length=255, null=False, blank=False)
    nivel_riesgo = models.CharField(verbose_name='Nivel de Riesgo', max_length=255)
    direccion = models.CharField(verbose_name='Dirección', max_length=255, null=False, blank=False)
    ciudad = models.CharField(verbose_name='Ciudad', max_length=255, null=False, blank=False)
    departamento = models.CharField(verbose_name='Departamento', max_length=255, null=False, blank=False)
    cant_trabajadores = models.IntegerField(verbose_name='Cantidad de Trabajadores')
    naturaleza_empresa = models.CharField(verbose_name='Naturaleza jurídica', max_length=100, null=False, blank=False)
    telefonos = models.CharField(verbose_name='Teléfonos de contacto', max_length=40)
    correo = models.EmailField(verbose_name='Correo electrónico', max_length=255, null=False, blank=False)
    tipo = models.CharField(verbose_name='Tipo de empresa', max_length=100, null=False, blank=False)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)  
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresa'

    def __str__(self):
        return self.nombre

class Areas(models.Model):## Clase que se usara para la creación de las áreas que tiene la empresa ingresada
    nit_empresa = models.ForeignKey(Empresa, on_delete= CASCADE)
    nombre_area = models.CharField(verbose_name='Nombre Area', max_length= 255, null=False, blank=False)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")
     
    class Meta:
        verbose_name = 'Nombre Area'
        verbose_name_plural = 'Areas de la empresa'

    def __str__(self):
        return self.nombre_area


class NivelAcademico(models.Model):## Clase que se usara para la creación de los nieveles académicos o estudios de los empleados
    nivel = models.CharField(verbose_name='Nivel Académico', max_length= 255, null=False)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")
     
    class Meta:
        verbose_name = 'Nivel Académico'
        verbose_name_plural = 'Niveles Académicos'

    def __str__(self):
        return self.nivel


class Cargos(models.Model):
    cargo = models.CharField(verbose_name='Cargo', max_length= 255, null=False)
    salario_cargo = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)  
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self) -> str:
        return self.cargo


class Cie10(models.Model):
    diagnostico = models.CharField(verbose_name="Código CIE 10", max_length=4)
    grupo = models.TextField(verbose_name="Grupo de Diagnóstico")
    descripcion = models.TextField(verbose_name="Descripción de Diagnóstico")

    class Meta:
        verbose_name = 'Diagnostico'
        verbose_name_plural = 'Diagnosticos'

    def __str__(self):
        return self.diagnostico

class Incapacidades(models.Model):
    cedula  = models.ForeignKey(Profile, on_delete=CASCADE)
    origen = models.CharField(verbose_name="Origen", max_length=155)
    clasificacion = models.CharField(verbose_name="Clasificación", max_length=155)
    fecha_inicio = models.DateField(verbose_name="Fecha de Inicio", auto_now=False)
    fecha_fin = models.DateField(verbose_name="Fecha de Finalización", auto_now=False)
    archivo_inc = models.FileField(default='/static/media/archivos', verbose_name="Cargue el archivo con la incapacidad")
    total_incapacidad = models.IntegerField(verbose_name="Total días incapacidad")
    valor_incapacidad = models.DecimalField(verbose_name="Valor Incapacidad", decimal_places=2, max_digits=12)
    valor_asumido_empresa = models.DecimalField(verbose_name="Valor Asumido Empresa", decimal_places=2, max_digits=12)
    valor_asumido_eps = models.DecimalField(verbose_name="Valor Asumido EPS", decimal_places=2, max_digits=12)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el")
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

    class Meta:
        verbose_name = 'Incapacidad'
        verbose_name_plural = 'Incapacidades'

    def __str__(self):
        return f' {self.id} Incapacidad {self.clasificacion}'

class Empleado(models.Model): ## Clase destinadad a la creación de los empleados
    cedula = models.ForeignKey(Profile, on_delete=CASCADE)
    area = models.ForeignKey(Areas, on_delete=CASCADE)
    cargo = models.ForeignKey(Cargos, on_delete=CASCADE)
    nivel_academico = models.ForeignKey(NivelAcademico, on_delete=CASCADE)
    fecha_ingreso = models.DateField(verbose_name='Fecha de ingreso' )
    salario_basico = models.DecimalField(verbose_name='Salario', max_digits=12, decimal_places=2)
    arl = models.CharField(verbose_name='ARL', max_length= 100, null=False)
    tipo_contrato = models.CharField(verbose_name="Tipo Contrato",max_length=255, choices=Contrato)
    antiguedad = models.DecimalField(verbose_name="Tiempo en la empresa", max_digits=2, decimal_places=2)
    barrio = models.CharField(verbose_name="Barrio", max_length=255, null=True, default="No indicado")
    ciudad = models.CharField(verbose_name="Ciudad", max_length=255, null=False, default="No indicada")
    departamento = models.CharField(verbose_name="Departamento", max_length=255, null=False, default="No indicado")
    estrato = models.IntegerField(verbose_name="Estrato", null=True, blank=True)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")


    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return f' {self.id} Código Empleado {self.cedula}'