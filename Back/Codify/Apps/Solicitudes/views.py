from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from Apps.Solicitudes import models as models_solicitudes
from Apps.Solicitudes import serializers as SolicitudesSerializers

# Create your views here.
class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = models_solicitudes.Acceso.objects.all()
    serializer_class = SolicitudesSerializers.SolicitudSerializer