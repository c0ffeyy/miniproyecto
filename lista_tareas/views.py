from django.shortcuts import render, redirect
from .models import Tarea

# Create your views here.

tareas = Tarea.objects.all()

def index(request):
    return render(request, 'index.html', {
        'tareas': tareas
    })

def detalles_tarea(request):
    return render(request, 'detalles_tarea.html', {
        'tareas': tareas
    })

def gestion_tareas(request):
    return render(request, 'gestion_tareas.html', {
        'tareas': tareas
    })