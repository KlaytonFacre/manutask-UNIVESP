from django.db import models
from datetime import datetime
from django import forms


# Create your models here.
class Pessoa(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=100)


class Oficina(models.Model):
    id_supervisor = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE
    )
    nome = models.CharField(max_length=20)


class Imovel(models.Model):
    id_locador = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE
    )
    rua = models.CharField(max_length=50)
    numero = models.IntegerField()
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6
    )


class OrdemServico(models.Model):
    id_reclamante = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        null=False,
        related_name='reclamante'
    )
    id_imovel = models.ForeignKey(
        Imovel,
        on_delete=models.CASCADE,
        null=False
    )
    timestamp_abertura = models.DateTimeField(
        default=datetime.now()
    )
    id_oficina_responsavel = models.ForeignKey(
        Oficina,
        on_delete=models.CASCADE
    )
    descricao_problema = models.TextField(max_length=255)
    timestamp_solucao = models.DateTimeField()
    descricao_solucao = models.TextField(max_length=255)
    id_solucionador = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        related_name='solucionador',
        default=1
    )
