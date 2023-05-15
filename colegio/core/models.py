from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin

# Create your models here.

class Apoderado(models.Model):
    id_apoderado = models.AutoField( primary_key=True, verbose_name='Id Apoderado')
    nombre_usuario = models.CharField(max_length=50, verbose_name='Nombre Usuario ')
    contraseña = models.CharField(max_length=50, verbose_name='Contraseña')
    primer_nombre = models.CharField(max_length=50, verbose_name='Primer nombre')
    segundo_nombre = models.CharField(max_length=50, verbose_name='segundo nombre')
    appaterno  = models.CharField(max_length=50, verbose_name='Apellido Paterno')
    apmaterno  = models.CharField(max_length=50, verbose_name='Apellido materno')
    
    def __str__(self):
        return self.Apoderado

class Alumno(models.Model):
    id_alumno = models.AutoField (primary_key=True , verbose_name='Id Alumno')
    primer_nombre = models.CharField(max_length=50, verbose_name='Primer Nombre')
    segundo_nombre = models.CharField(max_length=50, verbose_name='Segundo Nombre')
    appaterno  = models.CharField(max_length=50, verbose_name='Apellido Paterno')
    apmaterno  = models.CharField(max_length=50, verbose_name='Apellido materno')

    def __str__(self):
        return self.Alumno


class Profesor(models.Model):
    id_profesor = models.AutoField (primary_key=True , verbose_name='Id Profesor')
    primer_nombre = models.CharField(max_length=50, verbose_name='Primer Nombre')
    segundo_nombre = models.CharField(max_length=50, verbose_name='Segundo Nombre')
    appaterno  = models.CharField(max_length=50, verbose_name='Apellido Paterno')
    apmaterno  = models.CharField(max_length=50, verbose_name='Apellido materno')
    nombre_usuario = models.CharField(max_length=50, verbose_name='Nombre Usuario ')
    contraseña = models.CharField(max_length=50, verbose_name='Contraseña')

    def __str__(self):
        return self.Profesor

class Anotaciones(models.Model):

    id_anotacion= models.AutoField (primary_key=True , verbose_name='Id Anotaciones')
    definicion= models.CharField(max_length=200, verbose_name='Definicion')

    def __str__(self):
        return self.Anotaciones

class Asistencia(models.Model):

    id_asistencia= models.AutoField (primary_key=True, verbose_name='Id Asistencia')
    fecha = models.DateField(verbose_name='Fecha')
    estado = models.CharField(max_length=200, verbose_name='Estado')

    def __str__(self):
        return self.Asistencia

class Curso(models.Model):        
    id_curso= models.AutoField(primary_key=True, verbose_name='Id Curso')
    seccion= models.CharField(max_length=50, verbose_name='Seccion')

    def __str__(self):
        return self.Curso


class Nota(models.Model):        
    id_nota= models.AutoField(primary_key=True, verbose_name='Id Nota')
    calificacion= models.CharField(max_length=50, verbose_name='Calificacion')

    def __str__(self):
        return self.Nota



