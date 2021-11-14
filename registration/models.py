from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from core.types.listas_desplegables import *
from django.dispatch import receiver    # Libreria para hacer los cambios en los datos
from django.db.models.signals import post_save  # Complemento de dispatch

# Create your models here.
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    desc = models.CharField(default='describir', max_length=50)
    # imagen

    class Meta:
        ordering = ['user']

    def __str__(self):
        return f'Perfil de {self.user}'


def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename
class Profile(models.Model):
    usuario = models.OneToOneField(User, on_delete=CASCADE)
    telefono = models.CharField(max_length=20, verbose_name="Telefono", null=True, blank=True)
    celular = models.CharField(max_length=20, verbose_name="Celular", null=True, blank=True)
    direccion = models.CharField(max_length=255,verbose_name="Direccion", null=True, blank=True)
    correo = models.EmailField(max_length=255,verbose_name="Email", null=True, blank=True)
    tipo_documento = models.CharField(max_length=20, choices=Documentos,verbose_name="Genero",default="Otro")
    cedula = models.CharField(max_length=15,verbose_name="Cedula", null=True, blank=True)
    genero = models.CharField(max_length=20, choices=Generos,verbose_name="Genero",default="Otro")
    fecha_nacimiento = models.DateField(verbose_name="Fecha Nacimiento", auto_now=False)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)  
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")


    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f'Perfiles {self.cedula}'

# Función exclusiva para los usuarios logueados:
@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(usuario=instance)


class Contacto_Emergencia(models.Model):
    usuario = models.ForeignKey(User, on_delete=CASCADE)
    contacto_emergencia = models.CharField(max_length=255, verbose_name="Contacto Emergencia", null=True, blank=True)
    parentesco_emergercia = models.CharField(max_length=20,verbose_name="Parentesco", null=True, blank=True)
    telefono_emergencia = models.CharField(max_length=20, verbose_name="Telefono Emergencia", null=True, blank=True)
    create_at = models.DateField(auto_now_add=True, verbose_name="Creado el", null=True)  
    modify_at = models.DateField(auto_now=True, verbose_name="Actualizado el")

class Meta:
    verbose_name = 'Contacto'
    verbose_name_plural = 'Contactos'

def __str__(self):
    return f'Contacto {self.contacto_emergencia}'