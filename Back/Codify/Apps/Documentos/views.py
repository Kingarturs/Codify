from django.shortcuts import render, redirect
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
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
        code = request.POST.get("codigo").replace(u'\xa0', u' ')
        dir = request.POST.get("dir")
        estado = request.POST.get("estado")
        print("Code/%s/%s"%(request.session['sesion'],estado))
        if(dir == ""):
            with io.open("Code/%s/%s"%(request.session['sesion'],estado), 'w', encoding='utf8') as f:
                f.write(code)
            exec_command = subprocess.Popen("python Code/%s/%s"%(request.session['sesion'],estado), stdout=subprocess.PIPE)
            # with io.open(ruta, 'r', encoding='utf8') as f:
            #    text = f.read()
            return HttpResponse(exec_command.stdout.read())
        else:
            with io.open("Code/%s/%s/%s"%(request.session['sesion'],dir,estado), 'w', encoding='utf8') as f:
                f.write(code)
            exec_command = subprocess.Popen("python Code/%s/%s/%s"%(request.session['sesion'],dir,estado), stdout=subprocess.PIPE)
            # with io.open(ruta, 'r', encoding='utf8') as f:
            #    text = f.read()
            return HttpResponse(exec_command.stdout.read())

@csrf_exempt
def descargar(request,name,dir):
    print(name)
    print(dir)
    if dir == "a57f389a2d5e57b02b3f2225814ae13e":
        filename = "Code/%s/%s"%(request.session['sesion'],name)
        with io.open(filename, 'r', encoding='utf8') as f:
            text = f.read()
        response = HttpResponse(text,content_type ='application/force-download') # mimetype is replaced by content_type for django 1.7
        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename)
        response['X-Sendfile'] = smart_str("Code/%s/"%(request.session['sesion']))
        return response
    else:
        filename = "Code/%s/%s/%s"%(request.session['sesion'],dir,name)
        with io.open(filename, 'r', encoding='utf8') as f:
            text = f.read()
        response = HttpResponse(text,content_type ='application/force-download') # mimetype is replaced by content_type for django 1.7
        response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(filename)
        response['X-Sendfile'] = smart_str("Code/%s/%s"%(request.session['sesion'],dir))
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
    try:
        os.listdir("Code/%s"%usuario)
    except:
        os.mkdir("Code/%s"%usuario)
        with io.open("Code/%s/main.py"%usuario, 'w', encoding='utf8') as f:
                f.write("print('hola mundo')")
@csrf_exempt
def carpeta(request):
    nombre = request.POST.get("nombre")
    dirs = os.listdir("code/%s"%request.session['sesion'])
    if not (nombre in dirs):
        os.mkdir("code/%s/%s"%(request.session['sesion'],nombre))
        carpetas = {}
        for base, dirs, files in os.walk("code/%s"%request.session['sesion']):
            for i in dirs:
                carpetas[i] = os.listdir("code/%s/%s"%(request.session['sesion'],i))
            carpetas[""] = files
            break
        return JsonResponse(carpetas, safe=False)
    else:
        return HttpResponse("La carpeta ya existe")
@csrf_exempt
def archivo(request):
    nombre = request.POST.get("nombre")
    directorio = request.POST.get("directorio")
    tipo = request.POST.get("tipo")
    if tipo =="Python":
        if directorio != "":
            with io.open("Code/%s/%s/%s.py"%(request.session['sesion'],directorio,nombre), 'w', encoding='utf8') as f:
                    f.write("")
            carpetas = {}
            for base, dirs, files in os.walk("code/%s"%request.session['sesion']):
                for i in dirs:
                    carpetas[i] = os.listdir("code/%s/%s"%(request.session['sesion'],i))
                carpetas[""] = files
                break
            return JsonResponse(carpetas, safe=False)
        else:
            with io.open("Code/%s/%s.py"%(request.session['sesion'],nombre), 'w', encoding='utf8') as f:
                    f.write("")
            carpetas = {}
            for base, dirs, files in os.walk("code/%s"%request.session['sesion']):
                for i in dirs:
                    carpetas[i] = os.listdir("code/%s/%s"%(request.session['sesion'],i))
                carpetas[""] = files
                break
            return JsonResponse(carpetas, safe=False)
    else:
        if directorio != "":
            with io.open("Code/%s/%s/%s.js"%(request.session['sesion'],directorio,nombre), 'w', encoding='utf8') as f:
                    f.write("")
            carpetas = {}
            for base, dirs, files in os.walk("code/%s"%request.session['sesion']):
                for i in dirs:
                    carpetas[i] = os.listdir("code/%s/%s"%(request.session['sesion'],i))
                carpetas[""] = files
                break
            return JsonResponse(carpetas, safe=False)
        else:
            with io.open("Code/%s/%s.js"%(request.session['sesion'],nombre), 'w', encoding='utf8') as f:
                    f.write("")
            carpetas = {}
            for base, dirs, files in os.walk("code/%s"%request.session['sesion']):
                for i in dirs:
                    carpetas[i] = os.listdir("code/%s/%s"%(request.session['sesion'],i))
                carpetas[""] = files
                break
            return JsonResponse(carpetas, safe=False)
@csrf_exempt
def getCodigo(request):
    nombre = request.POST.get("nombre")
    dir = request.POST.get("dir")
    if dir == "":
        with io.open("code/%s/%s"%(request.session['sesion'],nombre), 'r', encoding='utf8') as f:
            text = f.read()
            return HttpResponse(text)
    else:
        with io.open("code/%s/%s/%s"%(request.session['sesion'],dir,nombre), 'r', encoding='utf8') as f:
            text = f.read()
            return HttpResponse(text)
    