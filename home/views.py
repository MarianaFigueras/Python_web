from tkinter import PIESLICE
from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
import random
from home.models import Pedido
from django.shortcuts import render, redirect
from home.forms import PedidoFormulario, BusquedaPedidoFormulario
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

def crear_pedido(request):
    formulario = PedidoFormulario(request.POST)
        
    if formulario.is_valid():
        data = formulario.cleaned_data
          
        nombre = data ['nombre']
        guarnicion = data ['guarnicion']
        cant_porciones = data['cant_porciones']
        fecha_pedido = data['fecha_pedido'] or datetime.now()
        
        pedido= Pedido(nombre=nombre, guarnicion=guarnicion, cant_porciones=cant_porciones, fecha_pedido=fecha_pedido)
        pedido.save()
        
        return redirect('ver_pedidos')
   
    formulario = PedidoFormulario()
    return render(request, 'home/crear_pedido.html', {'formulario': formulario})
    
    
def ver_pedidos(request):
    
    nombre = request.GET.get('nombre', None)
    
    if nombre:
        pedidos = Pedido.objects.filter(nombre__icontains=nombre)
    else:
        pedidos = Pedido.objects.all()
       
    formulario= BusquedaPedidoFormulario()
    
    return render(request, 'home/ver_pedidos.html', {'pedidos': pedidos, 'formulario':formulario})

def index(request):
    return render(request, 'home/index.html')

def about(request):
    return render(request, 'home/about_us.html')

class EliminarPedido(LoginRequiredMixin, DeleteView):
    model = Pedido
    success_url = '/ver-pedidos'
    template_name = 'home/eliminar_pedido_cbv.html'

