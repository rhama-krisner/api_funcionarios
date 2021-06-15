from django.contrib import admin
from funcionarios.models import Funcionarios

class Funcionario(admin.ModelAdmin):
    list_display: ('id','nome','cpf','cargo','data_nascimento')

admin.site.register(Funcionarios, Funcionario)