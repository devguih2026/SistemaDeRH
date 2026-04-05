# 1. Importa o motor principal: o ModelViewSet já vem com as funções 
# de Listar, Criar, Ver Detalhes, Editar e Deletar prontas.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# 2. Importa o "Tradutor" (Serializer) criado na pasta API.
from sistema.api import serializers

# 3. Importa a "Planta do Banco" (Models) para saber onde buscar os dados.
from sistema import models

# 4. Criamos a Classe. O nome "Funcionarioviewsets" é usado no Router (urls.py).
class Funcionarioviewsets(viewsets.ModelViewSet):

    permission_classes = (IsAuthenticated, )
    
    # 5. "Use este tradutor para converter meus dados em JSON".
    serializer_class = serializers.funcionarioSerializer
    
    # 6. Define a "Fonte": "Vá na tabela Task e pegue todos os registros".
    queryset = models.Funcionario.objects.all()