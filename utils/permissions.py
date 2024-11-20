from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Permite acesso de leitura (GET, OPTIONS, HEAD) apenas para usuários autenticados.
    Métodos de escrita (POST, PUT, PATCH, DELETE) são restritos a administradores.
    """

    def has_permission(self, request, view):
        # Apenas usuários autenticados podem acessar
        if not request.user.is_authenticated:
            return False
        # Métodos seguros (GET, HEAD, OPTIONS) são permitidos para usuários autenticados
        if request.method in SAFE_METHODS:
            return True
        # Para métodos de escrita, apenas administradores
        return request.user.is_staff or request.user.is_superuser
