from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from .models import Procuracao
from .forms import ProcuracaoForm
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def home(request):
    hoje = timezone.localdate()
    # Pega todas as procurações do usuário
    procuracoes = list(Procuracao.objects.filter(usuario=request.user).order_by('data_vencimento'))

    # Inicializa as listas para a contagem no dashboard
    vencidas_list = []
    vencem_em_30_dias_list = []
    ativas_list = []
    
    # Itera sobre as procurações para definir status, prioridade e preencher as listas
    for proc in procuracoes:
        if proc.data_vencimento < hoje:
            proc.status = 'Expirada'
            proc.prioridade = 'Alta'
            vencidas_list.append(proc)
        elif proc.data_vencimento <= hoje + timedelta(days=30):
            proc.status = 'Vence em breve'
            proc.prioridade = 'Média'
            vencem_em_30_dias_list.append(proc)
        else:
            proc.status = 'Ativa'
            proc.prioridade = 'Baixa'
            ativas_list.append(proc)
    
    return render(request, 'procuracoes/home.html', {
        'total_procuracoes': len(procuracoes),
        'procuracoes': procuracoes,
        'vencidas': vencidas_list,
        'vencem_em_30_dias': vencem_em_30_dias_list,
        'ativas': ativas_list,
    })

@login_required
def cadastrar_procuracao(request):
    if request.method == 'POST':
        form = ProcuracaoForm(request.POST)
        if form.is_valid():
            procuracao = form.save(commit=False)
            procuracao.usuario = request.user
            procuracao.save()
            return redirect('home')
    else:
        form = ProcuracaoForm()
    return render(request, 'procuracoes/cadastrar_procuracao.html', {'form': form})

@login_required
def editar_procuracao(request, pk):
    procuracao = get_object_or_404(Procuracao, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = ProcuracaoForm(request.POST, instance=procuracao)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProcuracaoForm(instance=procuracao)
    return render(request, 'procuracoes/editar_procuracao.html', {'form': form, 'procuracao': procuracao})

@login_required
def excluir_procuracao(request, pk):
    procuracao = get_object_or_404(Procuracao, pk=pk, usuario=request.user)
    if request.method == 'POST':
        procuracao.delete()
        return redirect('home')
    return render(request, 'procuracoes/excluir_procuracao.html', {'procuracao': procuracao})

@login_required
def api_buscar_procuracoes(request):
    query = request.GET.get('q', '')
    procuracoes = Procuracao.objects.filter(usuario=request.user)
    if query:
        procuracoes = procuracoes.filter(
            Q(outorgante__icontains=query) | Q(outorgado__icontains=query) | Q(numero__icontains=query)
        )
    lista_procuracoes = list(procuracoes.values('numero','outorgante', 'outorgado', 'data_vencimento'))
    return JsonResponse({'procuracoes': lista_procuracoes})