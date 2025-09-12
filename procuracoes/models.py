from django.db import models
from django.contrib.auth.models import User

# Tipos de procuração Ad Judicia (exemplo)
TIPO_PROCURACAO_CHOICES = (
    ('AD_JUDICIA', 'Ad Judicia'),
    ('FINANCEIRA', 'Financeira'),
    ('GERAL', 'Geral'),
)

# Opções para Prioridade
PRIORIDADE_CHOICES = (
    ('low', 'Baixa'),
    ('medium', 'Média'),
    ('high', 'Alta'),
)

# Opções para Status
STATUS_CHOICES = (
    ('active', 'Ativa'),
    ('expired', 'Expirada'),
    ('renewed', 'Renovada'),
)

class Procuracao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    numero = models.CharField(max_length=100, verbose_name='Número da Procuração', unique=True, default='')
    tipo = models.CharField(
        max_length=50,
        choices=TIPO_PROCURACAO_CHOICES,
        default='AD_JUDICIA',
        verbose_name='Tipo de Procuração'
    )
    outorgante = models.CharField(max_length=200, verbose_name='Outorgante')
    outorgado = models.CharField(max_length=200, verbose_name='Outorgado')
    data_emissao = models.DateField(verbose_name='Data de Emissão')
    data_vencimento = models.DateField(verbose_name='Data de Vencimento')
    prioridade = models.CharField(max_length=10, choices=PRIORIDADE_CHOICES, default='medium', verbose_name='Prioridade')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active', verbose_name='Status')
    observacoes = models.TextField(blank=True, null=True, verbose_name='Observações')
    
    def __str__(self):
        return f'Procuração de {self.outorgante} para {self.outorgado}'

    class Meta:
        verbose_name = 'Procuração'
        verbose_name_plural = 'Procurações'