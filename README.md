# S.I.P.E. - Sistema Integrado de Procurações Eletrônicas

## Descrição
O S.I.P.E. é um sistema web desenvolvido em Django para auxiliar na gestão e alerta de vencimento de procurações eletrônicas. Ele permite cadastro, edição, exclusão e busca de procurações, além de fornecer um dashboard com estatísticas e alertas de vencimento.

---

## Tecnologias Utilizadas

**Backend:**
- Python 3.x
- Django
- SQLite3 (para desenvolvimento)

**Frontend:**
- HTML5, CSS3, JavaScript
- Bootstrap 5.3
- Font Awesome 6.4

**Ferramentas:**
- VS Code
- Git para controle de versão

---

## Funcionalidades

- Dashboard com estatísticas de procurações (Total, Vencidas, Próximos 30 dias, Ativas)
- CRUD completo de procurações:
  - Cadastrar nova procuração
  - Editar procuração existente
  - Excluir procuração
  - Visualizar detalhes
- Pesquisa e filtros por número, outorgante, outorgado e status
- Sistema de login e logout utilizando Django
- Layout responsivo com Bootstrap e interativo com JavaScript

---

## Instalação

1. Clone o repositório:
```bash
git clone <URL_DO_REPOSITORIO>
cd SIPE
Crie um ambiente virtual e ative-o:

bash
Copiar código
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Execute as migrações:

bash
Copiar código
python manage.py migrate
Crie um superusuário (opcional):

bash
Copiar código
python manage.py createsuperuser
Execute o servidor de desenvolvimento:

bash
Copiar código
python manage.py runserver
Acesse o sistema no navegador:

cpp
Copiar código
http://127.0.0.1:8000/
Próximos Passos
Implementar alertas automáticos de vencimento por e-mail

Adicionar registro de novos usuários

Melhorias visuais e gráficos interativos

Preparar para implantação em servidor web

