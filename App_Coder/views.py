from django.http import HttpResponse
from django.shortcuts import render

from App_Coder.models import Curso

# Create your views here.

def curso (self, nombre, camada):

    curso = Curso(nombre = nombre, camada = camada)
    curso.save()

    return HttpResponse(f"""
        <p>Curso: {curso.nombre} - Camada: {curso.camada} agregado</p>
    """)

