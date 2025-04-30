from django.db import models

# Create your models here.
from django.db import models

class Solicitacao(models.Model):
    TIPO_SERVICO_CHOICES = [
        ("eletrico", "Elétrico"),
        ("hidraulico", "Hidráulico"),
        ("refrigeracao", "Refrigeração"),
        ("pintura", "Pintura"),
        ("outro", "Outro"),
    ]

    TIPO_MANUTENCAO_CHOICES = [
        ("corretiva", "Corretiva"),
        ("preventiva", "Preventiva"),
        ("melhoria", "Melhoria"),
    ]

    nome_solicitante = models.CharField(max_length=100)
    setor_solicitante = models.CharField(max_length=100)
    unidade = models.CharField(max_length=100)
    local_servico = models.CharField(max_length=200)
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    tipo_servico = models.CharField(max_length=20, choices=TIPO_SERVICO_CHOICES)
    tipo_manutencao = models.CharField(max_length=20, choices=TIPO_MANUTENCAO_CHOICES)
    outro_tipo_servico = models.CharField(max_length=100, blank=True, null=True)
    descricao_problema = models.TextField()

    def __str__(self):
        return f"{self.nome_solicitante} - {self.tipo_servico}"
