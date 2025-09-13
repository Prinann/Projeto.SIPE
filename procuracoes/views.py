from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import JsonResponse
from .models import Procuracao
from .forms import ProcuracaoForm
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import login
from django.contrib.auth.models import User

# ------------------------------
# View para login como visitante
# ------------------------------
def login_como_visitante(request):
    # Usuário visitante com login e senha padrão
    username = 'visitante'
    senha = 'visitante123'  # senha padrão

    # Tenta buscar o usuário, cria se não existir
    visitante, criado = User.objects.get_or_create(username=username)
    if criado:
        visitante.set_password(senha)
        visitante.save()

    # Faz login automático
    login(request, visitante)

    # Redireciona para o painel principal
    return redirect('home')

# ------------------------------
# Views originais
# ------------------------------

@login_required
def home(request):
    hoje = timezone.localdate()

    # Se for visitante, pega todas as procurações do sistema (visualização)
    if request.user.username == 'visitante':
        procuracoes = list(Procuracao.objects.all().order_by('data_vencimento'))
    else:
        procuracoes = list(Procuracao.objects.filter(usuario=request.user).order_by('data_vencimento'))

    # Inicializa listas para contagem no dashboard
    vencidas_list = []
    vencem_em_30_dias_list = []
    ativas_list = []
    
    # Itera sobre as procurações para definir status e prioridade
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
    # Bloqueia acesso do visitante à criação
    if request.user.username == 'visitante':
        return redirect('home')

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
    if request.user.username == 'visitante':
        return redirect('home')  # Bloqueia visitante

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
    if request.user.username == 'visitante':
        return redirect('home')  # Bloqueia visitante

    procuracao = get_object_or_404(Procuracao, pk=pk, usuario=request.user)
    if request.method == 'POST':
        procuracao.delete()
        return redirect('home')
    return render(request, 'procuracoes/excluir_procuracao.html', {'procuracao': procuracao})

@login_required
def api_buscar_procuracoes(request):
    if request.user.username == 'visitante':
        procuracoes = Procuracao.objects.all()
    else:
        procuracoes = Procuracao.objects.filter(usuario=request.user)

    query = request.GET.get('q', '')
    if query:
        procuracoes = procuracoes.filter(
            Q(outorgante__icontains=query) | Q(outorgado__icontains=query) | Q(numero__icontains=query)
        )
    lista_procuracoes = list(procuracoes.values('numero','outorgante', 'outorgado', 'data_vencimento'))
    return JsonResponse({'procuracoes': lista_procuracoes})
