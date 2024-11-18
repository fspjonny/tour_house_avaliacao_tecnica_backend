from django.db import models
from departamentos.models import Departamento

class Funcionario(models.Model):
    nome_completo = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    data_contratacao = models.DateField()
    data_demissao = models.DateField(null=True, blank=True, default=None)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    cep = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.nome_completo
