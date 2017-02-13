from django.shortcuts import render
from cumlaudeUcla.models import Estudiante
from rest_framework import viewsets
from cumlaudeUcla.serializers import EstudianteSerializer
from rest_framework.response import Response
import json
import codecs

class EstudianteViewSet(viewsets.ModelViewSet):
	queryset = Estudiante.objects.all()
	serializer_class = EstudianteSerializer

	def retrieve(self, request, pk):
		queryset = Estudiante.objects.get(cedula=pk)
		if (queryset != None):
			print(queryset.nombre)
			return Response({'ok' : 'true'})
		else:
			return Response({'ok' : 'false', 'error' : "No es egresado"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)