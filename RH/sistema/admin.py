from django.contrib import admin
# 1. Importe seus modelos
from .models import Funcionario, Setor, Cargo, Curso, InscricaoCurso

# 2. Registre cada um deles
admin.site.register(Funcionario)
admin.site.register(Setor)
admin.site.register(Cargo)
admin.site.register(Curso)
admin.site.register(InscricaoCurso)
