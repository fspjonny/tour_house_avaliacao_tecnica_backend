from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from empresas.views import EmpresaViewSet
from departamentos.views import DepartamentoViewSet
from funcionarios.views import FuncionarioViewSet
from django.http import JsonResponse

router = DefaultRouter()

router.register('empresas', EmpresaViewSet)
router.register('departamentos', DepartamentoViewSet) 
router.register('funcionarios', FuncionarioViewSet)

# Página inicial retorna uma resposta JSON mínima
def api_root(request):
    return JsonResponse({"message": "Bem-vindo à API, acesse /api/docs/ para documentação."})

urlpatterns = [
    path('', api_root),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

urlpatterns += [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]