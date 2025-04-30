from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from .models import Solicitacao

class IndexViewTests(TestCase):
    def test_index_view_returns_200(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Hello, world")

class SolicitacaoModelTest(TestCase):
    def test_criacao_solicitacao_valida(self):
        solicitacao = Solicitacao.objects.create(
            nome_solicitante="João Silva",
            setor_solicitante="TI",
            unidade="Bloco A",
            local_servico="Sala 101",
            tipo_servico="eletrico",
            tipo_manutencao="corretiva",
            outro_tipo_servico="",
            descricao_problema="Falta de energia na sala."
        )
        self.assertEqual(solicitacao.nome_solicitante, "João Silva")
        self.assertEqual(solicitacao.tipo_servico, "eletrico")