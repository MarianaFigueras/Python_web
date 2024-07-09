from django.shortcuts import render, redirect
from menu.models import Plato
from menu.forms import PlatoFormulario, BusquedaPlatoFormulario

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def ver_platos(request):
    
    tipo_plato = request.GET.get('tipo_plato', None)
    
    if tipo_plato:
        platos = Plato.objects.filter(tipo_plato__icontains=tipo_plato)
    else:
        platos = Plato.objects.all()
    
    formulario= BusquedaPlatoFormulario()
    
    return render(request, 'menu/ver_platos.html', {'platos': platos, 'formulario':formulario})

@login_required
def crear_plato(request):
    
    if request.method =='POST':
        formulario = PlatoFormulario(request.POST, request.FILES)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            
            plato = Plato(
                tipo_plato=datos['tipo_plato'],
                nombre_plato=datos['nombre_plato'],
                precio=datos ['precio'],
                descripcion=datos ['descripcion'],
                fecha_creacion=datos ['fecha_creacion'],
                autor=datos ['autor'],
                imagen=datos ['imagen']
            )
            plato.save()
            return redirect('ver_platos')
    
    
    formulario = PlatoFormulario()
    
    return render(request,'menu/crear_plato.html', {'formulario': formulario})


class EditarPlato(LoginRequiredMixin, UpdateView):
    model = Plato
    success_url = '/menu/menu/'
    template_name = 'menu/editar_plato_cbv.html'
    fields = ['tipo_plato', 'nombre_plato', 'precio', 'autor', 'fecha_creacion', 'descripcion', 'imagen']
    
    
class EliminarPlato(LoginRequiredMixin, DeleteView):
    model = Plato
    success_url = '/menu/menu/'
    template_name = 'menu/eliminar_plato_cbv.html'
    
class VerPlato(DetailView):
    model = Plato
    template_name = 'menu/ver_plato.html'
    

