from django.contrib import admin

# Register your models here.
from Usuarios.models import *
from tienda.snniper import Attr

class CiudadesInline(admin.StackedInline):
    model = Ciudades
    extra = 0

@admin.register(Provincias)
class modelo(admin.ModelAdmin):
    list_display =Attr(Provincias)
    list_display_links = Attr(Provincias)
    inlines = [CiudadesInline,]

@admin.register(Ciudades)
class modelo(admin.ModelAdmin):
    list_display =Attr(Ciudades)
    list_display_links = Attr(Ciudades)

@admin.register(Perfiles)
class modelo(admin.ModelAdmin):
    list_display =Attr(Perfiles)
    list_display_links = Attr(Perfiles)

@admin.register(Direcciones)
class modelo(admin.ModelAdmin):
    list_display =Attr(Direcciones)
    list_display_links = Attr(Direcciones)
