from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from Apps.Accesos import models as models_accesos
from Apps.Accesos import serializers as AccesoSerializers
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
    return render(request, "index.html",{"dirs":carpetas})

def welcome_view(request):
    return render(request, "welcome.html")

class AccesoViewSet(viewsets.ModelViewSet):
    queryset = models_accesos.Acceso.objects.all()
    serializer_class = AccesoSerializers.AccesoSerializer