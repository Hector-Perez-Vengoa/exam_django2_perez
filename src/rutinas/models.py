from django.db import models
from django.contrib.auth.models import User

class Actividad(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=100)
    duracion = models.DurationField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.tipo} - {self.duracion}"

class Rutina(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Ejercicio(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class RutinaEjercicio(models.Model):
    rutina = models.ForeignKey(Rutina, related_name='ejercicios', on_delete=models.CASCADE)
    ejercicio = models.ForeignKey(Ejercicio, on_delete=models.CASCADE)
    repeticiones = models.PositiveIntegerField()
    series = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.rutina.nombre} - {self.ejercicio.nombre}"
