from django.db import models

# Create your models here.

class Funcionarios(models.Model):
    GENERO = (
        ('Homem','Homem'),
        ('Mulher','Mulher'),
        ('Indefinido','Indefinido'),
    )

    nome = models.CharField(max_length=255)
    genero = models.CharField(max_length=255)
    cpf = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    salario = models.DecimalField(max_digits=255, decimal_places=2)
    genero = models.CharField(max_length=255, choices=GENERO)

    def __str__(self):
        return self.nome
