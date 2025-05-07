# rutinas/urls.py

from django.urls import path, include
from .views import ActividadViewSet, RutinaViewSet, EjercicioViewSet, RutinaEjercicioViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'actividades', ActividadViewSet)
router.register(r'rutinas', RutinaViewSet)
router.register(r'ejercicios', EjercicioViewSet)
router.register(r'rutinas-ejercicios', RutinaEjercicioViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Importante incluir las rutas del router
]
