# coding: utf-8
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from Usuarios.models import Ciudades


class Tiendas(models.Model):
    usuario= models.ForeignKey(User,on_delete=models.CASCADE)
    logo=models.ImageField(upload_to="logos",default="tienda_mia.png")
    razon_social=models.CharField(max_length=200)
    ciudad=models.ForeignKey(Ciudades,on_delete=models.CASCADE)
    telefono=models.CharField(max_length=13)
    direccion=models.CharField(max_length=120)

    def __str__(self):
        return self.razon_social

class Categorias(models.Model):
    nombre=models.CharField(max_length=60)
    detalle=models.TextField()

    def __str__(self):
        return self.nombre

class Productos(models.Model):
    categoria=models.ForeignKey(Categorias,on_delete=models.CASCADE,null=True,blank=True)
    fecha=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    tienda=models.ForeignKey(Tiendas,on_delete=models.CASCADE)
    portada=models.ImageField(upload_to='imagenes',null=True,blank=True)
    nombre=models.CharField(max_length=120)
    descripcion=models.TextField(null=True,blank=True)
    tamanio=models.CharField(max_length=30, default="Pequeño")
    porciones=models.IntegerField(default=1)

    calificacion=models.DecimalField(max_digits=9, decimal_places=2, default=0)
    en_oferta=models.BooleanField(default=False)
    retiro_en=models.CharField(default="Domicilio", max_length=30)
    graba_iva = models.BooleanField(default=False)
    precio = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    iva = models.DecimalField(max_digits=9, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=9, decimal_places=2, default=0)


    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if self.graba_iva:
            precio=float(self.precio)
            iva=precio * 0.12
            self.iva=iva
            self.total=precio+iva
        else:
            self.total=self.precio
            self.iva=0
        
        super(Productos, self).save()

