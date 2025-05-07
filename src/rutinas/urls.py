from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, ActividadViewSet, RutinaViewSet, EjercicioViewSet, RutinaEjercicioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'actividades', ActividadViewSet)
router.register(r'rutinas', RutinaViewSet)
router.register(r'ejercicios', EjercicioViewSet)
router.register(r'rutinas-ejercicios', RutinaEjercicioViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Incluye todas las rutas del router
]
