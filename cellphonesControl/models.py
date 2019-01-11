from django.db import models

# Create your models here.
class RecepcionMercancia(models.Model):
    subinventario = models.CharField(max_length=10, ${blank=False, null=False})
    nombre = models.CharField(max_length=50, ${blank=True, null=True})
    modelo = models.CharField(max_length=20, ${blank=True, null=True})
    imei = models.CharField(max_length=10, ${blank=True, null=True})
    folio = models.CharField(max_length=10, ${blank=True, null=True})

    def __str__(self):
        return '{} {}'.format(self.subinventario, self.nombre)
    
class OrdenCompra(models.Model):
    subinventario = models.ForeignKey('RecepcionMercancia', related_name='subinventario', on_delete=models.CASCADE)
    pvd = models.CharField(max_length= 50, ${blank=True, null=True})
    cantidadPedidos = models.IntegerField()
    comentario = models.CharField(max_length=100, ${blank=True, null=True})