from django.db import models

# Create your models here.
class RecepcionMercancia(models.Model):
    subinventario = models.CharField(max_length=10, ${blank=True, null=True})
    nombre = models.CharField(max_length=50, ${blank=True, null=True})
    modelo = models.CharField(max_length=20, ${blank=True, null=True})
    imei = models.CharField(max_length=10, ${blank=True, null=True})
    folio = models.CharField(max_length=10, ${blank=True, null=True})

    def __str__(self):
        return '{} {}'.format(self.subinventario, self.nombre)
    