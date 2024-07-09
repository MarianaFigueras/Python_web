from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm


class MiFormularioDeCreacion(UserCreationForm):
    
    email = forms.EmailField()
    genero = forms.CharField()
    password1 = forms.CharField(label='Contrasenia', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir Contrasenia', widget=forms.PasswordInput)
    avatar = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['username','email','genero','password1','password2', 'avatar']
        help_texts = {key: '' for key in fields}
        
class EditarPerfilFormulario(forms.Form):
    email = forms.CharField()
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    genero = forms.CharField()
    avatar = forms.ImageField(required=False)
     
class MiCambioDePassword(PasswordChangeForm):
    old_password = forms.CharField(label='Contrasenia vieja', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='Contrasenia nueva', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Repetir Contrasenia nueva', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']
        help_texts = {key: '' for key in fields}