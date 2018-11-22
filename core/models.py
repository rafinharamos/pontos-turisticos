from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
# Create your models here.

class PontosTuristicos(models.Model):
    nome = models.CharField(max_length=260)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracao = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)

    def __str__(self):
        return self.nome
