from django import forms
from ckeditor.fields import RichTextFormField

class PlatoFormulario(forms.Form):
    tipo_plato=forms.CharField(max_length=50)
    nombre_plato=forms.CharField(max_length=50)
    precio=forms.IntegerField()
    fecha_creacion=forms.DateField(required=False)
    autor=forms.CharField(max_length=50)
    imagen = forms.ImageField(required=False)
    descripcion=RichTextFormField(required=False)
    
class BusquedaPlatoFormulario(forms.Form):
    tipo_plato=forms.CharField(max_length=50, required=False)