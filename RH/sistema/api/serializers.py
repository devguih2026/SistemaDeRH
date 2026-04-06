from rest_framework import serializers
from sistema.models import Funcionario, InscricaoCurso, Curso

# 1. Primeiro, um serializer para a "Inscrição" (a tabela de ligação)
class InscricaoCursoSerializer(serializers.ModelSerializer):
    # Isso traz o nome do curso em vez de apenas o ID
    nome_curso = serializers.ReadOnlyField(source='curso.nome')

    class Meta:
        model = InscricaoCurso
        fields = ['curso', 'nome_curso', 'instituicao', 'carga_horaria', 'concluido']

# 2. Agora, o serializer do Funcionário
class funcionarioSerializer(serializers.ModelSerializer):
    # Mudamos o campo cursos para ler os dados da tabela InscricaoCurso
    # O 'source' aponta para o conjunto de inscrições desse funcionário
    cursos = InscricaoCursoSerializer(many=True, source='inscricaocurso_set', read_only=True)

    class Meta:
        model = Funcionario
        fields = "__all__"

def validate_cpf(self, value):
        cpf_limpo = value.replace('.', '').replace('-', '')

        if len(cpf_limpo) != 11:
            raise serializers.ValidationError("O CPF deve ter 11 dígitos.")
        
        if cpf_limpo == cpf_limpo[0] * 11:
            raise serializers.ValidationError("CPF inválido (números repetidos).")

        return value