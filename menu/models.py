from msilib.schema import Upgrade
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Plato(models.Model):
    tipo_plato=models.CharField(max_length=50)
    nombre_plato=models.CharField(max_length=50)
    descripcion=RichTextField(null=True)
    precio=models.IntegerField()
    fecha_creacion=models.DateField(null=True)
    autor=models.CharField(max_length=50,null=True)
    imagen=models.ImageField(upload_to='avatares',null=True, blank=True)
    
    def __str__(self):
        return f'Tipo: {self.tipo_plato} - Nombre: {self.nombre_plato} - Precio: {self.precio}'

