from django.shortcuts import render
from django.http import HttpResponse
from .models import Profesor
from .forms import ProfesorForm

def asistencia(request):
    return render(request,'asistencia.html')

def login(request):
    return render(request,'login.html')
    
def menu(request):
    return render(request,'menu.html')

def notas(request):
    return render(request,'notas.html')

def anotaciones(request):
    profesor= Profesor.objects.all()
    datos = {
        'profesor':profesor
    }

    return render(request,'anotaciones.html')

def donacion(request):
    return render(request,'Donacion.html')