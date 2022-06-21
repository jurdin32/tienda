from random import randint

from django.shortcuts import render

# Create your views here.
from Stores.models import Productos, Tiendas


def index(request):
    productos=Productos.objects.order_by('-fecha')
    productoss=None
    en_oferta=productos.filter(en_oferta=True)
    aletorio=randint(0,en_oferta.count()-1)
    if productos.count()>=12:
        productoss=productos[:12]
    else:
        productoss = productos

    if productos.count()>=36:
        productos=productos[:36]

    print("Ultimos 4:",productoss)
    print("Ultimos 36:", productos)
    contexto={
        'datos_productos':productoss,
        'productos':productos,
        'oferta':en_oferta[aletorio],
        'tiendas':Tiendas.objects.all().order_by('-id'),
    }
    return render(request,'index.html',contexto)

def detalles_producto(request):
    productos=None
    producto=None
    if request.GET.get('id'):
        producto=Productos.objects.get(id=request.GET.get('id'))
        productos= Productos.objects.filter(categoria=producto.categoria)
    contexto={
        'producto':producto,
        'productos':productos,
    }
    return render(request,'product_detail.html',contexto)