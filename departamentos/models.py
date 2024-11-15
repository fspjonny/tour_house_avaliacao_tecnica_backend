from django.db import models
from empresas.models import Empresa

class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    centro_custo = models.CharField(max_length=50)
    codigo_integracao = models.CharField(max_length=50)
    ativo = models.BooleanField(default=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='departamentos')

    def __str__(self):
        return f"{self.nome} - {self.empresa.nome}"
