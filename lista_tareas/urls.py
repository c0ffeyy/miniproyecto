from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('detalles_tarea/', views.detalles_tarea),
    path('gestion_tareas/', views.gestion_tareas),
]