from rest_framework.test import APIClient
from rest_framework import status


# Usuários Administradores obtendo access token e refresh token
def test_admin_obtem_access_token(api_client_admin, admin_user):
    client = api_client_admin
    
    response = client.post('/api/token/', {'username': admin_user.username, 'password': 'admin1234'})
    
    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data
    assert 'refresh' in response.data

def test_admin_faz_refresh_token(api_client_admin, admin_user):
    client = api_client_admin
    
    obtain_response = client.post('/api/token/', {'username': admin_user.username, 'password': 'admin1234'})
    refresh_token = obtain_response.data['refresh']
    
    refresh_response = client.post('/api/token/refresh/', {'refresh': refresh_token})
    
    assert refresh_response.status_code == status.HTTP_200_OK
    assert 'access' in refresh_response.data


# Usuários Comuns obtendo access token e refresh token
def test_usuario_obtem_access_token(api_common_user, common_user):
    client = api_common_user
    
    response = client.post('/api/token/', {'username': common_user.username, 'password': 'test1234'})
    
    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data
    assert 'refresh' in response.data


def test_usuario_faz_refresh_token(api_common_user, common_user):
    client = api_common_user 
    
    obtain_response = client.post('/api/token/', {'username': common_user.username, 'password': 'test1234'})
    refresh_token = obtain_response.data['refresh']
    
    refresh_response = client.post('/api/token/refresh/', {'refresh': refresh_token})
    
    assert refresh_response.status_code == status.HTTP_200_OK
    assert 'access' in refresh_response.data
