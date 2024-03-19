from django.shortcuts import render, redirect
from .models import Tarea

# Create your views here.

def index(request):
    tareas = Tarea.objects.all()
    return render(request, 'index.html', {
        'tareas': tareas
    })

def parametro_tarea(request, id):
    tareas_id = Tarea.objects.get(id=id)
    return render(request, 'parametro_tarea.html', {
        'tareas_id': tareas_id
    })

def detalles_tareas(request):
    tareas = Tarea.objects.all()
    return render(request, 'detalles_tareas.html', {
        'tareas': tareas
    })