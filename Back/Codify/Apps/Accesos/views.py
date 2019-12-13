from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from Apps.Documentos.models import Accesos_b,Solicitudes_b
from Apps.Accesos import models as models_accesos
from Apps.Accesos import serializers as AccesoSerializers
from django.contrib.auth.models import User
import os
# Create your views here.
def login_view(request):
    if request.session.get('sesion'):
        return redirect("/index")
    else:
        return render(request, "login.html")
        
def index_view(request):
    user = request.session['sesion']
    carpetas = {}
    for base, dirs, files in os.walk("code/%s"%user):
        for i in dirs:
            carpetas[i] = os.listdir("code/%s/%s"%(user,i))
        carpetas[""] = files
        break
    s = Solicitudes_b.objects.filter(invitado_id = user)
    solicitudes = {}
    try:
        for i in s:
            solicitudes[i.id] = {"ruta":i.ruta,"nombre":str(i.ruta.split("/")[-1:][0 ]), "id_dueno":i.dueno_id, "id_invitado":i.invitado_id, "dueno":User.objects.get(pk = i.dueno_id).username, "invitado":User.objects.get(pk = i.invitado_id).username}
    except:
        pass
    accesos = {}
    a = Accesos_b.objects.filter(solicitud_id=request.session['sesion'])
    try:
        for i in a:
            if len(i.ruta.split("/")) == 3:
                accesos[i.id] = {"ruta":"","nombre":str(i.ruta.split("/")[-1:][0 ]), "id_dueno":i.destinatario_id}
            else:
                
                accesos[i.id] = {"ruta":i.ruta.split("/")[2],"nombre":str(i.ruta.split("/")[-1:][0 ]), "id_dueno":i.destinatario_id}
    except:
        pass
    print(accesos)
    return render(request, "index.html",{"dirs":carpetas,"soli":solicitudes, "acces":accesos,"usuario":request.session['sesion']})

def welcome_view(request):
    return render(request, "welcome.html")

class AccesoViewSet(viewsets.ModelViewSet):
    queryset = models_accesos.Acceso.objects.all()
    serializer_class = AccesoSerializers.AccesoSerializer