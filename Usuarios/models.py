from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Provincias(models.Model):
    nombre=models.CharField(max_length=60)

    class Meta:
        verbose_name_plural="1. Provincias"

    def __str__(self):
        return self.nombre

class Ciudades(models.Model):
    provincia=models.ForeignKey(Provincias,on_delete=models.CASCADE)
    nombre=models.CharField(max_length=60)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural="2. Ciudades"


class Perfiles(models.Model):
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    tipo=models.CharField(max_length=30,choices=(("T","T"),("U","U")))
    cedula=models.CharField(max_length=13)

    class Meta:
        verbose_name_plural="3. Perfiles"


class Direcciones(models.Model):
    perfil=models.ForeignKey(Perfiles,on_delete=models.CASCADE)
    preguntar_por=models.CharField(max_length=60)
    ciudad = models.ForeignKey(Ciudades, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=120)
    referencias=models.TextField()
    telefono = models.CharField(max_length=13)

    class Meta:
        verbose_name_plural="4. Direcciones"





