from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from enderecos.models import Enderecos
# Create your models here.

class PontosTuristicos(models.Model):
    nome = models.CharField(max_length=260)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracao = models.ManyToManyField(Atracao)
    comentarios = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    endereco = models.ForeignKey(Enderecos, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome
