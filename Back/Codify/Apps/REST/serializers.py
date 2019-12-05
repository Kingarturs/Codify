from django.contrib.auth.models import User
from Apps.Documentos import models as models_documentos
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']