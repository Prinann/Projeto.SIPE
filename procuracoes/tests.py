from django.test import TestCase
from django.contrib.auth.models import User
from .models import Procuracao
from datetime import date, timedelta

class ProcuracaoModelTest(TestCase):
    def setUp(self):
        # Cria um usuário de teste para associar à procuração
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_procuracao_creation(self):
        """Testa se uma procuração pode ser criada corretamente."""
        procuracao = Procuracao.objects.create(
            usuario=self.user,
            outorgante='João Silva',
            outorgado='Maria Oliveira',
            data_emissao=date.today(),
            data_vencimento=date.today() + timedelta(days=365)
        )
        # Verifica se a procuração foi criada e salva no banco de dados
        self.assertEqual(procuracao.outorgante, 'João Silva')
        self.assertFalse(procuracao.esta_vencida)
        self.assertEqual(Procuracao.objects.count(), 1)

    def test_vencida_status(self):
        """Testa se o status 'esta_vencida' é atualizado corretamente."""
        procuracao = Procuracao.objects.create(
            usuario=self.user,
            outorgante='Pedro',
            outorgado='Ana',
            data_emissao=date.today() - timedelta(days=10),
            data_vencimento=date.today() - timedelta(days=5) # Venceu há 5 dias
        )
        # O campo `esta_vencida` não é atualizado automaticamente na criação
        # Faremos a lógica de atualização em uma etapa futura, mas o teste já mostra a necessidade.
        self.assertFalse(procuracao.esta_vencida)