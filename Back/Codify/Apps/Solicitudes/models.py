from django.db import models
from django.contrib.auth.models import User
from Apps.Documentos import models as models_documentos
import datetime

# Create your models here.
class Solicitud(models.Model):
    documento = models.ForeignKey(models_documentos.Documento, on_delete=models.CASCADE)
    recibe = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recibe')
    envia = models.ForeignKey(User, on_delete=models.CASCADE, related_name='envia')
    fecha = models.DateField(default=datetime.date.today)
    estatus = models.CharField(max_length=1, choices=[(1, "Pendiente"), (2, "Aceptado"), (3, "Rechazado")])