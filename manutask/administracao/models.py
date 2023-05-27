from django.db import models
from datetime import datetime
# from django import forms


# Entidades do sistema
class Pessoa(models.Model):
    cpf = models.CharField(max_length=11)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=100)

    def __repr__(self):
        return f'{self.nome} {self.sobrenome}'

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'


class Oficina(models.Model):
    id_supervisor = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE
    )
    nome = models.CharField(max_length=20)

    def __repr__(self):
        return f'{self.nome}'

    def __str__(self):
        return f'{self.nome}'


class Imovel(models.Model):
    id_locador = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE
    )
    rua = models.CharField(max_length=50)
    numero = models.IntegerField()
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True
    )

    def __repr__(self):
        return f'{self.rua}, {self.numero}'

    def __str__(self):
        return f'{self.rua}, {self.numero}'


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
        on_delete=models.CASCADE,
        null=True
    )
    descricao_problema = models.TextField(max_length=255, null=False)
    timestamp_solucao = models.DateTimeField(null=True)
    descricao_solucao = models.TextField(max_length=255, null=True)
    id_solucionador = models.ForeignKey(
        Pessoa,
        on_delete=models.CASCADE,
        related_name='solucionador',
        default=1,
        null=True
    )
