from django.urls import path
from menu import views

urlpatterns = [
    #vistas comunes
    path('menu/', views.ver_platos, name='ver_platos'),
    path('menu/crear/', views.crear_plato, name='crear_plato'),
       
   #cbv
    path('menu/editar/<int:pk>', views.EditarPlato.as_view(), name='editar_plato'),
    path('menu/eliminar/<int:pk>', views.EliminarPlato.as_view(), name='eliminar_plato'),
    path('menu/pages/<int:pk>', views.VerPlato.as_view(), name='ver_plato')
    
    
]
