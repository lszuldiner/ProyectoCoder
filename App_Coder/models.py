from operator import length_hint
from django.db import models

# Create your models here.
class Curso(models.Model):
    
    nombre = models.CharField(max_length=50)
    camada = models.IntegerField()


class Estudiante(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()


class Profesor(models.Model):

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

class Entregable(models.Model):

    nombre = models.CharField(max_length=30)
    fechaDeEntrega = models.CharField
    entregado = models.BooleanField()
