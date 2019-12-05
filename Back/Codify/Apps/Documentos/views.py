from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from Apps.Documentos import models as models_documentos
from Apps.Documentos import serializers as DocumentoSerializers

# Create your views here.
class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = models_documentos.Documento.objects.all()
    serializer_class = DocumentoSerializers.DocumentoSerializer

    @action(detail = False)
    def recent_documentos(self, request):
        recent_documentos = models_documentos.Documento.objects.all().order_by('nombre')
        serializer = self.get_serializer(recent_documentos, many=True)
        return Response(serializer.data)

class CarpetaViewSet(viewsets.ModelViewSet):
    queryset = models_documentos.Carpeta.objects.all()
    serializer_class = DocumentoSerializers.CarpetaSerializer

    @action(detail = False)
    def recent_carpetas(self, request):
        recent_carpetas = models_documentos.Carpeta.objects.all().order_by('nombre')
        serializer = self.get_serializer(recent_carpetas, many=True)
        return Response(serializer.data)