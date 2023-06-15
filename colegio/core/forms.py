from django import forms
from django.forms import ModelForm
from .models import Profesor,Alumno,Apoderado

#lista alumno
def lista_alumno():
    lista_alumno = ()
    lista_alumno = list(lista_alumno)
    Alumno = Alumno.objects.all()
    for a in Alumno:
        lista_alumno.append([a.id, str(a.nombre_alumno + ' ' + a.appaterno_alumno)])
    lista_alumno = tuple(lista_alumno)
    return lista_alumno

#lista profesor
def lista_profesor():
    lista_profesor = ()
    lista_profesor = list(lista_profesor)
    Profesor = Profesor.objects.all()
    for p in Profesor:
        lista_profesor.append([p.id, str(p.nombre_profesor + ' ' + p.appaterno_profesor)])
    lista_profesor = tuple(lista_profesor)
    return lista_profesor

#lista apoderado
def lista_apoderado():
    lista_apoderado = ()
    lista_apoderado = list(lista_apoderado)
    Apoderado = Apoderado.objects.all()
    for ap in Apoderado:
        lista_apoderado.append([ap.id, str(ap.nombre_apoderado + ' ' + ap.appaterno_apoderado)])
    lista_apoderado = tuple(lista_apoderado)
    return lista_apoderado


#definir los forms igual al models 

class ProfesorForm(forms.Form):
    nombre_profesor = forms.CharField(max_length=50, )
    appaterno_profesor  = forms.CharField(max_length=50, )
    apmaterno_profesor  = forms.CharField(max_length=50, )

    class Meta:
        model = Profesor
        fields =  ['id_profesor', 'nombre_profesor','appaterno_profesor','apmaterno_profesor']

class AlumnoForm(forms.Form):
    run_alumno = forms.CharField(max_length=8)
    dv_alumno = forms.CharField(max_length=1)
    nombre_alumno = forms.CharField(max_length=50, )
    appaterno_alumno  = forms.CharField(max_length=50, )
    apmaterno_alumno  = forms.CharField(max_length=50, )

    class Meta:
        model = Alumno
        fields =  ['id_alumno','nombre_alumno','run_alumno','dv_alumno','appaterno_alumno','apmaterno_alumno']

class ApoderadoForm(forms.Form):
    nombre_usuario = forms.CharField(max_length=50, )
    contraseña = forms.CharField(max_length=50, )
    nombre_apoderado = forms.CharField(max_length=50, )
    appaterno_apoderado  = forms.CharField(max_length=50, )
    apmaterno_apoderado  = forms.CharField(max_length=50, )

    class Meta:
        model = Apoderado
        fields =  ['id_apoderado','nombre_usuario','contraseña','nombre_apoderado','appaterno_apoderado','apmaterno_apoderado']