from django.db import models

class Setor(models.Model):
    nome = models.CharField(max_length=100)

class Cargo(models.Model):
    nome = models.CharField(max_length=100)

class Curso(models.Model):
    nome = models.CharField(max_length=100) # Mudei para 'nome' para seguir o padrão

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.IntegerField()
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField()
    email = models.EmailField(max_length=254, unique=True)
    data_contratacao = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE) 
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
   
    cursos = models.ManyToManyField(Curso, through='InscricaoCurso')

class InscricaoCurso(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    
    instituicao = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()
    data_conclusao = models.DateField(null=True, blank=True) 
    concluido = models.BooleanField(default=False)