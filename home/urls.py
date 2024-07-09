
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('about', views.about, name='about'),
    path('ver-pedidos', views.ver_pedidos, name='ver_pedidos'),
    path('crear-pedido', views.crear_pedido, name='crear_pedido'),
    path('home/eliminar/<int:pk>', views.EliminarPedido.as_view(), name='eliminar_pedido')

]