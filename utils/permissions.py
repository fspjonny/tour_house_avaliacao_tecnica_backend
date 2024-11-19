from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Permite DELETE apenas para administradores (is_staff ou is_superuser).
    Usuários comuns podem fazer apenas métodos de leitura (GET, PUT, PATCH, etc...).
    """

    def has_permission(self, request, view):
        # Métodos seguros (GET, HEAD, OPTIONS) são permitidos para todos
        if request.method in SAFE_METHODS:
            return True
        # Para métodos de escrita, apenas administradores
        return request.user.is_staff or request.user.is_superuser
