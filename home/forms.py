from django import forms

class PedidoFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    guarnicion=forms.CharField(max_length=50)
    cant_porciones=forms.IntegerField()
    fecha_pedido=forms.DateField(required=False)
    
class BusquedaPedidoFormulario(forms.Form):
    nombre=forms.CharField(max_length=50, required=False)