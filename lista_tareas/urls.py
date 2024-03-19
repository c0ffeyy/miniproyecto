from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('lista_tareas/<int:id>', views.parametro_tarea),
    path('detalles_tareas/', views.detalles_tareas),
]