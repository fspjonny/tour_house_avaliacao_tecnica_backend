from rest_framework import status


# Testando se o usuário é admin
def test_meu_user_é_admin(admin_user):
    usuario = admin_user
    assert usuario.is_superuser

# Testando se o usuário não é admin
def test_meu_user_não_é_admin(common_user):
    usuario = common_user
    assert not usuario.is_superuser

# Testando se os dados de acesso do usuário podem acessar a API
def test_admin_dados_de_acesso(api_client_admin):
    client = api_client_admin
    
    response = client.post('/api/token/', {'username': 'administrador', 'password': 'superadmin'})
    
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.data['detail'] == 'Usuário e/ou senha incorreto(s)'

def test_usuario_dados_de_acesso(api_common_user):
    client = api_common_user
    
    response = client.post('/api/token/', {'username': 'testador', 'password': 'tester1234'})
    
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.data['detail'] == 'Usuário e/ou senha incorreto(s)'
