from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, filters
from .models import Funcionario
from .serializers import FuncionarioSerializer
from utils.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from django_filters import CharFilter


# Definindo que o filtro deve encontrar qualquer ocorrência maiúscula ou minúscula no campo cidade e departamento.
class FuncionarioFilter(FilterSet):
    cidade = CharFilter(field_name='cidade', lookup_expr='icontains')
    departamento = CharFilter(field_name='departamento__nome', lookup_expr='icontains')

    class Meta:
        model = Funcionario
        fields = ['cidade', 'departamento']


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    permission_classes = [IsAdminOrReadOnly] # Só ADM tem permissão de inativar funcionários

    # Definindo filtros conforme especificado no desafio.
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['departamento', 'cidade']
    filterset_class = FuncionarioFilter
    
    # Definindo métodos HTTP permitidos
    http_method_names = ['get', 'post', 'put', 'delete']    

    # Filtro de registros
    def get_queryset(self):
        user = self.request.user
        # Se o usuário for um administrador, a consulta retorna todos os funcionários, mesmo inativos.
        if user.is_staff or user.is_superuser:
            return Funcionario.objects.all()
        # Caso contrário, retorna apenas os funcionários ativos
        return Funcionario.objects.filter(ativo=True)
    
    # Desativa o registro ao invés de excluí-lo(Só ADM's)
    def destroy(self, request, *args, **kwargs):
            instance = self.get_object()
            instance.ativo = False
            instance.data_demissao = timezone.now()
            instance.save()
            return Response(
                 {"detail": "Registro foi inativado com sucesso."}, 
                 status=status.HTTP_202_ACCEPTED
                )
    
    