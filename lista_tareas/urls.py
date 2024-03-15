from django.urls import path
from . import views

urlpatterns = [
    # Plantilla para rutas:
    # path('', views.[nombre de la función de "views.py"])

    path('', views.index),
]