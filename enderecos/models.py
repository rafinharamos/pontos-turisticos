from django.db import models

class Enderecos(models.Model):
    linha1 = models.TextField(max_length=250)
    linha2 = models.TextField(max_length=250, null=True, blank=True)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=100)
    latitude = models.IntegerField(null=True, blank=True)
    longitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.linha1

