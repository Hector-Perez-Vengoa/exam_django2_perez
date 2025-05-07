from rest_framework import viewsets
from .models import Actividad, Rutina, Ejercicio, RutinaEjercicio
from .serializers import ActividadSerializer, RutinaSerializer, EjercicioSerializer, RutinaEjercicioSerializer

class ActividadViewSet(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

class RutinaViewSet(viewsets.ModelViewSet):
    queryset = Rutina.objects.all()
    serializer_class = RutinaSerializer

class EjercicioViewSet(viewsets.ModelViewSet):
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer

class RutinaEjercicioViewSet(viewsets.ModelViewSet):
    queryset = RutinaEjercicio.objects.all()
    serializer_class = RutinaEjercicioSerializer
