from django.db import models

# Create your models here.

class Estudiante(models.Model):
	nombre = models.CharField(max_length=10, null=True, blank=True)
	apellido = models.CharField(max_length=10, null=True, blank=True)
	cedula = models.CharField(max_length=10, unique=True)
	estatus = models.CharField(max_length=1, null=True, blank=True)

	def __str__(self):
		return '{}'.format(self.nombre)