from django.db import models
from django.contrib.auth.models import User
from Apps.Documentos import models as models_documentos

# Create your models here.

class Acceso(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    documento = models.ForeignKey(models_documentos.Documento, on_delete=models.CASCADE)
