from django.db import models

# Create your models here.

class Funcionarios(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    cargo = models.CharField(max_length=20)
    salario = models.CharField(max_length=6)
    data_nascimento = models.DateField()

def __str__(self):
    return self.nome
