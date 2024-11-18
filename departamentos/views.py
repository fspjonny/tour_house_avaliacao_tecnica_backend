from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Departamento
from .serializers import DepartamentoSerializer
from utils.permissions import IsAdminOrReadOnly
from utils.pagination import CustomPageNumberPagination

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [IsAdminOrReadOnly]
    pagination_class = CustomPageNumberPagination

    # Definindo métodos HTTP permitidos
    http_method_names = ['get', 'post', 'put', 'delete']    

    # Filtro de registros
    def get_queryset(self):
        user = self.request.user
        # Se o usuário for um administrador, a consulta retorna todos os departamentos, mesmo inativos.
        if user.is_staff or user.is_superuser:
            return Departamento.objects.all()
        # Caso contrário, retorna apenas os departamentos ativos
        return Departamento.objects.filter(ativo=True)
    
    # Desativa o registro ao invés de excluir(Só ADM's)
    def destroy(self, request, *args, **kwargs):
            instance = self.get_object()
            instance.ativo = False
            instance.save()
            return Response(
                 {"detail": "Registro foi inativado com sucesso."}, 
                 status=status.HTTP_202_ACCEPTED
                )
