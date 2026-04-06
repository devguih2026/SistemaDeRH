# 1. Importa o motor principal: o ModelViewSet já vem com as funções 
# de Listar, Criar, Ver Detalhes, Editar e Deletar prontas.
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend

# 2. Importa o "Tradutor" (Serializer) criado na pasta API.
from sistema.api import serializers

# 3. Importa a "Planta do Banco" (Models) para saber onde buscar os dados.
from sistema import models

@extend_schema(tags=['Funcionários'])
# 4. Criamos a Classe. O nome "Funcionarioviewsets" é usado no Router (urls.py).
class Funcionarioviewsets(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated, )
    
    # 5. "Use este tradutor para converter meus dados em JSON".
    serializer_class = serializers.funcionarioSerializer
    
    # 6. Define a "Fonte": "Vá na tabela Task e pegue todos os registros".
    queryset = models.Funcionario.objects.all()

    # --- CONFIGURAÇÃO DE FILTROS E BUSCAS ---
    
    # Define quais motores de busca a API vai usar
    filter_backends = [
        DjangoFilterBackend,    # Filtros exatos (ex: ?setor=1)
        filters.SearchFilter,   # Busca por texto (ex: ?search=Guilherme)
        filters.OrderingFilter  # Ordenação (ex: ?ordering=-salario)
    ]
    
    # Campos para filtro exato (Dropdowns no Swagger)
    filterset_fields = ['setor', 'cargo', 'matricula']
    
    # Campos onde o 'search' vai procurar o texto digitado
    search_fields = ['nome', 'cpf', 'email']
    
    # Campos que o usuário pode usar para ordenar a lista
    ordering_fields = ['nome', 'salario', 'data_contratacao']
    
    # Ordenação padrão (caso o usuário não escolha nenhuma)
    ordering = ['nome']