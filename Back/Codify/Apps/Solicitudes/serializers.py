from django.contrib.auth.models import User
from Apps.Solicitudes import models as models_solicitudes
from rest_framework import serializers

class SolicitudSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models_solicitudes.Solicitud
        fields = ['id', 'documento', 'recibe', 'envia', 'fecha', 'estatus']