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
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
import os
import io
import subprocess
from django.utils.encoding import smart_str
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def codigo(request):
    if request.method == 'POST':
        # print(request.POST.get("codigo"))
        try:
            with io.open("Code/user1/Untitled.py", 'w', encoding='utf8') as f:
                f.write(request.POST.get("codigo").replace(u'\xa0', u' '))
            exec_command = subprocess.Popen("python Code/user1/Untitled.py", stdout=subprocess.PIPE)
            # with io.open(ruta, 'r', encoding='utf8') as f:
            #    text = f.read()
            return HttpResponse(exec_command.stdout.read())
        except:
            os.mkdir("Code/user1")
            with io.open("Code/user1/Untitled.py", 'w', encoding='utf8') as f:
                f.write(request.POST.get("codigo").replace(u'\xa0', u' '))
            exec_command = subprocess.Popen("python Code/user1/Untitled.py", stdout=subprocess.PIPE)
            # with io.open(ruta, 'r', encoding='utf8') as f:
            #    text = f.read()
            return HttpResponse(exec_command.stdout.read())

@csrf_exempt
def descargar(request):
    filename = "Code/user1/Untitled.py"
    with io.open(filename, 'r', encoding='utf8') as f:
        text = f.read()
    response = HttpResponse(text,content_type ='application/force-download') # mimetype is replaced by content_type for django 1.7
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename)
    response['X-Sendfile'] = smart_str("Code/user1/")
    print(response)
    return response

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

def crearCarpeta(request):
    if requet.method == 'POST':
        os.mkdir(os.path.join(BASE_DIR + '/Code', request.POST.get('carpeta')))
        return HttpResponse("Listo xd")
@csrf_exempt
def mkdir(request):
    usuario = request.POST.get("user")
    os.mkdir("Code/%s"%usuario)