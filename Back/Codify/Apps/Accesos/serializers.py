from django.contrib.auth.models import User
from Apps.Documentos import models as models_documentos
from rest_framework import serializers

class AccesoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models_documentos.Documento
        fields = ['id', 'usuario', 'documento']