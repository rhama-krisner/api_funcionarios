from django.db import models

# Create your models here.

class Funcionarios(models.Model):
    genero = (
        (u'H', u'Homem'),
        (u'M', u'Mulher'),
        (u'N', u'Não Binário'),
    )

    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=3, choices=genero)
    cpf = models.CharField(max_length=11)
    cargo = models.CharField(max_length=20)
    salario = models.DecimalField(max_digits=6, decimal_places=2)
    data_nascimento = models.DateField()

def __str__(self):
    return self.nome
