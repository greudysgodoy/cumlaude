from rest_framework.serializers import ModelSerializer
from cumlaudeUcla.models import Estudiante
from rest_framework import serializers

class EstudianteSerializer(ModelSerializer):
	class Meta:
		model = Estudiante
		fields = ('nombre','apellido','cedula','estatus')

