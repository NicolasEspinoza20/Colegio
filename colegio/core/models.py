from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin

# Create your models here.

class Apoderado(models.Model):
    nombre_usuario = models.CharField(max_length=50, verbose_name='Nombre Usuario ')
    contraseña = models.CharField(max_length=50, verbose_name='Contraseña')
    nombre_apoderado = models.CharField(max_length=200, verbose_name='Primer nombre')
    appaterno_apoderado  = models.CharField(max_length=50, verbose_name='Apellido Paterno')
    apmaterno_apoderado  = models.CharField(max_length=50, verbose_name='Apellido materno')
    
    def __str__(self):
        return self.nombre_usuario
    
class ApoderadoAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class Alumno(models.Model):
    run_alumno = models.CharField(max_length=8)
    dv_alumno = models.CharField(max_length=1)
    nombre_alumno = models.CharField(max_length=200, verbose_name='Primer Nombre')
    appaterno_alumno  = models.CharField(max_length=50, verbose_name='Apellido Paterno')
    apmaterno_alumno  = models.CharField(max_length=50, verbose_name='Apellido materno')
    
    def __str__(self):
        return self.nombre_alumno

class AlumnoAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class Profesor(models.Model):
    
    nombre_profesor = models.CharField(max_length=200, verbose_name='Primer Nombre')
    appaterno_profesor  = models.CharField(max_length=50, verbose_name='Apellido Paterno')
    apmaterno_profesor  = models.CharField(max_length=50, verbose_name='Apellido materno')

    def __str__(self):
        return self.nombre_profesor
    
class ProfesorAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class Anotaciones(models.Model):

    tipo_anotacion= models.CharField(max_length=200, verbose_name='Tipo anotacion')
    definicion= models.CharField(max_length=200, verbose_name='Definicion')
    id_alumno= models.ForeignKey('Alumno',on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo_anotacion
    
class AnotacionesAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class Asistencia(models.Model):

    id_curso= models.ForeignKey('Alumno', on_delete=models.CASCADE,null=True, blank=True,related_name='id_curso')
    id_alumno= models.ForeignKey('Alumno',on_delete=models.CASCADE,null=True, blank=True,related_name='id_alumno')
    fecha = models.DateField(verbose_name='Fecha')
    estado = models.CharField(max_length=200, verbose_name='Estado')

    def __str__(self):
        return self.fecha
    
class AsistenciaAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class Curso(models.Model):        
    
    
    id_alumno= models.ForeignKey('Alumno',on_delete=models.CASCADE,null=True, blank=True,related_name='id_alumno')
    id_profesor= models.ForeignKey('Profesor',on_delete=models.CASCADE,null=True, blank=True,related_name='id_profesor')
    curso= models.CharField(max_length=20, verbose_name='curso')

    def __str__(self):
        return self.curso
    
class CursoAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


class Nota(models.Model):        
    
    id_alumno= models.ForeignKey('Alumno',on_delete=models.CASCADE,null=True, blank=True,related_name='id_alumno')
    calificacion= models.CharField(max_length=50, verbose_name='Calificacion')

    def __str__(self):
        return self.calificacion
    
class NotaAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

class CustomUsuario(AbstractUser):
    is_profesor = models.BooleanField(default=False)
    is_apoderado = models.BooleanField(default=False)
    is_alumno = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class CustomUsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    



