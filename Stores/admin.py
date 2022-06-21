from django.contrib import admin

# Register your models here.
from Stores.models import *
from tienda.snniper import Attr


@admin.register(Tiendas)
class modelo(admin.ModelAdmin):
    list_display = Attr(Tiendas)
    list_display_links = Attr(Tiendas)

@admin.register(Categorias)
class modelo(admin.ModelAdmin):
    list_display = Attr(Categorias)
    list_display_links = Attr(Categorias)


@admin.register(Productos)
class modelo(admin.ModelAdmin):
    list_display = Attr(Productos)
    list_display_links = Attr(Productos)
    readonly_fields = ['iva','total',]