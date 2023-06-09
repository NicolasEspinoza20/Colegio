# Generated by Django 4.1.7 on 2023-05-15 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id_alumno', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Alumno')),
                ('primer_nombre', models.CharField(max_length=50, verbose_name='Primer Nombre')),
                ('segundo_nombre', models.CharField(max_length=50, verbose_name='Segundo Nombre')),
                ('appaterno', models.CharField(max_length=50, verbose_name='Apellido Paterno')),
                ('apmaterno', models.CharField(max_length=50, verbose_name='Apellido materno')),
            ],
        ),
        migrations.CreateModel(
            name='Anotaciones',
            fields=[
                ('id_anotacion', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Anotaciones')),
                ('definicion', models.CharField(max_length=200, verbose_name='Definicion')),
            ],
        ),
        migrations.CreateModel(
            name='Apoderado',
            fields=[
                ('id_apoderado', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Apoderado')),
                ('nombre_usuario', models.CharField(max_length=50, verbose_name='Nombre Usuario ')),
                ('contraseña', models.CharField(max_length=50, verbose_name='Contraseña')),
                ('primer_nombre', models.CharField(max_length=50, verbose_name='Primer nombre')),
                ('segundo_nombre', models.CharField(max_length=50, verbose_name='segundo nombre')),
                ('appaterno', models.CharField(max_length=50, verbose_name='Apellido Paterno')),
                ('apmaterno', models.CharField(max_length=50, verbose_name='Apellido materno')),
            ],
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id_asistencia', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Asistencia')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('estado', models.CharField(max_length=200, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id_curso', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Curso')),
                ('seccion', models.CharField(max_length=50, verbose_name='Seccion')),
            ],
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id_nota', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Nota')),
                ('calificacion', models.CharField(max_length=50, verbose_name='Calificacion')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id_profesor', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Profesor')),
                ('primer_nombre', models.CharField(max_length=50, verbose_name='Primer Nombre')),
                ('segundo_nombre', models.CharField(max_length=50, verbose_name='Segundo Nombre')),
                ('appaterno', models.CharField(max_length=50, verbose_name='Apellido Paterno')),
                ('apmaterno', models.CharField(max_length=50, verbose_name='Apellido materno')),
                ('nombre_usuario', models.CharField(max_length=50, verbose_name='Nombre Usuario ')),
                ('contraseña', models.CharField(max_length=50, verbose_name='Contraseña')),
            ],
        ),
    ]
