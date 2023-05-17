from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Profesor,Usuario
from .forms import ProfesorForm, RegistroForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView


@login_required
def asistencia(request):
    return render(request,'asistencia.html')

def is_staff(user):
    return (user.is_authenticated and user.is_superuser)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('menu')
        else:
            # Mostrar un mensaje de error de inicio de sesión
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    else:
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
    
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

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})