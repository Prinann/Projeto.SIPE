from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('procuracao/cadastrar/', views.cadastrar_procuracao, name='cadastrar_procuracao'),
    path('procuracao/editar/<int:pk>/', views.editar_procuracao, name='editar_procuracao'),
    path('procuracao/excluir/<int:pk>/', views.excluir_procuracao, name='excluir_procuracao'),
    path('api/buscar/', views.api_buscar_procuracoes, name='api_buscar_procuracoes'),
]
