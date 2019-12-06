from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from Apps.Accesos import models as models_accesos
from Apps.Accesos import serializers as AccesoSerializers

# Create your views here.
def login_view(request):
    if request.session.get('sesion'):
        return redirect("/index")
    else:
        return render(request, "login.html")
        
def index_view(request):
    return render(request, "index.html")

def welcome_view(request):
    return render(request, "welcome.html")

class AccesoViewSet(viewsets.ModelViewSet):
    queryset = models_accesos.Acceso.objects.all()
    serializer_class = AccesoSerializers.AccesoSerializer