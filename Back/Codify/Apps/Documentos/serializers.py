from django.contrib.auth.models import User
from Apps.Documentos import models as models_documentos
from rest_framework import serializers

class DocumentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models_documentos.Documento
        fields = ['id', 'nombre', 'lenguaje', 'ruta', 'proyecto']

class CarpetaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models_documentos.Carpeta
        fields = ['id', 'nombre', 'username']