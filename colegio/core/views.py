from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def anotaciones(request):
    return render(request,'core/anotaciones.html')

def asistencia(request):
    return render(request,'core/asistencia.html')

def login(request):
    return render(request,'core/login.html')
    
def meni(request):
    return render(request,'core/menu.html')

def notas(request):
    return render(request,'core/notas.html')