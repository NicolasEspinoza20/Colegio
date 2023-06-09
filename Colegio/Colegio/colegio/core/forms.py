from django import forms
from django.forms import ModelForm
from .models import Profesor,Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProfesorForm(forms.Form):
    primer_nombre = forms.CharField(max_length=50, )
    segundo_nombre = forms.CharField(max_length=50, )
    appaterno  = forms.CharField(max_length=50, )
    apmaterno  = forms.CharField(max_length=50, )

    class Meta:
        model = Profesor
        fields =  ['id_profesor', 'primer_nombre', 'segundo_nombre','appaterno','apmaterno']



class RegistroForm(UserCreationForm):
    username = forms.CharField(max_length=50, )
    email = forms.CharField(max_length=50, )
    password  = forms.CharField(max_length=50, widget=forms.PasswordInput)
    password2  = forms.CharField(max_length=50, widget=forms.PasswordInput )

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2')