from rest_framework import serializers
from .models import Actividad, Rutina, Ejercicio, RutinaEjercicio

class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = ['id', 'usuario', 'tipo', 'duracion', 'fecha']

class RutinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rutina
        fields = ['id', 'nombre', 'descripcion', 'usuario']

class EjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ejercicio
        fields = ['id', 'nombre', 'descripcion']

class RutinaEjercicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RutinaEjercicio
        fields = ['id', 'rutina', 'ejercicio', 'repeticiones', 'series']
