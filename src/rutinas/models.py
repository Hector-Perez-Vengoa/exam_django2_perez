from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    nombre = models.CharField(max_length=200)
    correo = models.EmailField(unique=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    edad = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre

# Modelo para registrar las actividades físicas del usuario
class Actividad(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Relación con el modelo Usuario
    tipo = models.CharField(max_length=100)  # Tipo de actividad (ej. correr, nadar, etc.)
    duracion = models.DurationField()  # Duración de la actividad
    fecha = models.DateTimeField(auto_now_add=True)  # Fecha de la actividad

    def __str__(self):
        return f"{self.usuario.nombre} - {self.tipo} - {self.duracion}"

# Modelo para crear rutinas de ejercicios
class Rutina(models.Model):
    nombre = models.CharField(max_length=200)  # Nombre de la rutina
    descripcion = models.TextField()  # Descripción de la rutina
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)  # Relación con el modelo Usuario

    def __str__(self):
        return self.nombre

# Modelo para registrar los ejercicios disponibles
class Ejercicio(models.Model):
    nombre = models.CharField(max_length=200)  # Nombre del ejercicio
    descripcion = models.TextField()  # Descripción del ejercicio

    def __str__(self):
        return self.nombre

# Modelo para asociar ejercicios a rutinas
class RutinaEjercicio(models.Model):
    rutina = models.ForeignKey(Rutina, related_name='ejercicios', on_delete=models.CASCADE)  # Relación con Rutina
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)  # Relación con Ejercicio
    repeticiones = models.PositiveIntegerField()  # Número de repeticiones
    series = models.PositiveIntegerField()  # Número de series

    def __str__(self):
        return f"{self.rutina.nombre} - {self.ejercicio.nombre}"
