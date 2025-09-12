from django import forms
from .models import Procuracao

class ProcuracaoForm(forms.ModelForm):
    class Meta:
        model = Procuracao
        fields = ['numero', 'outorgante', 'outorgado', 'data_emissao', 'data_vencimento', 'prioridade', 'status', 'observacoes']
        labels = {
            'numero': 'Número da Procuração',
            'outorgante': 'Outorgante',
            'outorgado': 'Outorgado',
            'data_emissao': 'Data de Emissão',
            'data_vencimento': 'Data de Vencimento',
            'prioridade': 'Prioridade',
            'status': 'Status',
            'observacoes': 'Observações',
        }
        widgets = {
            'numero': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Número único identificador da procuração'}),
            'outorgante': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Nome completo do outorgante'}),
            'outorgado': forms.TextInput(attrs={'class': 'form-control', 'required': True, 'placeholder': 'Nome completo do outorgado'}),
            'data_emissao': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control', 'required': True}),
            'data_vencimento': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date', 'class': 'form-control', 'required': True}),
            'prioridade': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'observacoes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Observações adicionais sobre a procuração...', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Corrige para manter as datas preenchidas no editar
        for field in ['data_emissao', 'data_vencimento']:
            if self.instance and getattr(self.instance, field):
                self.initial[field] = getattr(self.instance, field).strftime('%Y-%m-%d')
