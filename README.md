🏢 Sistema de Gestão de RH (API)
Esta é uma API robusta para gerenciamento de recursos humanos, desenvolvida para controlar funcionários, setores, cargos e o histórico acadêmico (cursos) de cada colaborador.

O projeto foca em relacionamentos complexos, segurança via JWT e documentação interativa com Swagger.

🚀 Tecnologias Utilizadas
Python 3.13.4

Django 5.0+: Framework web principal.

Django Rest Framework (DRF): Criação da API RESTful.

MySQL: Banco de dados relacional para persistência.

Simple JWT: Autenticação segura via tokens.

drf-spectacular: Documentação automática com OpenAPI 3.0 (Swagger).

django-filter: Sistema avançado de busca, filtragem e ordenação.


🛠️ Funcionalidades Principais
Gestão de Funcionários: CRUD completo com validação de CPF.

Relações Muitos-para-Muitos (M2M): Histórico de cursos utilizando uma tabela intermediária (through) para armazenar dados extras como Instituição e Carga Horária.

Autenticação: Endpoints protegidos que exigem Token JWT no cabeçalho da requisição.

Filtros Inteligentes:

Busca por nome, CPF ou e-mail.

Filtro por Setor, Cargo ou Matrícula.

Ordenação por Salário ou Data de Contratação.

Documentação Interativa: Interface Swagger para testes em tempo real.

📦 Como Instalar e Rodar o Projeto

1: Clone o repositório:
git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio

2: Crie e ative o ambiente virtual:
python -m venv venv


# No Windows:
.\venv\Scripts\activate

3: Instale as dependências:
pip install -r requirements.txt

4: Configure o Banco de Dados:
No seu settings.py, ajuste as credenciais do MySQL

5: Rode as migrações:
python manage.py makemigrations
python manage.py migrate

6: Inicie o servidor:
python manage.py runserver

📑 Documentação da API
Após iniciar o servidor, acesse a documentação interativa:

Swagger UI: http://127.0.0.1:8000/api/docs/swagger/

Redoc: http://127.0.0.1:8000/api/docs/redoc/

🛡️ Exemplo de JSON (Funcionário com Cursos)
A API utiliza Nested Serializers para entregar dados completos em uma única requisição:

{
    "id": 1,
    "nome": "João batista",
    "cursos": [
        {
            "nome_curso": "Engenharia de Software",
            "instituicao": "Estácio",
            "carga_horaria": 4000,
            "concluido": false
        }
    ],
    "setor": 1,
    "cargo": 1,
    "salario": "4000.00"
}


🎓 Autor
Guilherme, Software engineer/Engenheiro de Software.

Foco em Desenvolvimento Backend com Python e Django.
