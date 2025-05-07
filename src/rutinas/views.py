from rest_framework import viewsets
from .models import Usuario, Actividad, Rutina, Ejercicio, RutinaEjercicio
from .serializers import UsuarioSerializer, ActividadSerializer, RutinaSerializer, EjercicioSerializer, RutinaEjercicioSerializer

# Vista para el modelo Usuario
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

# Vista para las actividades
class ActividadViewSet(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer

# Vista para las rutinas
class RutinaViewSet(viewsets.ModelViewSet):
    queryset = Rutina.objects.all()
    serializer_class = RutinaSerializer

# Vista para los ejercicios
class EjercicioViewSet(viewsets.ModelViewSet):
    queryset = Ejercicio.objects.all()
    serializer_class = EjercicioSerializer

# Vista para los ejercicios dentro de las rutinas
class RutinaEjercicioViewSet(viewsets.ModelViewSet):
    queryset = RutinaEjercicio.objects.all()
    serializer_class = RutinaEjercicioSerializer
