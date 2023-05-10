from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def anotaciones(request):
    return render(request,'anotaciones.html')

def asistencia(request):
    return render(request,'asistencia.html')

def login(request):
    return render(request,'login.html')
    
def meni(request):
    return render(request,'menu.html')

def notas(request):
    return render(request,'notas.html')