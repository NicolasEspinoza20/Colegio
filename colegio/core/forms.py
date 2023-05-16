from django import forms
from django.forms import ModelForm
from .models import Profesor

class ProfesorForm(forms.Form):
    primer_nombre = forms.CharField(max_length=50, )
    segundo_nombre = forms.CharField(max_length=50, )
    appaterno  = forms.CharField(max_length=50, )
    apmaterno  = forms.CharField(max_length=50, )

    class Meta:
        model = Profesor
        fields =  ['id_profesor', 'primer_nombre', 'segundo_nombre','appaterno','apmaterno']