from django.db import models


# Create your models here.
class Pedido(models.Model):
    nombre=models.CharField(max_length=50)
    guarnicion=models.CharField(max_length=50)
    cant_porciones=models.IntegerField()
    fecha_pedido=models.DateField(null=True)
    
    def __str__(self):
        return f'{self.nombre} {self.guarnicion}'

