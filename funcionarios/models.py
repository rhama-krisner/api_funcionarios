from django.db import models

# Create your models here.

class Funcionarios(models.Model):
   
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
