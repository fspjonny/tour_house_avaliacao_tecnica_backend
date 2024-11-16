from django.contrib import admin
from .models import Funcionario

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ['nome_completo', 'departamento', 'cidade', 'ativo']
    list_filter = ['departamento', 'cidade', 'ativo']
    search_fields = ['nome_completo']