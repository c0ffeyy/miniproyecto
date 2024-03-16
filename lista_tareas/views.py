from django.shortcuts import render, redirect
from .models import Tarea
from .forms import TareaForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def detalles_tarea(request):
    return render(request, 'detalles_tarea.html')

def gestion_tareas(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TareaForm()
    
    return render(request, 'gestion_tareas.html', {'form': form})